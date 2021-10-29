###
### Author: Xin Li
### White House
###
width = int(input('Specify side width:\n'))
middle = int(input('Specify middle width:\n'))
hight = int(input('Specify flag height:\n'))
wall = (width + middle) / 4 + 1
print(' ')
print(' '+'   '*width+'    '*middle+'|'+'##')
print((' '+'   '*width+'    '*middle+'|'+'\n')*hight, end='')
print(' '+'   '*width+'.-.-'*middle+"''"+'-.-.'*middle)
print(' '+'   '*width+';.__'*middle+'--'+'__.;'*middle)
print('.'+'___'*width+'[---'*middle+'--'+'---]'*middle+'___'*width+'.')
print(('|'+'II '*width+'||II'*middle+'HH'+'II||'*middle+' II'*width+'|'+'\n'+'|'+'.. '*width+'||..'*middle+'||'+'..||'*middle+' ..'*width+'|'+'\n')*int(wall), end='')
