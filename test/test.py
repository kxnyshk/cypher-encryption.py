import random
import string
import sys
from time import sleep

def writer(text):
    for char in text:
        sleep(0.10)
        sys.stdout.write(char)
        sys.stdout.flush()

list1 = ['a', 'b']
list2 = ['c', 'd']
list3 = []

i = 0
limit = len(list1)
while i<limit:
    list3.append(list1[i]+list2[i])
    i +=1

# print(list3)

# list3 = ['ac', 'bd']
list4 = ['a', 'b']
print(list3)
print(list4)
for item1 in list4:
    for item2 in list3:
        if item1 == item2[0:1]:
            print(f'matching {item1} with {item2[0:1]}')
            print('yes')
            break
        else:
            print(f'matching {item1} with {item2[0:1]}')
            print('no')

text = 'Hello! looking nice :)'

ref = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', 
'-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', 
';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 
'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

key = ['r@', '_Q', 'M%', '51', 'mV', 'nR', 'g>', "'z", 'PA', 'Hb', '-G', 
'FU', '$}', 'Kc', 'VN', '`l', 'Z9', 'Nf', 'kT', '=]', 'j$', 'W:', 'Dm', 
'(k', '9S', 'u7', '6|', '\\q', '~-', 'sH', '>,', 'YI', 'wr', ';W', ':y', 
')&', '33', '*M', 'Ls', '}(', 'qJ', '4P', "?'", 'yD', 'Bo', '+i', 'E?', 
'^=', 'R8', 'S;', '2g', 'XF', 'G~', 'xK', '7h', 'Cw', '<B', 'aa', 'c+', 
'{\\', 'o<', '"Z', 'T4', 'v6', ',Y', '&C', 'Ie', 'p!', '%/', 'Q#', 'd^', 
'/t', '1)', 'Oj', 'J[', '[0', 'Un', 'tx', 'l_', 'ip', '@2', 'hv', 'b`', 
'fX', '05', ']{', '8u', 'e.', 'AE', '!d', 'zL']

list_text = []
list_text[:] = text
# ['H', 'e', 'l', 'l', 'o', '!', ' ', 'l', 'o', 'o', 'k', 'i', 'n', 'g', 
# ' ', 'n', 'i', 'c', 'e', ' ', ':', ')']

index = []


for item1 in list_text:
    for item2 in ref:
        if item1 == item2:
            idx = ref.index(item2)
            index.append(idx)
            val = key[idx]
            str + val
            break

print(index)
print(key[0])
