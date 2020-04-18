from ipaddress import ip_address

def int32_to_ipv4(int32:int) -> str :
    t1 = int(int32 / 16777216) % 256
    t2 = int(int32 / 65536) % 256
    t3 = int(int32 / 256) % 256
    t4 = int(int32) % 256

    return f'{t1}.{t2}.{t3}.{t4}'
    
def ipv4_to_int32(ip:str) -> int :
    tmp = list(map(int, ip.split('.')))
    res = (16777216 * tmp[0]) + (65536 * tmp[1]) + (256 * tmp[2]) + tmp[3]
    return res

def ipv4_to_int32_vers2(ip:str) -> int :
    return int(''.join(f'{int(octet):08b}' for octet in ip.split('.')),2)

def int32_to_ipv4_vers2(int32:int) -> str :
    octet = [int((int32/256**x) % 256) for x in range(4)]
    print(octet[::-1])

if __name__ == "__main__" :

    print('Test by ip lib')
    print(int(ip_address('10.0.0.50')))
    print(ip_address(2149583361))


    print('Test by my own')
    print(int32_to_ipv4(2149583361))
    print(ipv4_to_int32('10.0.0.50'))
    print(ipv4_to_int32_vers2('10.0.0.50'))
    print(int32_to_ipv4_vers2(2149583361))
