import json
import pickle
import sys

def test_json():
    data = {'f_name':'Jhon',
            'l_name': 'Dow',
            'age':29,
            'working':True,
            'address':None
        }
    print(json.dumps(data))


    c = json.dumps([data,data],indent = '  ')
    print(c)
    print('json size = ',sys.getsizeof(c))

    c =json.loads(c)
    print(c)


def test_pickle():
    data = {'f_name':'Jhon',
            'l_name': 'Dow',
            'age':29,
            'working':True,
            'address':None
        }
    p = pickle.dumps(data)
    print(p)
    p = pickle.loads(p)
    print(p)
    print('Pickle size = ',len(p))


if __name__ == "__main__":
    test_json()
    test_pickle()
