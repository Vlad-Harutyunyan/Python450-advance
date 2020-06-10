from wsgiref.simple_server import make_server
from importlib import import_module


import configparser
import os

#absolute path
thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'wsgi_server.conf')

config = configparser.ConfigParser()
config.read(initfile)

#settings  from config 
module_name = config['app']['module']
app_name = config['app']['app']
ip = config['server']['ip']
port = config.getint('server','port')

def dynamic_import(abs_module_path, class_name):
    module_object = import_module(abs_module_path)

    target_class = getattr(module_object, class_name)

    return target_class

wsgi_app = None
try:
   wsgi_app = dynamic_import(f'{module_name}',f'{app_name}')
except:
    print('[Error] wrong module or application name , sorry !')


if __name__ == '__main__':

    with make_server(ip, port, wsgi_app) as httpd:
        print(f'Serving on port {port}...')
        httpd.serve_forever()  