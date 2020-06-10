from bs4 import BeautifulSoup as bs
import requests
import json
import os

# a_tags = soup.find_all('a')

class Parser :
    def __init__(self:object) -> None :
        self.res = []
    
    def get_html(self:object,path:str) -> object : 
        r = requests.get(path).text
        soup = bs(r,'html.parser')
        return soup

    def get_a_tags(self:object,path:str) -> list :
        a_tags = self.get_html(path).find_all('a',href=True)
        return a_tags
    
    def filter_a_tags(self:object,path:str) -> list :
        a_tags = self.get_a_tags(path)
        result = []
        for a in a_tags:
            if 'https://' in a['href'] or 'www.' in a['href'] or a['href'][0] == '#':
                pass
            else:
                result.append(a)
        return list(set(result))

    def parse_by_depth(self:object, depth:int, start_path:str ,result=dict(), check = True, new_dict = dict(), limit = 2 ) -> dict :
        dot_cnt = 1 # just for better view 
        filtered_a_tags = []
        
        filtered_a_tags = self.filter_a_tags(start_path)
        page_name = start_path.split('//')[1].split('/')[0]
        page_name = f'https://{page_name}'

        if check == True :
            result['title'] = self.get_html(start_path).find('title').text
            result['links'] = []
        
        
        for a in filtered_a_tags :
            
            new_link = f'{page_name}{a["href"]}'
            new_d = {}
            new_d[a["href"]] = {}
            new_d[a['href']]['title'] = self.get_html(new_link).find('title').text
            new_d[a['href']]['links'] = []

            # print(new_dict)

            if new_dict :
                new_d[a['href']]['links'].append(new_dict)

        
            if depth != 1 : 
                return self.parse_by_depth(depth-1,new_link,result,check=False, new_dict = new_d)

            result['links'].append(new_d)
            
            #Just for better view
            os.system('cls' if os.name == 'nt' else 'clear')
            # print(new_link)
            print(f'Please wait ,  programm working','.'*dot_cnt)
            dot_cnt += 1
            
            if dot_cnt >= 4:
                dot_cnt = 1
           

            limit -= 1
            if limit == 0:
                break  
           
        return result
            
    def to_json(self:object,dct:dict) :
        with open ('data.json','w') as f :
            json.dump(dct,f,indent=3)
        print('All done successfully ! ')

               

if __name__ == "__main__":
    p = Parser()
    # print(p.get_a_tags())
    p.to_json(p.parse_by_depth(3,'https://en.wikipedia.org/wiki/Crew_Dragon_Demo-2'))