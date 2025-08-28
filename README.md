## 🚀 Como rodar o projeto

### 1. Acesse a pasta do projeto
> Atenção: use aspas se o caminho tiver espaços ou acentos. (No meu caso uso o macOS)
```bash
mkdir "~/burger-app"
cd "~/burger-app"
```

### 2. Crie e ative um ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Instale as dependências
Instale as deps `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Rode a aplicação
```bash
python app.py
```

Acesse no navegador:
```
http://127.0.0.1:3000
```

### 🔧 Comandos úteis
- **Sair do ambiente virtual**:
  ```bash
  deactivate
  ```
- **Ativar o ambiente virtual novamente**:
  ```bash
  source .venv/bin/activate
  ```

---

## ✅ Requisitos
- Python 3 (instalado via [Homebrew](https://brew.sh))
- pip (já incluso no Python 3)
