#In this we will learn how to create our own datatype

class Fraction:

    def __init__(self, num, denum) :
        self.num = num
        self.denum = denum

    def __str__(self) :
        return f"{self.num}/{self.denum}"
    
    def __add__(self,other):
        temp_num = self.num * other.denum + self.denum * other.num
        temp_denum = self.denum * other.denum
        return "{}/{}".format(temp_num,temp_denum)
    
    def __sub__(self,other):
        temp_num = self.num * other.denum - self.denum * other.num
        temp_denum = self.denum * other.denum
        return "{}/{}".format(temp_num,temp_denum)
    
    def __mul__(self,other):
        temp_num = self.num * other.num
        temp_denum = self.denum * other.denum
        return "{}/{}".format(temp_num,temp_denum)
    
    def __truediv__(self,other):
        temp_num = self.num * other.denum 
        temp_denum = self.denum * other.num
        return "{}/{}".format(temp_num,temp_denum)
    
x = Fraction(4,5)
y = Fraction(7,9)
print(x)
print(y)
print("Addition:",x + y)
print("Subtraction:",x - y)
print("Multiplication:",x * y)
print("Division:",x / y)