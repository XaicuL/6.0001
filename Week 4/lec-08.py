#################
## EXAMPLE: simple Coordinate class
#################


class Coordinate(object): #object is the parent class
    """ A coordinate made up of an x and y value """
    def __init__(self, x, y): #__init__ is the constructor method // #self is a reference to the object itself
        """ Sets the x and y values """
        self.x = x #self.x is an attribute of the object
        self.y = y #self.y is an attribute of the object
    def __str__(self):
        """ Returns a string representation of self """
        return "<" + str(self.x) + "," + str(self.y) + ">"
    def distance(self, other):
        """ Returns the euclidean distance between two points """
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5


c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c.x, origin.x)
print(c.distance(origin))
print(Coordinate.distance(c, origin))
print(origin.distance(c))
print(c)


#################
## EXAMPLE: simple class to represent fractions
## Try adding more built-in operations like multiply, divide
### Try adding a reduce method to reduce the fraction (use gcd)
#################
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom): #parameter is num and denom
        """ num and denom are integers """
        assert type(num) == int and type(denom) == int, "ints not used" #assert is a statement that must be true
        self.num = num #assign num to self.num
        self.denom = denom #assign denom to self.denom
    def __str__(self): #~exist parameter
        """ Retunrs a string representation of self """
        return str(self.num) + "/" + str(self.denom)
    def __add__(self, other): #parameter is other
        """ Returns a new fraction representing the addition """
        top = self.num*other.denom + self.denom*other.num #def new value to top
        bott = self.denom*other.denom  #def new value to bott
        return Fraction(top, bott) #return new fraction // top and bott are parameters
    def __sub__(self, other): #parameter is other
        """ Returns a new fraction representing the subtraction """
        top = self.num*other.denom - self.denom*other.num #def new value to top // local value
        bott = self.denom*other.denom  #def new value to bott // local value
        return Fraction(top, bott) #return new fraction // top and bott are parameters
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom #return float value of fraction
    def inverse(self):
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c) #16/16
print(float(c)) #1.0
print(Fraction.__float__(c)) #1.0
print(float(b.inverse())) #1.3.(infiniteDecimal)

#c = Fraction(3.14, 2.7) # assertion error
#print a*b # error, did not define how to multiply two Fraction objects


##############
## EXAMPLE: a set of integers as class
##############
class intSet(object):
    """
    An intSet is a set of integers
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once
    """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = [] #vals type is list, and emptySet

    def insert(self, e): #parameter is e
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals: #if e is not in self.vals
            self.vals.append(e) #add new element e to vals

    def member(self, e): #parameter is e
        """ Assumes e is an integer
        Returns True if e is in self, and False otherwise """
        return e in self.vals

    def remove(self, e): #parameter is e
        """ Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self """
        try: # --- Call A
            self.vals.remove(e) #--- Call a
        except: # --- Call B
            raise ValueError(str(e) + ' not found') #Call b

#Step i)
#=> A
#Step ii)
#=> case 1) EXCEPTION_OCCURRED
#           : Jump B
#=> case 2) NO_EXCEPTION_OCCURRED
#           : execution end
#Step iii)
#=> case 1) MATCH WITH B
#           : b Run
#
#=> case 2) ~MATCH WITH B
#           : error


    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


s = intSet()
print(s)
#s is an instance of intSet (intSet is class)

s.insert(3)
s.insert(4)
s.insert(3)
s.insert(6)
print(s)
# s is an instance of insert (insert is class)

s.member(3)
s.member(5)
print(s)
# s is an instance of member (insert is member)

#s.remove(3)  # leads to an error
print(s)
s.remove(3)