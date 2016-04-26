class Jogo:

   def __init__(self):
       self.turn = 1
       self.matriz_geral=[[0,0,0],[0,0,0],[0,0,0]]
   
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
       if self.matriz_geral[0][0] == jogador and self.matriz_geral[0][1] == jogador and self.matriz_geral[0][2] == jogador:
           return self.label_turno.configure(text="Vitoria {0}" .format(jogador))
       elif self.matriz_geral[1][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[1][2] == jogador:
           return 1
       elif self.matriz_geral[2][0] == jogador and self.matriz_geral[2][1] == jogador and self.matriz_geral[2][2] == jogador:
           return 1
       elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][0] == jogador and self.matriz_geral[2][0] == jogador:
           return 1
       elif self.matriz_geral[0][1] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][1] == jogador:
           return 1
       elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][2] == jogador and self.matriz_geral[2][2] == jogador:
           return 1
       elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][0] == jogador:
           return 1
   
   #def limpa_jogadas():

Tic = Jogo()