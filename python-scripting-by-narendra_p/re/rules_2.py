import re
text='ita python l	earn and \n itis easy 	to'


######################### At the beginning ###########################
my_pat='^i[ts]'
print(re.findall(my_pat,text))


######################## At the end ###################################
#text='ita python and \n itis easy 	to learn'
my_pat="learn$"
print(re.findall(my_pat,text))


######################## \b ############################################
my_pat=r"\blearn\b"
print(re.findall(my_pat,text))


######################## \B #############################################
my_pat=r"\Blearn\B"
print(re.findall(my_pat,text))


######################### \n #############################################
my_pat=r"\n"
print(re.findall(my_pat,text))