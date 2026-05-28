# 📖 Guia de Instalação

## Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonar o repositório)

## Passo 1: Clonar o Repositório

```bash
git clone https://github.com/luanisaque3/shedow_socyet.git
cd shedow_socyet
```

## Passo 2: Criar Ambiente Virtual (Opcional mas Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

## Passo 4: Executar

```bash
python3 esc.py
```

---

Se tiver problemas, verifique:
- ✅ Python está instalado: `python3 --version`
- ✅ pip está instalado: `pip --version`
- ✅ Dependências foram instaladas: `pip list`