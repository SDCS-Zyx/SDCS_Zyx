# -*- coding:UTF-8 -*-

from computer import *

def init_board() :
    #None is 0, player is 1, computer is 2
    return [[0] * 15 for i in range(15)]

def get_valid_move(board) :
    ret = []
    for i in range(15) :
        for j in range(15) :
            if board[i][j] == 0 :
                ret.append((i,j))
    return ret
    
def five(board) :
    #左上，上，右上，左，右，左下，下，右下
    way = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(15) :
        for j in range(15) :
            if board[i][j] != 0 :
                get = board[i][j]
                
                for w in way :
                    now = (i, j)
                    count = 1
                    
                    while True :
                        if (now[0] + w[0] not in range(15)) or (now[1] + w[1] not in range(15)) :
                            break
                        
                        now = (now[0] + w[0], now[1] + w[1])
                            
                        if board[now[0]][now[1]] != get :
                            break
                        else :
                            count += 1
                            
                            if count == 5 :
                                return get
    return False
    
def get_turn() :
    num = input("请决定先手，输入0玩家先手，输入1电脑先手")
    return 'computer' if int(num) else 'player'
    
def update(board, pos, turn) :
    board[pos[0]][pos[1]] = 1 if turn == 'player' else 2
    return board
    
def get_player_pos(board) :
    while True :
        pos = input("输入下棋位置").split()
        pos = (int(pos[0]), int(pos[1]))
        
        if pos[0] not in range(15) or pos[1] not in range(15) :
            print("输入非法\n")
            continue
        elif board[pos[0]][pos[1]] :
            print("位置非法\n")
            continue
        else :
            return pos
            
def valid_input(pos, board) :
    if pos[0] not in range(15) or pos[1] not in range(15) :
        return False
    if board[pos[0]][pos[1]] != 0 :
        return False
    return True

def get_computer_pos(board) :
    return get_pos(board)
    
def show_board(board) :
    #●○
    print("--------------------------------------------------------")
    
    print('   ', end = '')
    for i in range(15) :
        if i < 10 :
            print('', i, end = '')
        else :
            print(i, end = '')
    print()
    
    for i in range(15) :
		
        if i < 10 :
            print(i, ' ', end = '')
        else :
            print(i, '', end = '')
            
        for j in range(15) :
            if board[i][j] == 1 :
                print('○', end = '')
            elif board[i][j] == 2 :
                print('●', end = '')
            else :
                print('  ', end = '')
        print()
    print("--------------------------------------------------------")
    print()
    
def show_result(num) :
    if num == 1 :
        print("玩家胜")
    else :
        print("电脑胜")

def main() :
    
    board = init_board()
    turn = get_turn()
    
    while True :
        
        show_board(board)
        
        if turn == 'player' :
            pos = get_player_pos(board)
            board = update(board, pos, turn)
            turn = 'computer'
        else :
            pos = get_computer_pos(board)
            board = update(board, pos, turn)
            turn = 'player'
            
        res = five(board)
            
        if not res :
            if get_valid_move(board) :
                continue
            else :
                show_board(board)
                print("和棋")
                break
        else :
            show_board(board)
            show_result(res)
            break

main()

