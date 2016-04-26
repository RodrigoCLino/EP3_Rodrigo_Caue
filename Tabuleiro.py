import tkinter as tk

import jogo

class Tabuleiro:
    def __init__(self):
        #Chama class Jogo
        self.jogo = jogo.Jogo()     
        
        #Interface
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("300x330+100+100")
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
        
        self.turn = 1
         
        self.label_turno = tk.Label(self.window)
        if self.turn % 2 == 0:
            self.label_turno.configure(text="Turno de: X ")
        else:
            self.label_turno.configure(text="Turno de: O ")
        self.label_turno.grid(row=3, columnspan=3, sticky="nsew")
        
    
    def iniciar(self):
        self.window.mainloop()
        
    def clicou(self, i, j):
        print("Botão {0} - {1} clicado" .format(i,j))
            
    def botão0_0_clicado(self):
        self.clicou(0,0)
        if self.turn % 2 == 0:
           self.botão0_0.configure(text=" X ")
           self.botão0_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,0)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão0_0.configure(text=" O ")
           self.botão0_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,0)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão0_0.configure(state="disabled")
    
    def botão0_1_clicado(self):
        self.clicou(0,1)
        if self.turn % 2 == 0:
           self.botão0_1.configure(text=" X ")
           self.botão0_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,1)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão0_1.configure(text=" O ")
           self.botão0_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,1)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão0_1.configure(state= "disabled")
        
    def botão0_2_clicado(self):
        self.clicou(0,2)
        if self.turn % 2 == 0:
           self.botão0_2.configure(text=" X ")
           self.botão0_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,2)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão0_2.configure(text=" O ")
           self.botão0_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(0,2)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão0_2.configure(state= "disabled")      
          
    def botão1_0_clicado(self):
        self.clicou(1,0)
        if self.turn % 2 == 0:
           self.botão1_0.configure(text=" X ")
           self.botão1_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,0)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão1_0.configure(text=" O ")
           self.botão1_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,0)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão1_0.configure(state= "disabled")
        
    def botão1_1_clicado(self):
        self.clicou(1,1)
        if self.turn % 2 == 0:
           self.botão1_1.configure(text=" X ")
           self.botão1_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,1)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão1_1.configure(text=" O ")
           self.botão1_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,1)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão1_1.configure(state= "disabled")
        
    def botão1_2_clicado(self):
        self.clicou(1,2)
        if self.turn % 2 == 0:
           self.botão1_2.configure(text=" X ")
           self.botão1_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,2)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão1_2.configure(text=" O ")
           self.botão1_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(1,2)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão1_2.configure(state= "disabled")         
            
    def botão2_0_clicado(self):
        self.clicou(2,0)
        if self.turn % 2 == 0:
           self.botão2_0.configure(text=" X ")
           self.botão2_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,0)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão2_0.configure(text=" O ")
           self.botão2_0.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,0)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão2_0.configure(state= "disabled")
        
    def botão2_1_clicado(self):
        self.clicou(2,1)
        if self.turn % 2 == 0:
           self.botão2_1.configure(text=" X ")
           self.botão2_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,1)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão2_1.configure(text=" O ")
           self.botão2_1.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,1)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão2_1.configure(state= "disabled")
        
    def botão2_2_clicado(self):
        self.clicou(2,2)
        if self.turn % 2 == 0:
           self.botão2_2.configure(text=" X ")
           self.botão2_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,2)
           if self.jogo.verifica_ganhador == 1:
               self.label_turno.configure(text="Vitória Jogador X")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        else:
           self.botão2_2.configure(text=" O ")
           self.botão2_2.configure(font="Arial 50")
           self.jogo.recebe_jogada(2,2)
           if self.jogo.verifica_ganhador == 2:
               self.label_turno.configure(text="Vitória Jogador O")
           elif self.jogo.verifica_ganhador == -1:
               self.label_turno.configure(text="Velha")
        self.turn += 1
        self.botão2_2.configure(state= "disabled")

TicTac = Tabuleiro()
TicTac.iniciar()