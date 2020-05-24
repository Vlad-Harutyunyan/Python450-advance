import re
############################
#######   PROBLEM1 ########
###########################

#for roman number validation 
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'

class Circle:
    def __init__(self:object,radius:int,color:str) -> None:
        self.radius = radius
        self.color = color
        assert isinstance(self.radius,(int,float)) or self.radius <= 0 , '[Error] radius can be only integer of float number '
        assert isinstance(self.color,str) , '[Error] color can be only string !'
        self.PI = 3.14
     
    def get_radius(self:object) -> int:
        return self.radius

    def get_color(self:object) -> str:
        return self.color

    def calc_area(self:object) -> float:
        return self.PI * self.radius * self.radius

    def calc_circumference(self:object) -> float:
        return 2 * self.PI * self.radius

    def __str__(self:object) -> str:
        return f'{self.get_radius()} circle withradius {self.get_color()}'


############################
#######   PROBLEM2 ########
###########################

class RomanNumber:
    def __init__(self,roman_number:str) -> None:
        self.__r_n = roman_number

        #validate roman number 
        assert bool(re.match(thousand + hundred+ten+digit +'$', self.__r_n) ) , '[Error] wrong roman number '

    def get_num(self:object) -> str:
        return self.__r_n
    
    def set_num(self:object,num1:str) -> None:
        self.__r_n = num1

    def convert(self:object) -> int :

        num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for key,value in enumerate(self.__r_n) :
            if (key+1) == len(self.__r_n) or num_dict[value] >= num_dict[self.__r_n[key+1]]:
                result += num_dict[value]
            else:
                result -= num_dict[value]
        return result

        
    def convert_to_roman(self:object, num:int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def __add__(self:object,roman_num2:object) -> int:
        return RomanNumber(self.convert_to_roman(self.convert() + roman_num2.convert()))

    def __mul__ (self:object,roman_num2:object) -> int:
        return RomanNumber(self.convert_to_roman(self.convert() * roman_num2.convert()))

    def __sub__ (self:object,roman_num2:object) -> int:
        return RomanNumber(self.convert_to_roman(self.convert() - roman_num2.convert()))

    def __truediv__ (self:object,roman_num2:object) -> int:
        return RomanNumber(self.convert_to_roman(self.convert() // roman_num2.convert()))


############################
#######   PROBLEM3 ########
###########################


class Person:
    def __init__(self:object,name:str,last_name:str,age:int,gender:str,password:str) -> None:
        self.name = name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.student = False
        self.__password = password

        #validate name
        assert isinstance(self.name,str) , '[Error] Name can be only string'
        #validate surname
        assert isinstance(self.last_name,str) , '[Error] Last name can be only string'
        #validate age
        assert isinstance(self.age,int) or self.age < 0 , '[Error] Wrong age !'
        #validate gender
      
        self.gender = self.gender.upper()
        assert isinstance(self.gender,str) and len(self.gender.replace('MALE','') ) == 0 or  isinstance(self.gender,str) and len(self.gender.replace('FEAMLE','')) == 0  , '[Error] Wrong gender'
        self.gender = self.gender.lower()
      
        #validate password
        assert isinstance(self.__password,str) or len(self.__password) < 6 , '[Error] Weak or wrong password :( '


    def get_name (self:object) -> str:
        return self.name

    def get_last_name(self:object) -> str:
        return self.last_name

    def get_age(self:object) -> int :
        return self.age

    def get_status(self:object) -> bool :
        return self.student

    def Greeting(self:object,second_person:object) -> str:
        text = f'Welcom dear {second_person.get_name()}'
        print(text)

    def Goodbye(self:object) -> str:
        text = 'Bye everyone'
        print(text)

    def Favorite_num(self:object,num1:int) -> str:
        text = f'My favorite number is {num1}'
        return text
    
    def set_status(self:object,is_student:bool):
        self.student = is_student


    def Read_file(self:object, filename:str) :
        try :
            open(f'{filename}.txt')
            print('[Success] File is opened !')
        except FileNotFoundError:
            print('[Error] File not Found  Sorry ')
        

############################
#######   PROBLEM4 ########
###########################


class Polygon:
    def __init__(self:object, n_of_sides:int) -> None:
        self.n = n_of_sides
        assert isinstance(self.n,int) ,' Number of Sides can be only integer '
        self.sides = list()

    def input_sides(self:object, sides:list) -> None:
        self.sides = sides
        assert len(self.sides) == self.n , 'Wrong sides'
    
    def disp_sides(self:object):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def perimeter(self:object) -> int:
        return sum(self.sides)

class Quadrilateral(Polygon):
    def __init__(self:object) -> None:
        super().__init__(4)

class Rectangle(Quadrilateral) :
    def __init__(self:object, length:int,width:int) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def area(self:object) -> int :
        return self.length * self.width

    def perimeter(self:object) -> int:
        return 2 * self.length + 2 * self.width

    def input_sides(self):
        pass

class Square(Rectangle):
    def __init__(self:object,length:int) -> None:
        super().__init__(length, length)


#TESTING
if __name__ == "__main__":
    c = Circle(20,'red')
    print(c)
    print(c.calc_area())
    print(c.calc_circumference())
    # r = RomanNumber('IIX') #Raise error (wrong roman number )
    # print(r.convert())
    r1 = RomanNumber('X')
    r2 = RomanNumber('X')
    result = r1+r2

    print(result.convert())
    # p = Person('Vlad','Harutyunyan',20,'male3','password00') #rause error becouse gender wrong 
    p = Person('Vlad','Harutyunyan',20,'male','password00')
    p.Read_file('file') #raise error
    # p.Read_file('test')  
    
    # poli = Polygon('4') raise error
    poli = Polygon(4)
    # poli.input_sides([1,2,3,4,5])  raise error
    poli.input_sides([1,2,3,4])
