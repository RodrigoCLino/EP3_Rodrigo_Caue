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
          self.turn = 2
          print(self.matriz_geral)
       elif self.turn == 2:
          self.matriz_geral[linha][coluna]="O"
          self.turn = 1
          print(self.matriz_geral)
          
   def verifica_ganhador(self):
        
        if self.matriz_geral[0][0] =="X" and self.matriz_geral[0][1] == "X" and self.matriz_geral[0][2] == "X ":
                return 1
        elif self.matriz_geral[0][0] =="O" and self.matriz_geral[0][1] == "O" and self.matriz_geral[0][2] == "O":
                return 2
        elif self.matriz_geral[1][0] == "X" and self.matriz_geral[1][1] == "X" and self.matriz_geral[1][2] == "X":            
                return 1
        elif self.matriz_geral[1][0] == "O" and self.matriz_geral[1][1] == "O" and self.matriz_geral[1][2] == "O": 
                return 2
        elif self.matriz_geral[2][0] == "X" and self.matriz_geral[2][1] == "X" and self.matriz_geral[2][2] == "X":            
                return 1
        elif self.matriz_geral[2][0] == "O" and self.matriz_geral[2][1] == "O" and self.matriz_geral[2][2] == "O":  
                return 2
        elif self.matriz_geral[0][0] == "X" and self.matriz_geral[1][0] == "X" and self.matriz_geral[2][0] == "X":
                return 1
        elif self.matriz_geral[0][0] == "O" and self.matriz_geral[1][0] == "O" and self.matriz_geral[2][0] == "O":
                return 2
        elif self.matriz_geral[0][1] == "X" and self.matriz_geral[1][1] == "X" and self.matriz_geral[2][1] == "X":
                return 1
        elif self.matriz_geral[0][1] == "O" and self.matriz_geral[1][1] == "O" and self.matriz_geral[2][1] == "O":
                return 2
        elif self.matriz_geral[0][2] == "X" and self.matriz_geral[1][2] == "X" and self.matriz_geral[2][2] == "X":
                return 1
        elif self.matriz_geral[0][2] == "O" and self.matriz_geral[1][2] == "O" and self.matriz_geral[2][2] == "O":
                return 2
        elif self.matriz_geral[0][0] == "X" and self.matriz_geral[1][1] == "X" and self.matriz_geral[2][2] == "X":
                return 1
        elif self.matriz_geral[0][0] == "O" and self.matriz_geral[1][1] == "O" and self.matriz_geral[2][2] == "O":
                return 2
        elif self.matriz_geral[0][2] == "X" and self.matriz_geral[1][1] == "X" and self.matriz_geral[2][0] == "X":
                return 1
        elif self.matriz_geral[0][2] == "O" and self.matriz_geral[1][1] == "O" and self.matriz_geral[2][0] == "O":
                return 2 
        elif self.matriz_geral[0][0]!=0 and self.matriz_geral[0][1]!=0 and self.matriz_geral[0][2]!=0 and self.matriz_geral[1][0]!=0 and self.matriz_geral[1][1]!=0 and self.matriz_geral[1][2]!=0 and self.matriz_geral[2][0]!=0 and self.matriz_geral[2][1]!=0 and self.matriz_geral[2][2]!=0:
            return 0
            
   def limpa_jogadas(self):
        self.turn = 1
        self.matriz_geral=[[0,0,0],[0,0,0],[0,0,0]]
        self.lista_jogadas = []
           
       
       
       