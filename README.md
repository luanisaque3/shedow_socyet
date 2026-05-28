<div align="center">

# ⌨️ TECLADO VIRTUAL 1.1.0

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Stars](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](https://github.com/luanisaque3)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen)](https://github.com/luanisaque3/TECLADO_virtual_110.0)
[![Version](https://img.shields.io/badge/Version-1.1.0-blue)](#)

> 🚀 **Emulador de Teclado Virtual avançado e colorido para Python**
> 
> Digite textos automaticamente com estilo, velocidade personalizável e interface incrível!

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square&logo=python)
![pynput](https://img.shields.io/badge/Powered%20by-pynput-orange?style=flat-square)

---

</div>

## ✨ Features

- 🎨 **Interface Colorida e Moderna** - Terminal com cores ANSI
- ⚡ **4 Velocidades Diferentes** - De lento a ultra-rápido
- 📊 **Barra de Progresso** - Acompanhe a digitação em tempo real
- 📝 **3 Formas de Entrada** - Digitar, arquivo ou exemplo padrão
- 🎯 **Digitação Precisa** - Simula digitação humana
- ⏱️ **Tempo Estimado** - Veja quanto tempo levará
- 🛡️ **Tratamento de Erros** - Mensagens claras e úteis
- 🔧 **Fácil de Usar** - Interface intuitiva e bem organizada

## 🎯 Como Usar

### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/luanisaque3/TECLADO_virtual_110.0.git
cd TECLADO_virtual_110.0

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute o script
python3 esc.py
```

### Uso

```bash
python3 esc.py
```

**O script vai te guiar por:**

1. 📝 **Escolher como inserir o texto:**
   - Digitar manualmente
   - Carregar de um arquivo
   - Usar exemplo padrão

2. ⚡ **Escolher a velocidade:**
   - 🐢 Lento (0.15s)
   - 🚶 Normal (0.05s) ⭐ Recomendado
   - 🏃 Rápido (0.02s)
   - ⚡ Muito Rápido (0.01s)

3. 📊 **Ver resumo da digitação:**
   - Total de caracteres
   - Tempo estimado
   - Primeira linha do texto

4. ▶️ **Iniciar a digitação automaticamente**

## 📋 Requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

## 📦 Dependências

- `pynput` - Para controlar o teclado virtual

Instale com:
```bash
pip install -r requirements.txt
```

## 📚 Documentação

- [📖 Guia de Instalação](docs/INSTALACAO.md)
- [🎮 Guia de Uso](docs/USO.md)
- [🔨 Guia de Desenvolvimento](docs/DESENVOLVIMENTO.md)

## 💡 Exemplos

### Exemplo 1: Texto Simples
```bash
python3 esc.py
# Escolher opção 1 e digitar seu texto
# Escolher velocidade 2 (Normal)
```

### Exemplo 2: Arquivo
```bash
python3 esc.py
# Escolher opção 2
# Digitar: exemplos/exemplo1.txt
```

### Exemplo 3: Modo Rápido
```bash
python3 esc.py
# Escolher opção 3 (Exemplo padrão)
# Escolher velocidade 4 (Muito Rápido)
```

## 🎨 Interface

A interface é super colorida e intuitiva:

```
╔═══════════════════════════════════════════════════════════════╗
║          ⌨️  EMULADOR DE TECLADO VIRTUAL  ⌨️                  ║
║                    🚀 v1.1.0 Premium 🚀                       ║
║                  Criado por: Plascoy ❤️                       ║
╚═══════════════════════════════════════════════════════════════╝

📝 Como você deseja inserir o texto?

1 - Digitar o texto agora
2 - Ler de um arquivo (.txt)
3 - Usar exemplo padrão
```

## 🚀 Dicas de Uso

- ⏸️ Pressione `CTRL+C` para cancelar a digitação
- 🎯 Use velocidade "Normal" para melhor acompanhamento
- 📄 Crie seus próprios arquivos `.txt` na pasta `exemplos/`
- ⏱️ O tempo estimado é calculado antes de iniciar

## 🐛 Resolução de Problemas

### "ModuleNotFoundError: No module named 'pynput'"
```bash
pip install pynput
```

### Digitação não funciona
- Certifique-se de que a janela alvo está em foco
- Teste com um editor de texto simples primeiro (Notepad, VS Code, etc)

### Velocidade muito rápida/lenta
- Use as opções de velocidade do menu
- Ou modifique manualmente o valor de `delay` no código

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Criado por:** [Plascoy](https://github.com/luanisaque3)

Feito com ❤️ e Python

---

<div align="center">

**[⬆ Voltar ao topo](#teclado-virtual-110)**

Se gostou, não se esqueça de dar uma ⭐!

</div>
