class Jogo:
  
   def __init__(self):
       self.turn = 1
       self.matriz_geral=[[0,0,0],[0,0,0],[0,0,0]]
       self.lista_jogadas=[]
       self.Vg=0
       
   def iniciar(self):
       self.window.mainloop()
   
   def recebe_jogada(self,linha,coluna):
       if self.turn % 2 == 0:
          self.botão0_0.configure(text=" X ")
          self.botão0_0.configure(font="Arial 50")
          self.matriz_geral[linha][coluna]="X"
          self.verifica_ganhador("X")
       else:
          self.botão0_0.configure(text=" O ")
          self.botão0_0.configure(font="Arial 50")
          self.matriz_geral[linha][coluna]="O"
          self.verifica_ganhador("O")
       self.turn += 1
   
       

   def verifica_ganhador(self,jogador):
        self.lista_jogadas.append(jogador)
        
        if self.matriz_geral[0][0] == jogador and self.matriz_geral[0][1] == jogador and self.matriz_geral[0][2] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[1][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[1][2] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[2][0] == jogador and self.matriz_geral[2][1] == jogador and self.matriz_geral[2][2] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][0] == jogador and self.matriz_geral[2][0] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[0][1] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][1] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][2] == jogador and self.matriz_geral[2][2] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][2] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][0] == jogador:
            return (self.label_turno.configure(text="Vitoria Jogador {0}" .format(jogador)),self.Vg==1)
        elif len(self.lista_jogadas)==9:
            return (self.label_turno.configure(text="Velha"),self.Vg==-1)
            
   def limpa_jogadas(self):
        if self.Vg==1 or self.Vg==-1:
            self.matriz_geral=[[0,0,0],[0,0,0],[0,0,0]]
            
            
        
        
             