import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import keyboard

#If you want to save the graphs
record=False

class Graph:
    def __init__(self,x,y,board):
        """
            Creating the global figure
        """
        self.fig = plt.figure()
        self.x = x
        self.y = y
        #init of the figure at the first step
        self.update(0,board)
        
    def update(self,step,board):
        """
            Updating the figure, depending on the actual board
        """
        #Cleaning the figure
        self.fig.clear()
        ax = self.fig.add_subplot(1, 1, 1)
        #Add the title of the current board
        ax.set_title("Generation :"+str(step))
        plt.xlim(0,self.x)
        plt.ylim(0,self.y)

        grid_x_ticks = np.arange(0, self.x, 1)
        grid_y_ticks = np.arange(0, self.y, 1)

        #Creating the grid of the subplot in order to look like a chessboard
        ax.set_xticks(grid_x_ticks , minor=True)
        ax.set_yticks(grid_y_ticks , minor=True)
        ax.grid(which='both', alpha=0.4, linestyle='-')

        #removing w and y axis
        plt.xticks([])
        plt.yticks([])

        #Adding a black square where it belongs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==1:
                    rect = pat.Rectangle((j,len(board)-i-1),1,1)
                    rect.set_color("black")
                    ax.add_patch(rect)

        #Making a pause
        #Not usefull if the board is too large because it'll take time to compute the new board
        plt.pause(0.05)

        #Saving the figure in the img folder
        try:
            global record
            if record==True:
                self.fig.savefig("img/"+str(100000+step)+".png")
        except Exception as e:
            print(e)

def next_generation(board):
    """
        Updating the board for the new generation
    """
    new = []
    for i in range(len(board)):
        ligne = []
        for j in range(len(board[0])):

            #Var which saves the number of 1 arounf the current square
            count = 0
            
            #Check the 8*8 square around the current square
            for m in range(i-1,i+2):
                for n in range(j-1,j+2):
                    #Removing the forbidden square
                    if not(m==i and n==j) and (m>-1 and m<len(board)) and (n>-1 and n<len(board[0])):
                        count+=board[m][n]
                        
            #Making the update, based on the rules of the game of life
            if board[i][j]==0:
                if count==3:
                    ligne.append(1)
                else:
                    ligne.append(0)
            else :
                if count==2 or count==3:
                    ligne.append(1)
                else:
                    ligne.append(0)
        new.append(ligne)
    return new

def main(board):
    
    #Creating the main graph which display the chessboard
    graph = Graph(len(board[0]),len(board),board)
    step = 1
    loop=True
    
    #Main loop
    while loop:
        board = next_generation(board)
        graph.update(step,board)
        step+=1
        
        #We can stop the loop by pressing space
        if keyboard.is_pressed('space'):
            loop=False

if __name__=="__main__":
    try:
        
        """
            Converting the file into an array of integers
        """
        f = open(sys.argv[1],"r")
        board = []
        for ligne in f:
            ligne = (ligne.split(","))
            ligne = [int(value) for value in ligne]
            board.append(ligne)
        #if the last line is empty, will remove it
        if len(board[-1])==0:
            board = board[:-1]
        main(board)
    except Exception as e:
        print(e)
