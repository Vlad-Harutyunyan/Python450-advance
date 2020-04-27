import os 
import sys

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'test.ini')

def ini_parser(path:str) -> dict :
    with open (path) as ini :
        lines = [line.strip().replace(' ','') for line in ini if line.strip() != '']
        general = []
        d = dict()   
        cnt = 0

        for x in lines:
            if '[' in x and ']' in x  :
                if x.count('[') == 1 and x.count(']') == 1 and x.index('[') == 0 and x.index(']') == len(x)-1 :
                    d[x[1:-1]] = []
                    lines[cnt] = lines[cnt][1:-1]
                else :
                    print('wrong format')
                    sys.exit(0)
            cnt += 1
        
        for el in range(len(lines)) :
            if lines[el] not in d :
                if '=' in lines[el] :
                    lines[el] = lines[el].split('=')
                else:
                    print('wrong format')
                    sys.exit(0)

                if lines[el][1].isdecimal()  and lines[el][1][0] != '0':
                    lines[el][1] = int(lines[el][1])
    
        for el in lines :
            if isinstance(el,list):
                pass
            else:
                for x in lines :
                    if isinstance(x,list):
                        d[el].append(x)
        return d

        #test
if __name__ == "__main__":
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'test.ini')
    print(ini_parser(initfile))