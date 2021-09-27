#This script requires pyperclip
#takes some lines of text and make an array with the data to be paste. 
'''
input

Magdalena 0 Barranquilla 10
Bogota 2 Bogota 16
Cauca 3 Cali 85
Sinu 4 Ituango 70
Tota 5 Tota 25

output

[['Magdalena', '0', 'Barranquilla', '10'], ['Bogota', '2', 'Bogota', '16'], ['Cauca', '3', 'Cali', '85'], ['Sinu', '4', 'Ituango', '70'], ['Tota', '5', 'Tota', '25']]

'''

import pyperclip as py
import re

text = py.paste()
text = text.split('\n')
ntext = []

for v in text:
    ntext.append(v.split())
print(ntext)
py.copy(ntext)
