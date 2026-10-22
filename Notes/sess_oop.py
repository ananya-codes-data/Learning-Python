# Class and Object
# creating a banking program to understand class, object, constructor, methods and functions

# banking program
class Atm:  # class name (pascal case: MyWorld)

    __counter = 1

    # constructor (special function) (when object is created constructor is executed on it own)
    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.__counter
        Atm.__counter = Atm.__counter + 1
        # self.menu()     # function calling
    
    # utility functions
    @staticmethod
    def get_counter():
        return Atm.__counter

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print('Change the type of the value')

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)

        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw()
        else:
            exit()

    def create_pin(self):       # function for pin generation
        user_pin = input('enter your pin:')
        self.pin = user_pin

        user_balance = int(input('enter balance:'))
        self.__balance = user_balance

        print('PIN CREATED SUCCESSFULLY')
        self.menu()

    def change_pin(self):       # function for changing pin
        old_pin = input('enter old pin:')

        if old_pin == self.pin:
            # let the person change the pin
            new_pin = input('enter new pin:')
            self.pin = new_pin
            print('PIN CHANGE SUCCESSFUL')
            self.menu()
        else:
            print("can't change the pin")
            self.menu()

    def check_balance(self):        # function for checking balance
        user_pin = input('enter your pin:')
        if user_pin == self.pin:
            print('your balance is', self.__balance)
            self.menu()
        else:
            print("can't show the balance")
            self.menu()

    def withdraw(self):         # function for withdrawing money
        user_pin = input('enter your pin:')
        if user_pin == self.pin:
            # ask for withdrawal amount and also show the balance left
            withdrawal_amount = int(input('enter the withdrawal amount:'))
            if withdrawal_amount <= self.__balance:
                self.__balance = self.__balance - withdrawal_amount
                print(withdrawal_amount, 'withdrawn successful')
                print('balance left in the account:', self.__balance)
            else:
                print('not enough balance')
        else:
            print("can't withdraw money")
        self.menu()

obj = Atm()     # objectname = classname()

c1 = Atm()

c2 = Atm()

c3 = Atm()

# print(c1.cid)     # 2

print(Atm.get_counter())    # 5

# constructor is executed as we create the object of the class

print(type(obj))    # <class '__main__.Atm'>

obj.pin   # object can access the things that are present in class

# creating our own data type

class Fraction:

    # parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):      # when we put object inside print function this method would be executed
        return '{}/{}'.format(self.num, self.den)

    def __add__(self, other):       # addition
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den*other.den

        return '{}/{}'.format(new_num, new_den)

    def __sub__(self, other):       # subtraction
        new_num = self.num*other.den - self.den*other.num
        new_den = self.den*other.den
    
        return '{}/{}'.format(new_num, new_den)

    def __mul__(self, other):       # multiplication
        new_num = self.num*other.num
        new_den = self.den*other.den
        
        return '{}/{}'.format(new_num, new_den)

    def __truediv__(self, other):       # division
        new_num = self.num*other.den
        new_den = self.den*other.num
        
        return '{}/{}'.format(new_num, new_den)

    def convert_to_decimal(self):       # covert fraction to decimal
        return self.num/self.den

fr1 = Fraction(3,4)
print(fr1)  # 3/4

fr2 = Fraction(1,2)
print(fr2)  # 1/2

print(fr1 + fr2)    # 10/8

print(fr1 - fr2)    # 2/8

print(fr1 * fr2)    # 3/8

print(fr1 / fr2)    # 6/4

print(fr1.convert_to_decimal())     # 0.75


# Write OOP classes to handle the following scenarios:

# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return '<{},{}>'.format(self.x_cod, self.y_cod)

    def euclidean_distance(self, other):
        return ((other.x_cod - self.x_cod)**2 + (other.y_cod - self.y_cod)**2)**0.5

    def distance_from_origin(self):
        # return (self.x_cod**2 + self.y_cod**2)**0.5
        return self.euclidean_distance(Point(0,0))

class Line:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A, self.B, self.C)

    def point_on_line(line, point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return "lies on the line"
        else:
            return "does not lie on the line"

    def shortest_distance(line, point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/ (line.A**2 + line.B**2)**0.5

    def intersection_points(self, other):
        det =  self.A*other.B - other.A*self.B 
        if det != 0:
            x = (self.B*other.C - other.B*self.C) / det
            y = (other.A*self.C - self.A*other.C) / det
            return f"lines are intersecting at {Point(x,y)}"
        else:
            return "lines are parallel"

p1 = Point(10,10)
print(p1)       # <10,10>

p2 = Point(1,1)
print(p2)       # <1,1>

print(p1.euclidean_distance(p2))    # 12.727922061357855

print(p1.distance_from_origin())    # 14.142135623730951

l1 = Line(3, 4, 5)
print(l1)       # 3x + 4y + 5 = 0

l2 = Line(1, 1, -2)
print(l2)

print(l2.point_on_line(p2))       # lies on the line

print(l2.shortest_distance(p2))     # 0.0

print(l1.intersection_points(l2))       # lines are intersecting at <13.0,-11.0>

# collection of objects

class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('ananya','female')
p2 = Person('shan','male')
p3 = Person('situ','male')

L = [p1,p2,p3]

print(L)        # the addresses of all the 3 objects since we don't have __str__ method in our class

for i in L:
  print(i)      # the addresses of all the 3 objects


for i in L:
  print(i.name, i.gender)
# output    
# ananya female
# shan male
# situ male


d = {'p1':p1, 'p2':p2, 'p3':p3}

for i in d:
  print(i)
# output
# p1
# p2
# p3

for i in d:
  print(d[i])       # # the addresses of all the 3 objects


for i in d:
  print(d[i].name)
# output
# ananya
# shan
# situ

for i in d:
  print(d[i].gender)
# output
# female
# male
# male


