###
### Author: Xin Li
### Eiffel Tower
###
size = float(input('Enter Eiffel tower size:\n'))
UH = size*1.5
MW = size*2+1
MH = size/2+3
LW = size*4+1
LH = size/1.5
M = (MW-3)/2
L = (LW-MW)/2
print(' ')
print(' '*3+' '*int(L)+' '*int(M)+' '+'$')
print((' '*3+' '*int(L)+' '*int(M)+'|Z|'+'\n')*int(UH), end='')
print(' '*2+' '*int(L)+'/'+'Z'*int(MW)+'\\')
print((' '*2+' '*int(L)+'H'+' '*int(MW)+'H'+'\n')*int(MH), end='')
print(' '*2+'/'+'%'*int(LW)+'\\')
print((' '+'##'+' '*int(LW)+'##'+'\n')*int(LH), end='')
print(('##'+' '*int(LW)+' '*2+'##'+'\n')*int(LH), end='')
