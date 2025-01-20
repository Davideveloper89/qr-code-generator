# 🧾 Gerador de QR Code em Python

Um gerador simples de QR Code usando Python e a biblioteca `qrcode`.

---

## 📦 Requisitos

Antes de executar o código, certifique-se de que possui os seguintes requisitos instalados:

- **Python 3.7** ✔️
- **Biblioteca `qrcode`** ✔️

### 📥 Instalando o Python

#### 🖥️ Windows
1. Baixe o instalador em: [python.org](https://www.python.org/downloads/windows/)
2. Execute o instalador e selecione a opção **"Add Python to PATH"**
3. Conclua a instalação e verifique executando:
   ```bash
   python --version
   ```

#### 🍎 macOS
1. Instale via Homebrew:
   ```bash
   brew install python
   ```
2. Verifique a instalação com:
   ```bash
   python3 --version
   ```

#### 🐧 Linux

- **Debian/Ubuntu**
  ```bash
  sudo apt update && sudo apt install python3
  ```
- **Fedora**
  ```bash
  sudo dnf install python3
  ```
- **openSUSE**
  ```bash
  sudo zypper install python3
  ```
- **Alpine Linux**
  ```bash
  doas apk add python3
  ```

  Caso necessite compilar o Python manualmente no Alpine Linux:
  ```bash
  doas apk add --no-cache build-base python3-dev py3-pip
  wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
  tar -xvzf Python-3.7.0.tgz
  cd Python-3.7.0
  ./configure --enable-optimizations
  make
  doas make install
  ```

Verifique a instalação com:
```bash
python3 --version
```

### ⚙️ Instalando as Dependências

Após instalar o Python, instale a biblioteca necessária executando:

```bash
pip install qrcode[pil]
```

---

## 🚀 Como Usar

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/Davideveloper89/qr-code-generator.git
   cd qr-code-generator
   ```

2. Execute o script Python:

   ```bash
   python qr-code.py
   ```

3. Insira o texto ou URL quando solicitado.
4. O QR Code será gerado e salvo como `qrcode.png` no diretório atual.

---

## 🛠️ Estrutura do Código

O script contém as seguintes funções:

- **`gerar_qr_code(texto)`**: Gera um QR Code a partir do texto fornecido.
  - `version=1`: Define o tamanho do QR Code (1 é o menor).
  - `error_correction=qrcode.constants.ERROR_CORRECT_L`: Define o nível de correção de erro.
  - `box_size=10`: Define o tamanho de cada caixa (pixel).
  - `border=4`: Define o tamanho da borda.

- **`salvar_qr_code(img, nome_arquivo)`**: Salva a imagem gerada em um arquivo.

- **`main()`**: Função principal que solicita ao usuário o texto/URL, gera o QR Code e o salva.

---

## 📋 Exemplo de Uso

```bash
Digite o texto ou URL para gerar o QR Code: https://exemplo.com
QR Code gerado e salvo como 'qrcode.png'.
```

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

### 💡 Dicas

- Certifique-se de que tem permissão para salvar arquivos no diretório atual.
- Utilize URLs curtas para QR Codes mais limpos.

---

