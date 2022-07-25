#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 11:27:30 2021

@author: kishanpatel
"""

import numpy as np
import random
import time

print("Instructions: Pick your spot using an integer from 1-n^2. Ex. the first spot in the second row is n+1. You are 'x', cpu is 'o'.")
time.sleep(5)
n = 5 #dimensions of board
board = np.zeros((n,n))

def play_user_hand(board, n):
    try:
        spot = input("mark your spot: ")
        spot = int(spot) #convert input string to integer
        if 1 <= spot <= n**2:
            row = (spot - 1)//n
            col = (spot - 1) % n
            if board[row][col] != 0:
                print("Invalid input. Pick a spot that's not already marked.")
                board = play_user_hand(board, n)
            else:
                board[row][col] = 1
                print("user move:", spot)
                print()
        else:
            raise ValueError #will send to except case
    except ValueError:
        print("Invalid input. Make sure you enter an integer from 1-n^2")
        board = play_user_hand(board, n)
    return board

def play_cpu_hand(board):
    rows_poss, cols_poss = np.where(board==0) #rows and cols array of unmarked spots
    if rows_poss.size != 0: #ensure there are unmarked spots remaining
        print("cpu is making a move...")
        time.sleep(1.2)
        rand_ind = random.randint(0, len(rows_poss) - 1) #random index in array of unmarked spots
        cpu_row, cpu_col = rows_poss[rand_ind], cols_poss[rand_ind]
        board[cpu_row][cpu_col] = -1 #record cpu move on board
        cpu_spot = (n * cpu_row) + cpu_col + 1
        print("cpu move:", cpu_spot)
        time.sleep(1.2)
    return board

def win_game(board, mark):
    win = False
    row_wins, col_wins = np.all(board==mark, axis=1), np.all(board==mark, axis=0)
    if np.any(row_wins) or np.any(col_wins):
        win = True
    diag1, diag2 = board.diagonal(), np.fliplr(board).diagonal()
    if np.all(diag1==mark) or np.all(diag2==mark):
        win = True
    return win

def tie_game(board):
    tie = False
    if np.all(board != 0): #no remaining unmarked spots
        tie = True
    return tie

def play_hand(board, n):
    end_game = False
    board = play_user_hand(board, n)
    time.sleep(1.2)
    if win_game(board, 1):
        print("you win! congrats!")
        end_game = True
        return board, end_game
    
    board = play_cpu_hand(board)
    print()
    if win_game(board, -1):
        print("you lost! try again next time!")
        end_game = True
    elif tie_game(board):
        print("you tied! at least you tried!")
        end_game = True
    return board, end_game

def display_board(board):
    disp = np.where(board==1, 'x', board)
    disp = np.where(board==-1, 'o', disp)
    disp = np.where(board==0, '-', disp)
    return disp

def play_game(board, n):
    end_game = False
    while not end_game:
        board, end_game = play_hand(board, n)
        disp = display_board(board)
        print(disp)
    return board

play_game(board, n)






