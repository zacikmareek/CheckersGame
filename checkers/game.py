import pygame
from .constants imprt RED, WHITE

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = RED

