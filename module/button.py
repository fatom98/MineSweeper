class Button:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value
        self.pressed = False

    def press(self):
        self.pressed = True

    def un_press(self):
        self.pressed = False

    def __str__(self):
        return f"ROW: {self.row}, COL: {self.col}, Pressed: {self.pressed}"
