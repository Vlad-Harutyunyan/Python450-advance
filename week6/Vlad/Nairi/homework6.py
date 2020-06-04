import urllib.request as rq


class Parse_data:
    def __init__(self,path):
        self.path = path

    def parse_path(self):

        with rq.urlopen(self.path) as response:

            output = response.read().decode('utf-8')
            output = output.split('<html lang=\"en\">')
            finall_reslut = output[0].split('<!--')[2].replace('<--','').replace('-->','').split(' ')

            return finall_reslut

    def get_message(self):
        inp = self.parse_path()
        finnal_result = []
        for word in inp :
            finnal_result.append(chr(int(word, 2)))
        return finnal_result
    
    def print_message(self):
        for word in self.get_message():
            print(word,end='')
        print()
    
if __name__ == "__main__":
    path = 'https://aca.am/en/index.html'
    test = Parse_data(path)
    test.print_message()