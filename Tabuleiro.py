import tkinter as tk

import jogo

class Tabuleiro:
    def __init__(self):
        #Chama class Jogo
        self.jogo = jogo.Jogo()     
        
        #Interface
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("500x550+100+100")
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=30, weight=1)
        self.window.rowconfigure(4, minsize=60, weight=1)
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
        #Botoões
        self.botão0_0 = tk.Button(self.window)
        self.botão0_0.grid(row=0, column=0, sticky="nsew")
        self.botão0_0.configure(command=self.botão0_0_clicado)
         
        self.botão0_1 = tk.Button(self.window)
        self.botão0_1.grid(row=0, column=1, sticky="nsew")
        self.botão0_1.configure(command=self.botão0_1_clicado)
          
        self.botão0_2 = tk.Button(self.window)
        self.botão0_2.grid(row=0, column=2, sticky="nsew")
        self.botão0_2.configure(command=self.botão0_2_clicado)
     
        self.botão1_0 = tk.Button(self.window)
        self.botão1_0.grid(row=1, column=0, sticky="nsew")
        self.botão1_0.configure(command=self.botão1_0_clicado)
         
        self.botão1_1 = tk.Button(self.window)
        self.botão1_1.grid(row=1, column=1, sticky="nsew")
        self.botão1_1.configure(command=self.botão1_1_clicado)
          
        self.botão1_2 = tk.Button(self.window)
        self.botão1_2.grid(row=1, column=2, sticky="nsew")
        self.botão1_2.configure(command=self.botão1_2_clicado)
       
        self.botão2_0 = tk.Button(self.window)
        self.botão2_0.grid(row=2, column=0, sticky="nsew")
        self.botão2_0.configure(command=self.botão2_0_clicado)
         
        self.botão2_1 = tk.Button(self.window)
        self.botão2_1.grid(row=2, column=1, sticky="nsew")
        self.botão2_1.configure(command=self.botão2_1_clicado)
          
        self.botão2_2 = tk.Button(self.window)
        self.botão2_2.grid(row=2, column=2, sticky="nsew")
        self.botão2_2.configure(command=self.botão2_2_clicado)
        
        self.botão_reinicia=tk.Button(self.window)
        self.botão_reinicia.grid(row=4, column=1, sticky="nsew") 
        self.botão_reinicia.configure(text="reiniciar")
        self.botão_reinicia.configure(command=self.botão_reinicia_clicado)
        
        self.turn = 1
         
        self.label_turno = tk.Label(self.window)
        if self.turn == 1:
            self.label_turno.configure(text="Turno de: X ")
        elif self.turn == 2:
            self.label_turno.configure(text="Turno de: O ")
        self.label_turno.grid(row=3, columnspan=3, sticky="nsew")
           
    def iniciar(self):
        self.window.mainloop()
                   
    def botão0_0_clicado(self):       
        if self.turn == 1:
           self.botão0_0.configure(text=" X ")
           self.botão0_0.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(0,0)
           self.verifica()
        elif self.turn == 2:
           self.botão0_0.configure(text=" O ")
           self.botão0_0.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(0,0)
           self.verifica()
        self.botão0_0.configure(state="disabled")
    
    def botão0_1_clicado(self):        
        if self.turn == 1:
           self.botão0_1.configure(text=" X ")
           self.botão0_1.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(0,1)
           self.verifica()
        else:
           self.botão0_1.configure(text=" O ")
           self.botão0_1.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(0,1)
           self.verifica()
        self.botão0_1.configure(state= "disabled")
        
    def botão0_2_clicado(self):
        if self.turn == 1:
           self.botão0_2.configure(text=" X ")
           self.botão0_2.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(0,2)
           self.verifica()
        else:
           self.botão0_2.configure(text=" O ")
           self.botão0_2.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(0,2)
           self.verifica()
        self.botão0_2.configure(state= "disabled")      
          
    def botão1_0_clicado(self):
        if self.turn == 1:
           self.botão1_0.configure(text=" X ")
           self.botão1_0.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(1,0)
           self.verifica()
        else:
           self.botão1_0.configure(text=" O ")
           self.botão1_0.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(1,0)
           self.verifica()
        self.botão1_0.configure(state= "disabled")
        
    def botão1_1_clicado(self):
        if self.turn == 1:
           self.botão1_1.configure(text=" X ")
           self.botão1_1.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(1,1)
           self.verifica()
        else:
           self.botão1_1.configure(text=" O ")
           self.botão1_1.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(1,1)
           self.verifica()
        self.botão1_1.configure(state= "disabled")
        
    def botão1_2_clicado(self):
        if self.turn == 1:
           self.botão1_2.configure(text=" X ")
           self.botão1_2.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(1,2)
           self.verifica()
        else:
           self.botão1_2.configure(text=" O ")
           self.botão1_2.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(1,2)
           self.verifica()
        self.botão1_2.configure(state= "disabled")         
            
    def botão2_0_clicado(self):
        if self.turn == 1:
           self.botão2_0.configure(text=" X ")
           self.botão2_0.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(2,0)
           self.verifica()
        else:
           self.botão2_0.configure(text=" O ")
           self.botão2_0.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(2,0)
           self.verifica()
        self.botão2_0.configure(state= "disabled")
        
    def botão2_1_clicado(self):
        if self.turn == 1:
           self.botão2_1.configure(text=" X ")
           self.botão2_1.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(2,1)
           self.verifica()
        else:
           self.botão2_1.configure(text=" O ")
           self.botão2_1.configure(font="Arial 35")
           self.turn = 1
           self.jogo.recebe_jogada(2,1)
           self.verifica()
        self.botão2_1.configure(state= "disabled")
        
    def botão2_2_clicado(self):
        if self.turn == 1:
           self.botão2_2.configure(text=" X ")
           self.botão2_2.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(2,2)
           self.verifica()
        else:
           self.botão2_2.configure(text=" O ")
           self.botão2_2.configure(font="Arial 35")
           self.turn = 2
           self.jogo.recebe_jogada(2,2)
           self.verifica() 
        self.botão2_2.configure(state= "disabled")
        
    def verifica(self): 
        if self.jogo.verifica_ganhador() == 1:      
            self.label_turno.configure(text="O vencedor é X!")
        elif self.jogo.verifica_ganhador() == 2:         
            self.label_turno.configure(text="O vencedor é O!")
        elif self.jogo.verifica_ganhador() == 0:
            self.label_turno.configure(text="Velha")
        else:
            return -1
   
    def botão_reinicia_clicado(self):
        self.jogo.limpa_jogadas()
        jogar=Tabuleiro()
        jogar.iniciar()
       


TicTac = Tabuleiro()
TicTac.iniciar()
