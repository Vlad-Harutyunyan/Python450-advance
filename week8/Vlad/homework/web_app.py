from pathlib import Path
from urllib.parse import parse_qs
from typing import Callable, Iterable
from wsgiref.simple_server import make_server
import os
import json 

#absolute path
thisfolder = os.path.dirname(os.path.abspath(__file__))

# checking content type for static files linked to html file via href`s or src`s  (doesn`t work yet )
def content_type(path:str) -> str:                                                          
    if path.endswith(".css"):                                                    
        return "text/css"                                                        
    else:                                                                        
        return "text/html" 



class HTTPError(Exception):

    def __init__(self, reason: str, code: int):
        self.code = code
        self.reason = reason
        super().__init__(reason)


def get_feedback(env: dict):
    with open(Path(f'{thisfolder}/html/feedback.html'), 'rb') as fd:
        return fd.read()

#Storing inputed dict in json file 
def store_in_db(data:dict) -> None :

    initfile = os.path.join(thisfolder, 'db.json')
    old_data = []
    if not os.path.isfile(initfile):
        old_data.append(data)
        with open(initfile, mode='w') as f:
            f.write(json.dumps(old_data, indent=2))
    else:
        with open(initfile) as feedsjson:
            feeds = json.load(feedsjson)
        feeds.append(data)
        with open(initfile, mode='w') as f:
            f.write(json.dumps(feeds, indent=2))

 

def post_feedback(env: dict):
    expected_keys = ('user_first_name', 'user_last_name','user_age','user_gender')
    payload = env['wsgi.input'].read(int( env['CONTENT_LENGTH'] ))

    data = parse_qs(payload.decode())
    print(data)
    if len(data) != len(expected_keys):
        raise HTTPError('Bad Request', 400)

    for key in expected_keys:
        if key not in data:
            raise HTTPError('Bad Request', 400)

    store_in_db(data)
    return get_feedback(env)

def search_in_db(search:dict)  -> list :
    initfile = os.path.join(thisfolder, 'db.json')

    with open(initfile,'r') as json_db:
        db_data = json.load(json_db)
    if not search :
        return 
    find_elemets = []
    for item in db_data:
        if f"{item['user_first_name'][0].lower()} {item['user_last_name'][0].lower()}" == search['user_search'][0].lower() :
            find_elemets.append(item)
        # for key in item :
        #     if item[key][0] == search['user_search'][0]:
        #         find_elemets.append(item)
    return find_elemets

def search_result_to_html(row):
    return f' <div class="card text-white bg-info mb-3 style="max-width: 18rem;"> <div class="card-header">Find Someone</div> <div class="card-body"> <h5 class="card-title">User information from database </h5> <p class="card-text">{" ".join([str(val) for key in row  for val in row[key]])} </p></div></div>'

def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 
   
def get_search(env: dict):
    payload = env['QUERY_STRING']
    data = parse_qs(payload)

    data_from_db = search_in_db(data) 
    if data_from_db:
        html = """ 

            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

                    <style>
                        .user_info_card{
                            color:#393939;
                            font-family: "Gill Sans", sans-serif;
                            width:200px;
                            height:40px;
                        } 
                         """ + f"""
                    </style>
                </head>
                <body>
               
                <div class= "container">
                 <div class="alert alert-success" role="alert">
                    Success  !! We found {len(data_from_db) } matches, want to  <a href="/search" class="alert-link">Search again ?</a> 
                </div>
                    {
                        listToString([ search_result_to_html(item) for item in data_from_db])
                    }
                </div>
                </body>
            </html>
        
         """
        print('find something')  
        return html.encode()
    with open(Path(f'{thisfolder}/html/search.html'), 'rb') as fd:
        return fd.read()
    

def post_search(env: dict):
    pass


def not_found(env: dict):
    raise HTTPError('Not Found', 404)



ROUTING_TABLE = {
    '/feedback': {
        'GET': get_feedback,
        'POST': post_feedback,
    },
    '/feedback/send': {
        'POST': post_feedback,
    },
    '/search': {
        'GET': get_search,
        'POST': post_search,
    }
}


def app(env: dict, start_response: Callable) -> Iterable:
    # for key, val in env.items():
    #    print(key, '=', val)

    route = env['PATH_INFO']
    method = env['REQUEST_METHOD']
    try:
        handler = ROUTING_TABLE.get(route, {}).get(method, not_found)
        response = handler(env)
        headers = []                                                                   
        headers.append(("Content-Type", content_type(route)))  
        start_response('200 OK',headers)
        return [response]

    except HTTPError as herr:
        start_response(f'{herr.code} {herr.reason}', [('Content-type', 'text/html')])
        return [f'<h2>{herr.code} {herr.reason}</h2>'.encode()]


if __name__ == '__main__':
    port = 8003
    with make_server('', port, app) as httpd:
        print(f'Serving on port {port}...')
        httpd.serve_forever()
