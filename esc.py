import time
import os
from pynput.keyboard import Controller

# Cores para terminal
class Cores:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[35m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def exibir_banner():
    """Exibe o banner inicial com ASCII art"""
    limpar_tela()
    print(f"\n{Cores.MAGENTA}{Cores.BOLD}")
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          ⌨️  EMULADOR DE TECLADO VIRTUAL ⌨️                  ║
║                                                               ║
║                    🚀 v1.0.0 Premium 🚀                       ║
║                                                               ║
║                  Criado por: Plascoy ❤️                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
    """)
    print(f"{Cores.ENDC}\n")

def exibir_linha_decorativa(caractere="="):
    """Exibe uma linha decorativa"""
    print(f"{Cores.CYAN}{caractere * 63}{Cores.ENDC}")

def obter_texto():
    """Obtém o texto do usuário"""
    print(f"{Cores.CYAN}{Cores.BOLD}📝 Como você deseja inserir o texto?{Cores.ENDC}\n")
    print(f"  {Cores.YELLOW}1{Cores.ENDC} - Digitar o texto agora")
    print(f"  {Cores.YELLOW}2{Cores.ENDC} - Ler de um arquivo (.txt)")
    print(f"  {Cores.YELLOW}3{Cores.ENDC} - Usar exemplo padrão\n")
    
    exibir_linha_decorativa()
    
    opcao = input(f"\n{Cores.BOLD}Escolha uma opção (1-3): {Cores.ENDC}").strip()
    
    if opcao == "1":
        print(f"\n{Cores.CYAN}{Cores.BOLD}✍️  Digite seu texto (pressione Enter 2x para terminar):{Cores.ENDC}\n")
        linhas = []
        linhas_vazias = 0
        
        while linhas_vazias < 1:
            linha = input()
            if linha == "":
                linhas_vazias += 1
            else:
                linhas_vazias = 0
                linhas.append(linha)
        
        return "\n".join(linhas)
    
    elif opcao == "2":
        caminho = input(f"\n{Cores.BOLD}📁 Digite o caminho do arquivo (.txt): {Cores.ENDC}").strip()
        try:
            with open(caminho, 'r', encoding='utf-8') as f:
                texto = f.read()
                print(f"{Cores.GREEN}✅ Arquivo carregado com sucesso!{Cores.ENDC}")
                return texto
        except FileNotFoundError:
            print(f"{Cores.RED}❌ Arquivo não encontrado!{Cores.ENDC}\n")
            return obter_texto()
        except Exception as e:
            print(f"{Cores.RED}❌ Erro ao ler arquivo: {e}{Cores.ENDC}\n")
            return obter_texto()
    
    elif opcao == "3":
        print(f"{Cores.GREEN}✅ Usando texto exemplo padrão...{Cores.ENDC}\n")
        return """Clara adorava observar o sítio da família ao amanhecer. O cheiro da terra molhada e o canto dos passarinhos sempre fizeram parte de sua vida. Porém, nos últimos anos, ela percebeu que algo estava mudando. As árvores ao redor do riacho estavam desaparecendo, a água diminuía e a plantação já não produzia como antes.

Seu pai acreditava que a solução era aumentar a área de cultivo, derrubando o pouco de mata que restava. Clara, preocupada, decidiu procurar ajuda com dona Helena, uma agrônoma aposentada que morava perto dali.

A senhora explicou que a natureza precisava de equilíbrio. Ensinou sobre preservação das nascentes, adubação natural e cultivo consciente. Clara ficou encantada e resolveu colocar tudo em prática no sítio.

No início, o pai não acreditou muito nas ideias da filha. Mesmo assim, ela começou a plantar árvores frutíferas perto do riacho e criou uma pequena composteira para transformar restos orgânicos em adubo. Também convenceu os vizinhos a participarem de um mutirão para recuperar a mata ciliar.

Com o passar do tempo, o vale começou a mudar. A água voltou a correr mais forte, borboletas reapareceram e a terra ficou mais fértil. A produção melhorou sem destruir a natureza.

Durante a festa da colheita, os moradores perceberam que cuidar do meio ambiente não era um obstáculo para o agro, mas a chave para garantir alimento e qualidade de vida no futuro.

Clara sorriu ao ver o vale cheio de vida novamente. Ela sabia que pequenas atitudes podiam transformar o mundo inteiro."""
    
    else:
        print(f"{Cores.RED}❌ Opção inválida! Tente novamente.{Cores.ENDC}\n")
        return obter_texto()

def escolher_velocidade():
    """Permite ao usuário escolher a velocidade de digitação"""
    print(f"\n{Cores.CYAN}{Cores.BOLD}⚡ Escolha a velocidade de digitação:{Cores.ENDC}\n")
    print(f"  {Cores.GREEN}1{Cores.ENDC} - 🐢 Lento (0.15s por caractere) - Fácil acompanhar")
    print(f"  {Cores.GREEN}2{Cores.ENDC} - 🚶 Normal (0.05s por caractere) - ⭐ RECOMENDADO")
    print(f"  {Cores.GREEN}3{Cores.ENDC} - 🏃 Rápido (0.02s por caractere) - Bom para testes")
    print(f"  {Cores.GREEN}4{Cores.ENDC} - ⚡ Muito rápido (0.01s por caractere) - Máxima velocidade\n")
    
    exibir_linha_decorativa()
    
    opcao = input(f"\n{Cores.BOLD}Escolha uma opção (1-4): {Cores.ENDC}").strip()
    
    velocidades = {
        "1": (0.15, "🐢 Lento"),
        "2": (0.05, "🚶 Normal"),
        "3": (0.02, "🏃 Rápido"),
        "4": (0.01, "⚡ Muito Rápido")
    }
    
    delay, nome = velocidades.get(opcao, (0.05, "🚶 Normal"))
    print(f"\n{Cores.YELLOW}Velocidade selecionada: {nome}{Cores.ENDC}\n")
    
    return delay

def exibir_resumo(texto, delay):
    """Exibe um resumo antes de iniciar"""
    total_chars = len(texto)
    tempo_estimado = total_chars * delay
    minutos = int(tempo_estimado // 60)
    segundos = int(tempo_estimado % 60)
    
    print(f"{Cores.BOLD}{Cores.BLUE}")
    exibir_linha_decorativa("═")
    print(f"║                    {'RESUMO DA DIGITAÇÃO':^43} ║")
    exibir_linha_decorativa("═")
    print(f"{Cores.ENDC}\n")
    
    print(f"  📊 {Cores.BOLD}Total de caracteres:{Cores.ENDC} {Cores.YELLOW}{total_chars:,}{Cores.ENDC}")
    print(f"  ⏱️  {Cores.BOLD}Tempo estimado:{Cores.ENDC} {Cores.YELLOW}{tempo_estimado:.1f}s{Cores.ENDC} ({minutos}min {segundos}s)")
    
    primeira_linha = texto.split('\n')[0][:52]
    print(f"  📝 {Cores.BOLD}Primeira linha:{Cores.ENDC} {Cores.CYAN}{primeira_linha}...{Cores.ENDC}\n")

def contar_regressiva():
    """Exibe contagem regressiva"""
    print(f"{Cores.BOLD}{Cores.RED}⚠️  AVISO: Mude o foco para a janela onde deseja digitar!{Cores.ENDC}")
    print(f"{Cores.BOLD}{Cores.YELLOW}Iniciando em:{Cores.ENDC}\n")
    
    for i in range(5, 0, -1):
        print(f"\r{Cores.BOLD}{Cores.YELLOW}     {i} segundo{'s' if i > 1 else ''}...{Cores.ENDC}   ", end="", flush=True)
        time.sleep(1)
    
    print(f"\r{Cores.GREEN}{Cores.BOLD}     ✓ DIGITANDO AGORA! 🎯{Cores.ENDC}          \n")
    time.sleep(0.5)

def digitar_texto(texto, delay):
    """Digita o texto com delay entre caracteres"""
    keyboard = Controller()
    total = len(texto)
    
    contar_regressiva()
    
    inicio = time.time()
    
    for i, char in enumerate(texto):
        keyboard.type(char)
        time.sleep(delay)
        
        # Mostra progresso a cada 50 caracteres
        if (i + 1) % 50 == 0 or i == total - 1:
            progresso = (i + 1) / total * 100
            tempo_decorrido = time.time() - inicio
            
            # Barra de progresso
            barra_tamanho = 30
            barra_preenchida = int((progresso / 100) * barra_tamanho)
            barra = "█" * barra_preenchida + "░" * (barra_tamanho - barra_preenchida)
            
            print(f"\r  {Cores.CYAN}[{barra}] {progresso:6.1f}% ({i + 1:,}/{total}) - {tempo_decorrido:.1f}s{Cores.ENDC}", end="", flush=True)
    
    tempo_total = time.time() - inicio
    
    print(f"\n\n{Cores.GREEN}{Cores.BOLD}")
    exibir_linha_decorativa("═")
    print(f"║                {'✅ DIGITAÇÃO CONCLUÍDA!':^43} ║")
    exibir_linha_decorativa("═")
    print(f"{Cores.ENDC}\n")
    
    print(f"  {Cores.BOLD}Tempo total:{Cores.ENDC} {Cores.YELLOW}{tempo_total:.2f}s{Cores.ENDC}")
    print(f"  {Cores.BOLD}Caracteres digitados:{Cores.ENDC} {Cores.YELLOW}{total:,}{Cores.ENDC}")
    print(f"  {Cores.BOLD}Velocidade média:{Cores.ENDC} {Cores.YELLOW}{(total/tempo_total):.0f} chars/s{Cores.ENDC}\n")

def main():
    """Função principal"""
    exibir_banner()
    
    # Obter texto
    texto = obter_texto()
    
    if not texto or texto.isspace():
        print(f"\n{Cores.RED}❌ Nenhum texto foi inserido!{Cores.ENDC}\n")
        return
    
    limpar_tela()
    exibir_banner()
    
    # Escolher velocidade
    delay = escolher_velocidade()
    
    # Exibir resumo
    exibir_resumo(texto, delay)
    
    input(f"{Cores.BOLD}➜ Pressione ENTER para iniciar a digitação...{Cores.ENDC}")
    
    # Digitar
    digitar_texto(texto, delay)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Cores.YELLOW}{Cores.BOLD}⚠️  Digitação interrompida pelo usuário.{Cores.ENDC}\n")
        print(f"{Cores.CYAN}Obrigado por usar! 👋{Cores.ENDC}\n")
    except Exception as e:
        print(f"\n{Cores.RED}{Cores.BOLD}❌ Erro: {e}{Cores.ENDC}\n")