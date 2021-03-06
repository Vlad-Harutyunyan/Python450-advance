import json
import os
import xml.etree.ElementTree as ET

######################
###P R O b L E M 1 ###
######################

pr1_Dict = {
    2:{
        'name':'Vlad',
        'surname':'Harutyunyan',
        'age':20,
        'company':'VMware'
    },
    3:{
        'name':'Vlad',
        'surname':'Poghosyan',
        'age':30,
        'company':'VXSoft'
    },
    1:{
        'name':'Nairi',
        'surname':'Hakobyan',
        'age':30,
        'company':'Ucom'
    }
}

def problem1_convertor(dct:dict) -> str :
    return (json.dumps(dct, sort_keys=True, indent = 4))


######################
###P R O b L E M 2 ###
######################
samplejson = """  {
    "company":{
        "employee":{
            "name":"Emma",
            "payble":{
                "salary":7000,
                "bonus":800
            }
        }
    }
    
}
"""

#Fixed
def pr2(srch):
    res = json.loads(srch)
    if 'salary' in res['company']['employee']['payble'] :
        return res['company']['employee']['payble']['salary']
    else:
        return 'Sorry , this field doesnt exist '
     


class Vehicle:
    def __init__ (self:object,name:str,engine:str,price:int,fuel_per_100km:int) -> None:
        self.name = name
        self.engine = engine 
        self.price = price
        self.fuel_per_100km = fuel_per_100km
    
    def fuel_cost_calc(self:object,distance:int) -> float:
        return distance * (self.fuel_per_100km/100)


def to_obj(obj:object) -> object:
    if '__type__' in obj and obj['__type__'] == 'Vehicle':
        return Vehicle(obj['name'], obj['engine'],obj['price'],obj['fuel_per_100km'])
    return obj


def pr5_parser(path:str) -> None:
    tree = ET.parse(path)
    root = tree.getroot()
    print(root.tag)
    for child in root:
        print(child.tag,child.attrib)


def pr6_parser(path:str) -> None:
    tree = ET.parse(path)
    root = tree.getroot()
    movies = root.findall('./genre/decade/movie')
    for m in movies :
        print(m.attrib['title'])
    
def pr7_parser(path:str) -> None :
    tree = ET.parse(path)
    root = tree.getroot()
    movies = root.findall('.//movie/[year="1992"]')
    for m in movies:
        name = m.attrib['title']
        print(f'in 1992 out this film ` {name}')

def pr8_parser(path:str) -> None :
    tree = ET.parse(path)
    root = tree.getroot()
    movies = root.findall('.//movie/format[@multiple="Yes"]/..')
    print('in multiple formats available')
    for m in movies:
        print(m.attrib['title'])
    

def pr9_parser(path:str) -> None :
    tree = ET.parse(path)
    root = tree.getroot()
    movie = root.findall('.//movie[@title="Back to the Future"]')
    try:
        movie[0].attrib['title'] = 'Back to the Future'
    except:
        pass
    tree.write(path)
    print('Done')

def pr10_parser(path:str) -> None :
    tree = ET.parse(path)
    root = tree.getroot()
    movies = root.findall('.//movie/format[@multiple="Yes"]')
    for m in movies:
        if len(m.text.split(','))  <  2 : 
            m.attrib['multiple'] = 'No'
    tree.write(path)
    print('Done')

def pr11_parser(path:str) -> None :
    check = False
    tree = ET.parse(path)
    root = tree.getroot()
    dec_list = []
    d =  root.findall('./decade')

    for decade in d:

        dec_list.append(decade)
        movies = decade.findall("movie")
        
        for m in movies:
            y = m.find('year')
            if int(y.text) > int(decade.attrib['years'][:-1])+9 or int(y.text) < int(decade.attrib['years'][:-1]):
                decade.remove(m)
                for x in dec_list:
                    if int(y.text) < int(x.attrib['years'][:-1])+9 or int(y.text) > int(x.attrib['years'][:-1]):
                        x.append(m)
                        break
    tree.write(path.split('xml')[0][:-1]+'new.xml')
    print('Done')

if __name__ == "__main__":
   #Problem 1
    print('------------------PROBLEM1------------------------')

    print(problem1_convertor(pr1_Dict))

   #Problem 2
    print('------------------PROBLEM2------------------------')

    print(pr2(samplejson))

    #Problem 3
    print('------------------PROBLEM3------------------------')

    vehicle = Vehicle("Toyota Rav4", "2.5L", 32000,13)
    test3 = json.dumps(vehicle.__dict__)
    print(test3)

    #Problem 4 // another way 
    print('------------------PROBLEM4------------------------')

    test4 = json.loads('{"__type__": "Vehicle", "name":"Toyota Rav4", "engine":"2.5L", "price":32000,"fuel_per_100km":13}' ,object_hook=to_obj)
    print(f' Data loads from json ` name - {test4.name} , engine - {test4.engine} ,price - {test4.price} ')
    print(f'for 500 km we need to spend {test4.fuel_cost_calc(500)}L , petrol ')

    #get file full path
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'movies.xml')
    #Problem 5
    print('------------------PROBLEM5------------------------')

    pr5_parser(initfile)
    #Problem 6
    print('------------------PROBLEM6------------------------')

    pr6_parser(initfile)   
    #Problem 7
    print('------------------PROBLEM7------------------------')
    pr7_parser(initfile)   

    #Problem 8
    print('------------------PROBLEM8------------------------')
    pr8_parser(initfile)  

    #Problem 9
    print('------------------PROBLEM9------------------------')
    pr9_parser(initfile)  

    #Problem 10
    print('------------------PROBLEM10------------------------')
    pr10_parser(initfile)  

      #Problem 11
    print('------------------PROBLEM11------------------------')
    pr11_parser(initfile)  
