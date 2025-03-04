from random import randint
from Buttons import Buttons

class Difficulty:
    def __init__(self):
        self.difficulty = ""
        self.difficulty_list = ["Easy", "Medium", "Hard", "Random"]
        self.easy_button = None
        self.medium_button = None
        self.hard_button = None
        self.random_button = None
        self.difficulty_map = {
            "Easy": (10,5),
            "Medium": (20,7),
            "Hard": (30,10),
            "Random": (randint(10, 30), randint(5, 10))
        }

    def difficulti(self, screen):
        self.easy_button = Buttons(text=self.difficulty_list[0], screen=screen, x_pos=430, y_pos=200, aliases=False, text_shadow=True, borders=True, line_thickness=5, border_color="red", size_x=200)
        self.easy_button.draw()
        self.medium_button = Buttons(text=self.difficulty_list[1], screen=screen, x_pos=430, y_pos=300, aliases=False, text_shadow=True, borders=True, line_thickness=5, border_color="red", size_x=200)
        self.medium_button.draw()
        self.hard_button = Buttons(text=self.difficulty_list[2], screen=screen, x_pos=430, y_pos=400, aliases=False, text_shadow=True, borders=True, line_thickness=5, border_color="red", size_x=200)
        self.hard_button.draw()
        self.random_button = Buttons(text=self.difficulty_list[3], screen=screen, x_pos=430, y_pos=500, aliases=False, text_shadow=True, borders=True, line_thickness=5, border_color="red", size_x=200)
        self.random_button.draw()
        if self.easy_button.check_click():
            self.difficulty = self.difficulty_list[0]
        if self.medium_button.check_click():
            self.difficulty = self.difficulty_list[1]
        if self.hard_button.check_click():
            self.difficulty = self.difficulty_list[2]
        elif self.random_button.check_click():
            self.difficulty = self.difficulty_list[3]
        else:
            pass


