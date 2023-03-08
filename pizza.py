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

class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + ", " + self.description
    
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Olives sauce"
        self.cost = 1.50
        
    def get_name(self):
        return self.description

class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushrooms sauce"
        self.cost = 1.00
        
    def get_name(self):
        return self.description
    
class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Goat Cheese sauce" 
        self.cost = 2.00
        
    def get_name(self):
        return self.description

class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat sauce"
        self.cost = 2.50
        
    def get_name(self):
        return self.description

class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onions sauce"
        self.cost = 1.00
        
    def get_name(self):
        return self.description

class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn sauce"
        self.cost = 1.50
        
    def get_name(self):
        return self.description

class Plain(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "no sauce"
        self.cost = 0.0
        
    def get_name(self):
        return self.description