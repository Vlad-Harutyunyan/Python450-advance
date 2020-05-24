#hist x = dat   e , y = count
#hist x = dat   e , y = count'

print('hello world !!!! (just test)' )

#inheritance

class Polygon:
    def __init__(self,n_of_sides):
        self.n = n_of_sides
        self.sides = list()
    def input_sides (self,sides):
        self.sides = sides
    def disp_sides(self):
        for i in range(self.n):
            print('Side',i+1,'is',self.sides[i])
    def get_perimeter(self):
        return sum(self.sides)

p = Polygon(5)
p.input_sides([1,2,3,4,5])
p.disp_sides()
test = 'male333'
test.upper().replace('MALE','')
print()