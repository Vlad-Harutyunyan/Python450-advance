import re


#regular expression

# | - or - color|colour
# () - parentheses - col(o|ou)r
# ? - 0 or 1 occurences of the previous element - clolu?r
# * - 0 or more occurences of the previous element
# + = 1 or more occurences of the previous element
# e.t.c

line = "abb"
res1 = re.match('ab{1}',line)
c = res1.group()
print(c)  # group return result as a string

l = 'Python?'
c = re.findall('Python*!+|\?',l)

c1 = re.match('Python(!+|\?)',l).group()
print(c)
print(c1)
