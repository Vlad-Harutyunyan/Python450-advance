import random 
##############################
#########PROBLEM1##########
#############################

class RomanNumber:
    def __init__(self,roman_number:str):
        self.__r_n = roman_number
    
    def get_num(self:object) -> str:
        return self.__r_n
    
    def set_num(self:object,num1:str):
        self.__r_n = num1

    def convert(self:object) -> int :
        num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for key,value in enumerate(self.__r_n):
            if (key+1) == len(self.__r_n) or num_dict[value] >= num_dict[self.__r_n[key+1]]:
                result += num_dict[value]
            else:
                result -= num_dict[value]
        return result

    def __add__(self:object,roman_num2:object) -> int:
        return self.convert() + roman_num2.convert()


    def __mul__ (self:object,roman_num2:object) -> int:
        return self.convert() * roman_num2.convert()


    def __sub__ (self:object,roman_num2:object) -> int:
        return self.convert() - roman_num2.convert()


    def __truediv__ (self:object,roman_num2:object) -> int:
        return self.convert() // roman_num2.convert()


class Person:
    def __init__(self:object,name:str,last_name:str,age:int,gender:bool,password:str):
        self.name = name
        self.last_name = last_name
        self.age = age 
        self.gender = gender
        self.student = False
        self.__password = password


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

    

class Polygon:
    def __init__(self, n_of_sides):
        self.n = n_of_sides
        self.sides = list()

    def input_sides(self, sides):
        self.sides = sides

    def disp_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def perimeter(self):
        return sum(self.sides)

class Quadrilateral(Polygon):
    def __init__(self):
        super().__init__(4)

class Rectangle(Quadrilateral) :
    def __init__(self , length:int,width:int):
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
    def __init__(self,length):
        super().__init__(length, length)


        


    #####TESTING#####    
if __name__ == "__main__" :

    print(
    """
    ##########################
    #####Problem 1 testes #######
    ##########################
    """
    )

    num1 = RomanNumber('XIII')
    num2 = RomanNumber('XIII')
    num3 = RomanNumber('XXIII')


    res1 = num1 + num2
    print('----Add------')
    print(res1)
    
    print('----Mult------')
    res2 = num2 * num1
    print(res2)

    print('----Sub------')
    res3 = num2 - num3
    print(res3)

    print('----Div------')
    res4 = num2 / num3
    print(res4)

    print(
    """
    ##########################
    #####Problem 2 testes #######
    ##########################
    """
    )
    p1 = Person('Vlad','Harutyunyan',20,'male','#13s^5#pass')
    p2 = Person('Nairi','Hakobyan',30,'male','#13s^5#pa231ss')
    p3 = Person('Vlad','Poghosyan',29,'male','$$#13s^5#p901ass')
    p4 = Person('Ruzanna','Ordyan',18,'female','im_young$$@@#$pass')

    #set function
    p1.set_status(True)
    p2.set_status(False)
    p3.set_status(False)
    p4.set_status(True)

    person_list = []
    person_list.append(p1)
    person_list.append(p2)
    person_list.append(p3)
    person_list.append(p4)

    #getter functions 
    
    for person in person_list:
        print(f' first person name - {person.get_name()} , surname - {person.get_last_name()} , i`m {person.get_age()} years old , student status {person.get_status()}' )
        person.Greeting(person_list[3])
        print(person.Favorite_num(random.randint(1,999)))
        person.Goodbye()

    print(
    """
    ##########################
    #####Problem 3 testes #######
    ##########################
    """
    )

    #Square
    print('Square')
    sqr = Square(10)
    print(f'area - {sqr.area()}')
    print(f'peremeter - {sqr.perimeter()}')
    print()
    #Rectangle
    print('Rectangle')
    rec = Rectangle(10,20)
    print(f'area - {rec.area()}')
    print(f'peremeter - {rec.perimeter()}')










