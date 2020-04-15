MAX_CHAR = 26
#practical 6  

def practical6(tempstr, repstr): 
      
    global MAX_CHAR 
      
    count = [0] * MAX_CHAR  

    for i in range (0, len(tempstr)): 
        count[ord(tempstr[i]) - 97] += 1

    index = 0; 
    tempstr = "" 
      
    for i in range (0, len(repstr)): 
        j = 0
        while(j < count[ord(repstr[i]) - ord('a')]):  
            tempstr += repstr[i] 
            j = j + 1
            index += 1
      
    return tempstr
  

if __name__ == "__main__":
    str1 = "abaabbccabbed"
    str2 = "bedac"
    print(practical6(str1, str2))

#need to be explaned