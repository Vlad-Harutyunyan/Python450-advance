import json
import os

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'test.json')

 
def json_to_xml(path:str,root = None) -> dict :
    r = None
    if root == None:
        root = 'root'
    with open (path,'r') as f:
        r = json.loads(f.read())
    buffs = ['<?xml version="1.0" encoding="UTF-8" standalone="no" ?>']
    for x in r:
        buffs.append(f'\t <{root}>')
        
        for k in x:
            buffs.append(f' \t\t <{k}>{x[k]}</{k}> ')

        buffs.append(f'\t </{root}>')
    return '\n'.join(buffs)   


if __name__ == "__main__":
    print(json_to_xml(initfile))