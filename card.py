class Card:
    def __init__(self, number):
        self.number = number
        self.is_selected = False

    def __str__(self):
        return str(self.number)

    def toggle(self):
        self.is_selected = not self.is_selected

    def get_color(self):
        if self.number == 55:
            return '#ff0000', '#ffff00'
        if self.number % 11 == 0:
            return '#ab0000', '#f5cbcb'
        if self.number % 10 == 0:
            return '#219401', '#e3fcdc'
        if self.number % 5 == 0:
            return '#003fab', '#b6cffc'
        return '#6700ab', '#ffffff'

    def get_selected_color(self):
        return self.get_color()[0], '#aaaaaa'

