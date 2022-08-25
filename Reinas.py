class estado_tablero:
    __mboard = [None for _ in range(8)]
    __num_queen = 0

    def set_queen(self,row,col):
        self.__mboard[col]=row
        self.__num_queen += 1
    
    def del_queen(self,row,col):
        if self.__mboard:
            self.__mboard[col]=None
            self.__num_queen -= 1

    def num_queen(self):
        return self.__num_queen

    def get_board(self):
        return self.__mboard

class screen_tab:
    __matboard=[[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)],[None for _ in range(8)]]
    
    def screen(self,boards):
        for ind in range(0,8):
            if(boards[ind]!= None):
                    self.__matboard[boards[ind]][ind]="Q"
        
        print("\n")
        for fil in range(0,8):
            for col in range(0,8):
                print("|",self.__matboard[fil][col],end="")
            print("|\n")

Tablero = estado_tablero()
print (Tablero.get_board())

Tablero.set_queen(1,2)
print (Tablero.get_board())
Pantalla = screen_tab()
board=Tablero.get_board()
Pantalla.screen(board)