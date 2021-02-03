import os
import sys

from pyshark.tshark.tshark_json import packet_from_json_packet
from pyshark.capture.live_capture import LiveCapture

class ImageCapture(LiveCapture):
    def __init__(self, interface=None, bpf_filter=None, display_filter='http.content_type contains "image" && http.response_for.uri contains "http"',
                 only_summaries=False, decryption_key=None, encryption_type='wpa-pwk', output_file=None, decode_as=None,
                 disable_protocol=None, tshark_path=None, override_prefs=None, capture_filter=None,
                 monitor_mode=False, use_json=False, include_raw=False, eventloop=None, custom_parameters=["-e", "http.response_for.uri"],
                 debug=False):

        super(ImageCapture, self).__init__(interface=interface, bpf_filter=bpf_filter, display_filter=display_filter,
                                          only_summaries=only_summaries, decryption_key=decryption_key, encryption_type=encryption_type,
                                          output_file=output_file, decode_as=decode_as, disable_protocol=disable_protocol,
                                          tshark_path=tshark_path, override_prefs=override_prefs, capture_filter=capture_filter,
                                          monitor_mode=monitor_mode, use_json=use_json, include_raw=include_raw,
                                          eventloop=eventloop, custom_parameters=custom_parameters,
                                          debug=debug)

    async def _get_packet_from_stream(self, stream, existing_data, got_first_packet=True, psml_structure=None):
        if self.use_json:
            packet, existing_data = self._extract_packet_json_from_data(existing_data,
                                                                        got_first_packet=got_first_packet)
        else:
            packet, existing_data = self._extract_tag_from_data(existing_data)

        if packet:
            if self.use_json:
                packet = packet_from_json_packet(packet, deduplicate_fields=self._json_has_duplicate_keys)
            else:
                packet = self._uri_from_xml_packet(packet)
            return packet, existing_data

        new_data = await stream.read(self.DEFAULT_BATCH_SIZE)
        existing_data += new_data

        if not new_data:
            raise EOFError()

        return None, existing_data

    def _uri_from_xml_packet(self, packet, search_string='http.response_for.uri" value="'):
        uri = str(packet)
        start_index = uri.index(search_string) + len(search_string)
        uri = uri[start_index:]
        end_index = uri.index('"')
        uri = uri[:end_index]

        return uri
