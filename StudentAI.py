from random import randint
from BoardClasses import Move
from BoardClasses import Board
from Checker import Checker
import copy
import math

#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.

# color/player 1 == black
# color/player 2 == white
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
        self.bestMove = None
        self.blackVal = 0 #-------
        self.whiteVal = 0 #-------

    def get_move(self,move):
        if len(move) != 0:
            self.board.make_move(move,self.opponent[self.color])
        else:
            self.color = 1

        moves = self.board.get_all_possible_moves(self.color)
        cloneBoard = copy.deepcopy(self.board)
        self.minimax(cloneBoard, 2, True)
        move = self.bestMove
        self.board.make_move(move,self.color)
        return move
        
        
    def minimax(self, cloneBoard, depth, maximizingPlayer):
        if(depth == 0):
            return self.evaluate(cloneBoard)
            
        if(maximizingPlayer == True):
            maximizerMoves = cloneBoard.get_all_possible_moves(self.color)
            value = -math.inf
            for move in maximizerMoves:
                for x in move:
                    clone = copy.deepcopy(cloneBoard)
                    clone.make_move(x, self.color)
                    score = self.minimax(clone, depth - 1, False)
                    if(score > value):
                        value = score
                        self.bestMove = x
            return value
            
        else:
            minimizerMoves = cloneBoard.get_all_possible_moves(self.opponent[self.color])
            value = math.inf
            for move in minimizerMoves:
                for x in move:
                    clone = copy.deepcopy(cloneBoard)
                    clone.make_move(x, self.opponent[self.color])
                    score = self.minimax(clone, depth - 1, True)
                    if(score < value):
                        value = score
            return value
                
    def evaluate(self, board):
        # for x in range(self.row):
        #     for y in range(self.col):
        #         if (self.board.board[x][y].is_king):
        #             if self.board.board[x][y].color == "B":
        #                 # print("%s king row:%d col:%d" % (self.board.board[x][y].color, x,y))
        #                 self.blackVal += 7
        #             else:
        #                 self.whiteVal += 7

        if(self.color == 1):
            return self.blackVal + 5 * board.black_count - 5 * board.white_count
        else:
            return self.whiteVal + 5 * board.white_count - 5 * board.black_count     












# class StudentAI():

#     def __init__(self,col,row,p):
#         self.col = col
#         self.row = row
#         self.p = p
#         self.board = Board(col,row,p)
#         self.board.initialize_game()
#         self.color = ''
#         self.opponent = {1:2,2:1}
#         self.color = 2
#         self.bestMove = None

#     def get_move(self,move):
#         if len(move) != 0:
#             self.board.make_move(move,self.opponent[self.color])
#         else:
#             self.color = 1
#         moves = self.board.get_all_possible_moves(self.color)
#         cloneBoard = copy.deepcopy(self.board)
#         self.minimax(cloneBoard, 2, True)
#         move = self.bestMove
#         self.board.make_move(move,self.color)
#         return move
    
    
#     def minimax(self, cloneBoard, depth, maximizingPlayer):
#         if(depth == 0):
#             return self.evaluate(cloneBoard)
        
#         if(maximizingPlayer == True):
#             maximizerMoves = cloneBoard.get_all_possible_moves(self.color)
#             value = -math.inf
#             for move in maximizerMoves:
#                 for x in move:
#                     clone = copy.deepcopy(cloneBoard)
#                     clone.make_move(x, self.color)
#                     score = self.minimax(clone, depth - 1, False)
#                     if(score > value):
#                         value = score
#                         self.bestMove = x
#             return value
        
#         else:
#             minimizerMoves = cloneBoard.get_all_possible_moves(self.opponent[self.color])
#             value = math.inf
#             for move in minimizerMoves:
#                 for x in move:
#                     clone = copy.deepcopy(cloneBoard)
#                     clone.make_move(x, self.opponent[self.color])
#                     score = self.minimax(clone, depth - 1, True)
#                     if(score < value):
#                         value = score
#             return value
            
#     def evaluate(self, board):
#         if(self.color == 1):
#             return board.black_count - board.white_count
        
#         else:
#             return board.white_count - board.black_count