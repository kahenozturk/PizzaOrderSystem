class Pizza:
    def __init__(self):
        self.description = "Unknown"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost
    
class Classic(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Classic Pizza"
        self.cost = 8.99
        
class Margherita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margherita Pizza"
        self.cost = 9.99

class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Turk Pizza"
        self.cost = 11.99

class PlainPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Plain Pizza"
        self.cost = 7.99