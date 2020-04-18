# from ipaddress import ip_address
import re

def is_valid_ipv4(addr:str) -> bool :
    try:
        ad = addr.split('.')
    except:
        return 'invalid address'
    for x in ad :
        if x.isdigit()  :
            x = int(x)
        else:
            return 'invalid address'
        if x <= 255 and x >= 0:
            pass
        else :
            return False
    return True

def is_valid_mac(addr:str) -> bool :
    return re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", addr.lower())


if __name__ == "__main__":
    print(is_valid_ipv4('192.168.1.145'))       #True
    print(is_valid_ipv4('127.168.1.1415'))      #False
    print(is_valid_ipv4('127.168.ff.123'))    
    print(is_valid_ipv4(14))                    #False
    print(is_valid_mac('3D-E1-2D-83-9C-62'))    #True