# Automação de Formulários EBD

Este projeto automatiza o preenchimento de formulários de participação na Escola Bíblica Dominical (EBD). Ele foi desenvolvido usando Python e a biblioteca Selenium para interagir com o navegador Chrome.

## Funcionalidades

- Preenche automaticamente CPFs de participantes.
- Seleciona opções em campos personalizados (`selectize`).
- Insere texto no editor Quill.
- Marca checkboxes e envia formulários.
- Processa múltiplos CPFs a partir de um arquivo de texto.

## Requisitos

Para executar este projeto, você precisará dos seguintes itens instalados:

1. **Python 3.x**: [Download Python](https://www.python.org/downloads/)
2. **Bibliotecas Python**:
   - `selenium`
   - `webdriver-manager`
3. **Navegador Google Chrome**: [Download Chrome](https://www.google.com/chrome/)
4. **Git** (opcional, para clonar o repositório): [Download Git](https://git-scm.com/)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio

2. **Crie e ative o ambiente virtual**:
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows

3. **Instale as dependências**:
   pip install -r requirements.txt

4. **COnfigure os arquivos de entrada**:
   cpfs.txt e participacao.txt

5. **Execute o script**:
   python preencher_formulario.py 

## 👤 Autor

Desenvolvido por https://github.com/Patrick-Jabba

## 🛡️ Licença

Este projeto está licenciado sob a [MIT License](LICENSE).



