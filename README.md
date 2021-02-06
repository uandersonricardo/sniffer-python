# sniffer-python

## Sobre o projeto

Projeto proposto pela cadeira IF678 - Infraestrutura de Comunicação, cujo objetivo é desenvolver um sniffer em Python, utilizando o PyShark. Além disso, o projeto tem por objetivo abordar na prática os protocolos de rede e a estrutura de camadas ensinados nas aulas.

## O código

O projeto foi desenvolvido em Python, fazendo uso das bibliotecas que estão listadas no arquivo ```requirements.txt```. A biblioteca PyShark apresentou alguns problemas na captura de alguns pacotes (sendo mais específico, ocorria erro de parse do XML/PDML que era capturado pelo Tshark), portanto uma nova classe ImageCapture (extendida a partir do LiveCapture) foi escrita, de forma que ela solicita apenas o RESPONSE_FOR_URI dos pacotes HTTP que contém imagem. Dessa forma, através de manipulação simples de strings, podemos obter os links das imagens sem qualquer problema.

Para facilitar a escolha da interface de rede, foi utilizada a biblioteca PyInquirer, que permitiu a criação de um CLI mais amigável.

## Funcionamento do projeto

![Demonstração](https://media.giphy.com/media/Ou4tCgRGNpM2N4tUA0/giphy.gif)

## Instalação

O projeto tem como pré-requisitos o ```python```, o ```wireshark``` e o ```tshark```.

```properties
# Para baixar o projeto
git clone https://github.com/uandersonricardo/sniffer-python.git

# Para instalar as bibliotecas
python -m pip install -r requirements.txt

# Para executar o projeto
python main.py
```