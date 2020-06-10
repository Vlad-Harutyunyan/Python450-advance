import pickle

class test :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

v = test(False,1,2)

s = open('ttt.txt','ab')
pickle.dump(v,s)

q = open('ttt.txt','rb')
new_t = pickle.load(q)

print(new_t.a)