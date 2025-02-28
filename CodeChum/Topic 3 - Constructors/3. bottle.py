from beverage import Beverage

class Bottle:
    def __init__(self, mL: int, flavor: str = "Unknown", color: str = "Unknown"):
        self.mL = mL
        self.beverage = Beverage(flavor, color)