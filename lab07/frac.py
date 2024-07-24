class Frac():

    def __init__(self, numer, denom):
        self.numer = numer / Frac.gcd(numer,denom)
        self.denom = denom / Frac.gcd(numer,denom)

    def __str__(self):
        return str(int(self.numer)) + "/" + str(int(self.denom))

    def add(self, frac): 
        result = Frac(self.numer*frac.denom + frac.numer*self.denom, self.denom*frac.denom + frac.denom*self.denom)
        gcd = Frac.gcd(result.numer, result.numer)
        result = Frac(result.numer/gcd, result.denom/gcd)
        return result

    def sub(self, frac):
        return Frac(self.numer - frac.numer, self.denom - frac.denom)
    
    def mul(self, frac):
        return Frac(self.numer * frac.numer, self.denom * frac.denom)
    
    def div(self, frac):
        return Frac(self.numer / frac.numer, self.denom / frac.denom)

    def gcd(a, b):
        while b != 0:
            t = b
            b = a % b
            a = t
        return abs(a)

#-----------------------

# uppg 4

# testar add
x = Frac(1, 6)
y = Frac(1, 6)
z = x.add(y)
print(f"{x} + {y} = {z}") # Skriver ut 1/6 + 1/6 = 1/3

# testar sub
x = Frac(2, 3)
y = Frac(1, 6)
z = x.sub(y)
print(f"{x} - {y} = {z}") # Skriver ut 2/3 - 1/6 = 1/2

# testar mul
x = Frac(2, 5)
y = Frac(3, 4)
z = x.mul(y)
print(f"{x} * {y} = {z}") # Skriver ut 2/5 * 3/4 = 3/10

# testar div
x = Frac(3, 7)
y = Frac(5, 2)
z = x.div(y)
print(f"{x} / {y} = {z}") # Skriver ut 3/7 / 5/2 = 6/35
