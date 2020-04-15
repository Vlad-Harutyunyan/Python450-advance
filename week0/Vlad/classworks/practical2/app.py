from logic import foo as logic_foo
from utils import foo as utils_foo

def foo():
    return 'hello from app.py'

if __name__ == "__main__" :
    print(foo())
    print(logic_foo())
    print(utils_foo())