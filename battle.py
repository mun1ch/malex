#!/usr/bin/env python

import random



class main(object):
    def __init__(self):
        self.dot_list = []
        self.my_list = []
        self.cpu_list = []
        self.hit_list = []
        for x in 'abcdefghij':
            self.dot_list.append('.')
        for x in range (1,11):
            self.my_list.append(self.dot_list[:])    
            self.cpu_list.append(self.dot_list[:])    
            self.hit_list.append(self.dot_list[:])    

    def modify_my_list(self,x_cor,y_cor,value):
        self.my_list[x_cor][y_cor]=value

    def modify_cpu_list(self,x_cor,y_cor,value):
        self.cpu_list[x_cor][y_cor]=value

    def check_for_boats(self,x_cor,y_cor,length,direction,which_list):
        if which_list=='cpu':
            this_list = self.cpu_list 
        elif which_list=='my':
            this_list = self.my_list 

        while (length > 0):
            if direction==1:
                x_cor = x_cor + 1
            elif direction==2:
                y_cor = y_cor + 1
            elif direction==3:
                x_cor = x_cor - 1
            elif direction==4:
                y_cor = y_cor - 1
            if this_list[x_cor][y_cor]=='o':
                print "BOAT ! here: ",x_cor,y_cor,direction
                return True
            length = length - 1
        return False

    def set_boats(self,x_cor,y_cor,length,direction,which_list):
        if which_list=='cpu':
            set_this = self.modify_cpu_list
        elif which_list=='my':
            set_this = self.modify_my_list 
        set_this(x_cor,y_cor,'o')
        length = length - 1
        while (length > 0):
            if direction==1 or direction=='N':
                x_cor = x_cor - 1
            elif direction==2 or direction=='E':
                y_cor = y_cor + 1
            elif direction==3 or direction=='S':
                x_cor = x_cor + 1
            elif direction==4 or direction=='W':
                y_cor = y_cor - 1
            else:
                pass
            set_this(x_cor,y_cor,'o')
            length = length - 1

    def return_my_board(self):
        return self.my_list

    def return_cpu_board(self):
        return self.cpu_list

def print_board(board):
    letters = 'abcdefghijklmnop'
    letters = '0123456789'
    numbers = '   0   1   2   3   4   5   6   7   8   9'
    for x in range(0,10):
        print letters[x],
        for z in range(0,10):
            if board[x][z]=='.':
                print ' . ',
            elif board[x][z]=='x':
                print ' x ',
            elif board[x][z]=='o':
                print ' o ',
        print '\n' 
    print numbers



def return_random_boat(length):
        x = length
        x_rand = random.randint(0,9)
        y_rand = random.randint(0,9)
        rand_direction = random.randint(1,4)
        while((x_rand -x) < 0):
            x_rand = x_rand + 1
        while((y_rand -x) < 0):
            y_rand = y_rand + 1
        while((x_rand + x) > 9):
            x_rand = x_rand - 1
        while((y_rand + x) > 9):
            y_rand = y_rand - 1
        print "Coordinates: (%d,%d) & Direction: %s" % (x_rand,y_rand,rand_direction)
        return (x_rand,y_rand,x,rand_direction)


if __name__=="__main__":
    game = main()
    my_board = game.return_my_board() 
    cpu_board = game.return_cpu_board() 

    print_board(my_board)
## Setting boats for the CPU
    for i in 2,3,3,5,7:
        infinite_loop = 0
        boat_check = True 
        while boat_check:
            y,x,length,direction = return_random_boat(i)
            boat_check = game.check_for_boats(x,y,length,direction,"cpu")
            print boat_check, "There is a boat here"
            infinite_loop = infinite_loop + 1
            if infinite_loop > 300:
                exit("GAHHHH INFINITE LOOP")
        game.set_boats(x,y,length,direction,"cpu")
        user_y,user_x,user_direction = input("Return an X,Y, and DIRECTION for your %d length boat i.e 2,2,'N': " % i) 
        game.set_boats(user_x,user_y,i,user_direction,"my")
        print_board(cpu_board)
        print_board(my_board)
