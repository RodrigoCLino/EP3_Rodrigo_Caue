class Jogo:

   def __init__(self):
       self.turn = 1
       self.matriz_geral=[[0,0,0],[0,0,0],[0,0,0]]
       self.lista_jogadas = []
       
   def iniciar(self):
       self.window.mainloop()
   
   def recebe_jogada(self,linha,coluna):
       if self.turn == 1:
          self.matriz_geral[linha][coluna]="X"
          self.verifica_ganhador("X")
          print(self.matriz_geral)
          print(self.lista_jogadas)
          self.turn==2
       elif self.turn==2:
          self.matriz_geral[linha][coluna]="O"
          self.verifica_ganhador("O")
          print(self.matriz_geral)
          print(self.lista_jogadas)
          self.turn==1
       
       
   def verifica_ganhador(self,jogador):
        self.lista_jogadas.append(jogador)
        if jogador == "X":
            if self.matriz_geral[0][0] == jogador and self.matriz_geral[0][1] == jogador and self.matriz_geral[0][2] == jogador:
                return 1
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
            elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][2] == jogador:
                return 1
            elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][0] == jogador:
                return 1
        elif jogador == "O":
            if self.matriz_geral[0][0] == jogador and self.matriz_geral[0][1] == jogador and self.matriz_geral[0][2] == jogador:
                return 2
            elif self.matriz_geral[1][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[1][2] == jogador:
                return 2
            elif self.matriz_geral[2][0] == jogador and self.matriz_geral[2][1] == jogador and self.matriz_geral[2][2] == jogador:
                return 2
            elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][0] == jogador and self.matriz_geral[2][0] == jogador:
                return 2
            elif self.matriz_geral[0][1] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][1] == jogador:
                return 2
            elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][2] == jogador and self.matriz_geral[2][2] == jogador:
                return 2
            elif self.matriz_geral[0][0] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][2] == jogador:
                return 2
            elif self.matriz_geral[0][2] == jogador and self.matriz_geral[1][1] == jogador and self.matriz_geral[2][0] == jogador:
                return 2
        elif len(self.lista_jogadas) == 9:
            return -1
            
   #def limpa_jogadas():