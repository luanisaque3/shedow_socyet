import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import time
import threading
from pynput.keyboard import Controller

class TecladoVirtualGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⌨️ Teclado Virtual 1.1.0")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Cores
        self.bg_color = "#1a1a2e"
        self.fg_color = "#eaeaea"
        self.accent_color = "#00d4ff"
        self.success_color = "#00ff88"
        self.warning_color = "#ffaa00"
        
        self.root.configure(bg=self.bg_color)
        
        # Configurar estilo
        self.setup_styles()
        
        # Variáveis
        self.keyboard = Controller()
        self.is_typing = False
        self.delay = 0.05
        
        # Criar interface
        self.create_widgets()
    
    def setup_styles(self):
        """Configura os estilos dos widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar cores
        style.configure('TLabel', background=self.bg_color, foreground=self.fg_color)
        style.configure('TButton', font=('Arial', 10))
        style.configure('TCombobox', font=('Arial', 10))
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'), foreground=self.accent_color)
        style.configure('Title.TLabel', font=('Arial', 14, 'bold'))
    
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        
        # ===== HEADER =====
        header_frame = tk.Frame(self.root, bg=self.bg_color)
        header_frame.pack(fill=tk.X, padx=20, pady=15)
        
        header_label = ttk.Label(header_frame, text="⌨️ EMULADOR DE TECLADO VIRTUAL", style='Header.TLabel')
        header_label.pack(side=tk.LEFT)
        
        version_label = ttk.Label(header_frame, text="v1.1.0 Premium", foreground=self.success_color)
        version_label.pack(side=tk.RIGHT)
        
        # ===== ÁREA DE ENTRADA =====
        input_frame = tk.LabelFrame(self.root, text="📝 Texto para Digitar", bg=self.bg_color, fg=self.accent_color, font=('Arial', 11, 'bold'))
        input_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Botões para inserir texto
        button_frame = tk.Frame(input_frame, bg=self.bg_color)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        btn_digitar = tk.Button(button_frame, text="✏️ Digitar Texto", command=self.limpar_texto, 
                               bg=self.accent_color, fg=self.bg_color, font=('Arial', 9, 'bold'), 
                               padx=10, pady=5, cursor="hand2")
        btn_digitar.pack(side=tk.LEFT, padx=5)
        
        btn_arquivo = tk.Button(button_frame, text="📁 Carregar Arquivo", command=self.carregar_arquivo,
                               bg=self.warning_color, fg=self.bg_color, font=('Arial', 9, 'bold'),
                               padx=10, pady=5, cursor="hand2")
        btn_arquivo.pack(side=tk.LEFT, padx=5)
        
        btn_exemplo = tk.Button(button_frame, text="📖 Usar Exemplo", command=self.usar_exemplo,
                               bg=self.success_color, fg=self.bg_color, font=('Arial', 9, 'bold'),
                               padx=10, pady=5, cursor="hand2")
        btn_exemplo.pack(side=tk.LEFT, padx=5)
        
        btn_limpar = tk.Button(button_frame, text="🗑️ Limpar", command=self.limpar_texto,
                              bg="#ff4444", fg="white", font=('Arial', 9, 'bold'),
                              padx=10, pady=5, cursor="hand2")
        btn_limpar.pack(side=tk.RIGHT, padx=5)
        
        # Área de texto
        self.text_area = scrolledtext.ScrolledText(input_frame, height=12, font=('Courier', 10),
                                                   bg="#0f0f1e", fg=self.accent_color,
                                                   insertbackground=self.accent_color)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ===== CONFIGURAÇÕES =====
        config_frame = tk.LabelFrame(self.root, text="⚙️ Configurações", bg=self.bg_color, fg=self.accent_color, font=('Arial', 11, 'bold'))
        config_frame.pack(fill=tk.X, padx=20, pady=10)
        
        config_inner = tk.Frame(config_frame, bg=self.bg_color)
        config_inner.pack(fill=tk.X, padx=10, pady=10)
        
        # Velocidade
        velocity_label = ttk.Label(config_inner, text="⚡ Velocidade:")
        velocity_label.pack(side=tk.LEFT, padx=5)
        
        self.velocity_var = tk.StringVar(value="normal")
        velocity_combo = ttk.Combobox(config_inner, textvariable=self.velocity_var,
                                     values=["🐢 Lento (0.15s)", "🚶 Normal (0.05s)", 
                                            "🏃 Rápido (0.02s)", "⚡ Muito Rápido (0.01s)"],
                                     state="readonly", width=25)
        velocity_combo.pack(side=tk.LEFT, padx=5)
        velocity_combo.bind("<<ComboboxSelected>>", self.atualizar_velocidade)
        
        # Informações
        info_frame = tk.Frame(config_frame, bg=self.bg_color)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.info_label = ttk.Label(info_frame, text="📊 Caracteres: 0 | ⏱️ Tempo estimado: 0s")
        self.info_label.pack(side=tk.LEFT, padx=5)
        
        # ===== STATUS =====
        status_frame = tk.LabelFrame(self.root, text="📡 Status", bg=self.bg_color, fg=self.accent_color, font=('Arial', 11, 'bold'))
        status_frame.pack(fill=tk.X, padx=20, pady=10)
        
        self.status_label = ttk.Label(status_frame, text="✅ Pronto para usar", foreground=self.success_color)
        self.status_label.pack(padx=10, pady=10)
        
        # Barra de progresso
        self.progress = ttk.Progressbar(status_frame, mode='determinate', length=400)
        self.progress.pack(fill=tk.X, padx=10, pady=5)
        
        # ===== BOTÕES PRINCIPAIS =====
        button_main_frame = tk.Frame(self.root, bg=self.bg_color)
        button_main_frame.pack(fill=tk.X, padx=20, pady=15)
        
        self.btn_iniciar = tk.Button(button_main_frame, text="▶️ INICIAR DIGITAÇÃO", 
                                    command=self.iniciar_digitacao,
                                    bg=self.success_color, fg=self.bg_color,
                                    font=('Arial', 12, 'bold'), padx=20, pady=10,
                                    cursor="hand2", activebackground="#00dd77")
        self.btn_iniciar.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        self.btn_cancelar = tk.Button(button_main_frame, text="⏹️ CANCELAR",
                                     command=self.cancelar_digitacao,
                                     bg="#ff4444", fg="white",
                                     font=('Arial', 12, 'bold'), padx=20, pady=10,
                                     cursor="hand2", state=tk.DISABLED)
        self.btn_cancelar.pack(side=tk.LEFT, padx=5)
        
        # Footer
        footer = tk.Frame(self.root, bg=self.bg_color)
        footer.pack(fill=tk.X, padx=20, pady=10)
        
        footer_label = ttk.Label(footer, text="Criado por Plascoy ❤️  |  Python 3.7+  |  Powered by pynput")
        footer_label.pack(side=tk.RIGHT)
    
    def atualizar_velocidade(self, event=None):
        """Atualiza a velocidade de digitação"""
        velocidades = {
            "🐢 Lento (0.15s)": 0.15,
            "🚶 Normal (0.05s)": 0.05,
            "🏃 Rápido (0.02s)": 0.02,
            "⚡ Muito Rápido (0.01s)": 0.01
        }
        self.delay = velocidades.get(self.velocity_var.get(), 0.05)
        self.atualizar_info()
    
    def atualizar_info(self):
        """Atualiza as informações de caracteres e tempo estimado"""
        texto = self.text_area.get("1.0", tk.END).strip()
        total_chars = len(texto)
        tempo_estimado = total_chars * self.delay
        
        minutos = int(tempo_estimado // 60)
        segundos = int(tempo_estimado % 60)
        
        self.info_label.config(
            text=f"📊 Caracteres: {total_chars:,} | ⏱️ Tempo estimado: {tempo_estimado:.1f}s ({minutos}m {segundos}s)"
        )
    
    def limpar_texto(self):
        """Limpa a área de texto"""
        self.text_area.delete("1.0", tk.END)
        self.atualizar_info()
        self.status_label.config(text="✅ Pronto para usar", foreground=self.success_color)
    
    def carregar_arquivo(self):
        """Carrega texto de um arquivo"""
        arquivo = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt"), ("Todos", "*.*")])
        if arquivo:
            try:
                with open(arquivo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", conteudo)
                self.atualizar_info()
                self.status_label.config(text=f"✅ Arquivo carregado: {arquivo.split('/')[-1]}", foreground=self.success_color)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar arquivo:\n{str(e)}")
    
    def usar_exemplo(self):
        """Usa o texto de exemplo padrão"""
        exemplo = """Clara adorava observar o sítio da família ao amanhecer. O cheiro da terra molhada e o canto dos passarinhos sempre fizeram parte de sua vida. Porém, nos últimos anos, ela percebeu que algo estava mudando. As árvores ao redor do riacho estavam desaparecendo, a água diminuía e a plantação já não produzia como antes.

Seu pai acreditava que a solução era aumentar a área de cultivo, derrubando o pouco de mata que restava. Clara, preocupada, decidiu procurar ajuda com dona Helena, uma agrônoma aposentada que morava perto dali.

A senhora explicou que a natureza precisava de equilíbrio. Ensinou sobre preservação das nascentes, adubação natural e cultivo consciente. Clara ficou encantada e resolveu colocar tudo em prática no sítio.

No início, o pai não acreditou muito nas ideias da filha. Mesmo assim, ela começou a plantar árvores frutíferas perto do riacho e criou uma pequena composteira para transformar restos orgânicos em adubo. Também convenceu os vizinhos a participarem de um mutirão para recuperar a mata ciliar.

Com o passar do tempo, o vale começou a mudar. A água voltou a correr mais forte, borboletas reapareceram e a terra ficou mais fértil. A produção melhorou sem destruir a natureza.

Durante a festa da colheita, os moradores perceberam que cuidar do meio ambiente não era um obstáculo para o agro, mas a chave para garantir alimento e qualidade de vida no futuro.

Clara sorriu ao ver o vale cheio de vida novamente. Ela sabia que pequenas atitudes podiam transformar o mundo inteiro."""
        
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", exemplo)
        self.atualizar_info()
        self.status_label.config(text="✅ Exemplo padrão carregado", foreground=self.success_color)
    
    def iniciar_digitacao(self):
        """Inicia a digitação em thread separada"""
        texto = self.text_area.get("1.0", tk.END).strip()
        
        if not texto:
            messagebox.showwarning("Aviso", "Por favor, insira um texto antes de começar!")
            return
        
        # Mostrar aviso
        resultado = messagebox.showinfo("Atenção", 
            "⚠️  Clique OK e então mude o foco para a janela onde deseja digitar!\n\n"
            "A digitação começará em 3 segundos...")
        
        if resultado is None:
            return
        
        # Desabilitar botão de iniciar e habilitar cancelar
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_cancelar.config(state=tk.NORMAL)
        self.is_typing = True
        
        # Iniciar digitação em thread
        thread = threading.Thread(target=self._executar_digitacao, args=(texto,), daemon=True)
        thread.start()
    
    def _executar_digitacao(self, texto):
        """Executa a digitação (rodando em thread)"""
        try:
            # Contagem regressiva
            for i in range(3, 0, -1):
                self.status_label.config(text=f"⏳ Iniciando em {i} segundos...", foreground=self.warning_color)
                time.sleep(1)
            
            self.status_label.config(text="✅ DIGITANDO AGORA!", foreground=self.success_color)
            self.progress['value'] = 0
            self.root.update()
            
            total_chars = len(texto)
            inicio = time.time()
            
            for i, char in enumerate(texto):
                if not self.is_typing:
                    break
                
                self.keyboard.type(char)
                time.sleep(self.delay)
                
                # Atualizar progresso a cada 50 caracteres
                if (i + 1) % 50 == 0 or i == total_chars - 1:
                    progresso = (i + 1) / total_chars * 100
                    self.progress['value'] = progresso
                    
                    tempo_decorrido = time.time() - inicio
                    self.status_label.config(
                        text=f"⏳ Digitando... {progresso:.1f}% ({i + 1}/{total_chars}) - {tempo_decorrido:.1f}s",
                        foreground=self.accent_color
                    )
                    self.root.update()
            
            if self.is_typing:
                tempo_total = time.time() - inicio
                self.progress['value'] = 100
                self.status_label.config(
                    text=f"✅ DIGITAÇÃO CONCLUÍDA! Tempo total: {tempo_total:.2f}s",
                    foreground=self.success_color
                )
                messagebox.showinfo("Sucesso", f"✅ Digitação concluída!\n\nTempo: {tempo_total:.2f}s\nCaracteres: {total_chars:,}")
            else:
                self.status_label.config(text="⏹️ Digitação cancelada", foreground=self.warning_color)
                self.progress['value'] = 0
        
        except Exception as e:
            self.status_label.config(text=f"❌ Erro: {str(e)}", foreground="#ff4444")
            messagebox.showerror("Erro", f"Erro durante digitação:\n{str(e)}")
        
        finally:
            self.is_typing = False
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_cancelar.config(state=tk.DISABLED)
    
    def cancelar_digitacao(self):
        """Cancela a digitação em andamento"""
        self.is_typing = False
        self.status_label.config(text="⏹️ Digitação cancelada", foreground=self.warning_color)
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_cancelar.config(state=tk.DISABLED)
        messagebox.showinfo("Cancelado", "Digitação foi cancelada!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TecladoVirtualGUI(root)
    root.mainloop()
