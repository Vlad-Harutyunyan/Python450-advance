import os 
import sys

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'test.ini')

def ini_parser(path:str) -> dict :
    with open (path) as ini :
        lines = [line.strip() for line in ini if line.strip() != '']
        d = dict()   
        cnt = 0
        t = []
        for x in lines:
            if '[' in x and ']' in x  :
                if x.count('[') == 1 and x.count(']') == 1 and x.index('[') == 0 and x.index(']') == len(x)-1 :
                    d[x[1:-1]] = []
                    t.append(cnt)
                    lines[cnt] = lines[cnt][1:-1]
                else :
                    print('wrong format')
                    return
            cnt += 1
        for el in range(len(lines)) :
            if lines[el] not in d :
                if '=' in lines[el] :
                    lines[el] = lines[el].split('=')
                    lines[el][0] = lines[el][0].strip()
                    lines[el][1] = lines[el][1].strip()
                else:
                    print('wrong format')
                    return
                if lines[el][1].isdecimal()  and lines[el][1][0] != '0':
                    lines[el][1] = int(lines[el][1])
        t.append(len(lines))
        c = {lines[t[x]]:lines[t[x]+1:t[x+1]] for x in range(len(t)-1) }
        return c
    
if __name__ == "__main__":
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    initfile = os.path.join(thisfolder, 'test.ini')
    print(ini_parser(initfile))