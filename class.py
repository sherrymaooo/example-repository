poly = [2, 0, -3, 1]
degree = len(poly) - 1
print(degree)
print(f"{degree = }")
print(f"degree = {degree}")

class Polynomial(object):
    #call __init__function that initializes coefficient of polynomial
    def __init__(self, coef):
        #attribute
        self.coef = coef

    #define a degree method
    def degree(self):
        self.degree = len(self.coef) - 1
        return degree

#Initialize one instance of polynomial class
#P(x) = 2x^3 - 3x + 1
p = Polynomial([2, 0, -3, 1])
print(p)
#p.coef does not require parenthesis because it is an attribute
print(f"p has coefficient {p.coef}")
#p.degree requires parenthesis becuase it is a method
print(f"p if of degree {p.degree()}")

