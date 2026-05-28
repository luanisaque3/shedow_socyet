# 🔨 Guia de Desenvolvimento

## Estrutura do Código

### Arquivo Principal: `esc.py`

#### Classe `Cores`
Define as cores ANSI para o terminal:

```python
class Cores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    # ... etc
```

#### Funções Principais

- `limpar_tela()` - Limpa o terminal
- `exibir_banner()` - Mostra o banner inicial
- `obter_texto()` - Obtém texto do usuário
- `escolher_velocidade()` - Menu de velocidade
- `exibir_resumo()` - Mostra resumo da digitação
- `contar_regressiva()` - Contagem de 5 segundos
- `digitar_texto()` - Executa a digitação
- `main()` - Função principal

## Dependências

```python
import time              # Para delays
import os              # Para limpar tela
from pynput.keyboard import Controller  # Para digitar
```

## Estrutura de Fluxo

```
main()
  ├── exibir_banner()
  ├── obter_texto()
  ├── limpar_tela()
  ├── exibir_banner()
  ├── escolher_velocidade()
  ├── exibir_resumo()
  ├── contar_regressiva()
  └── digitar_texto()
```

## Como Personalizar

### Mudar o Banner

Edite a função `exibir_banner()`:

```python
def exibir_banner():
    print("""
    Seu ASCII art aqui
    """)
```

### Adicionar Cores

Adicione à classe `Cores`:

```python
class Cores:
    NOVA_COR = '\033[CODIGO_ANSI_AQUI'
```

### Modificar Velocidades Padrão

Na função `escolher_velocidade()`:

```python
velocidades = {
    "1": (0.15, "🐢 Lento"),
    "2": (0.05, "🚶 Normal"),
    # Adicione mais
}
```

## Testando

```bash
# Teste básico
python3 esc.py

# Com exemplo padrão
# Escolha opção 3

# Com arquivo
# Escolha opção 2 e forneça o caminho
```

## Contribuindo

1. Fork o repositório
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Bugs Conhecidos

Nenhum no momento! 🎉

## Roadmap

- [ ] GUI com tkinter
- [ ] Suporte a múltiplos idiomas
- [ ] Gravação e reprodução de macros
- [ ] Plugin system

---

**Dúvidas?** Abra uma issue no GitHub!