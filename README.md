# Desafio Ransomware da DIO

Bem-vindo ao repositório do Desafio Ransomware da DIO, foi criada uma ferramenta para praticar as técnicas de desenvolvimento de Ransomware para aprendizado! Este projeto, desenvolvido por mim, Albino Marques, acompanhando o Bootcamp da DIO de CyberSegurança em parceria com o Santander(Santander Bootcamp Cibersegurança) permite criptografar arquivos e diretórios idealmente de teste, para compreender os riscos deste tipo de ferramentas, podendo, se for mal intencionado, manter como refém os dados até que suas demandas sejam atendidas.
Foram feitas algumas alterações no código em relação ao apresentado na aula para poder dar mais personalidade ao mesmo enquanto modularizava um pouco mais a o código com funções.

## Como Usar

1. **Executando o Ransomware:**
   - Certifique-se de ter o Python instalado em seu sistema.
   - Instale a biblioteca `pyaes` através do comando `pip install pyaes` no terminal.
   - Abra o terminal e execute `python encrypter.py`.
   - Siga as instruções para fornecer o caminho do arquivo ou diretório a ser criptografado.

2. **Descriptografando os Arquivos:**
   - Para desfazer o caos, execute `python decrypter.py`.
   - Novamente, siga as instruções para especificar o alvo da descriptografia.

## Ferramentas Utilizadas

- **Python:**
  - A linguagem de programação principal para a implementação do ransomware.

- **pyaes:**
  - Uma biblioteca Python para a criptografia AES (Advanced Encryption Standard), usada para garantir que os arquivos permaneçam inacessíveis.

- **pathlib:**
  - Uma biblioteca para manipulação de caminhos de arquivos e diretórios.


## Aviso Importante

Este ransomware é uma criação maliciosa destinada exclusivamente para fins educacionais. O uso deste código em ambientes não autorizados é estritamente proibido e ilegal. O autor não assume qualquer responsabilidade por atividades ilegais resultantes do uso deste software.

É crucial utilizar este código com extrema cautela e apenas em ambientes controlados para fins educativos e de pesquisa. O propósito deste projeto é fornecer insights sobre as ameaças de segurança cibernética e promover a conscientização sobre os perigos associados a esse tipo de atividade.

---
