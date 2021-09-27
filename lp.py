# This script requires pyeperclip
# This script takes a windows path copied in cliboard and returns a path that can be use
# to paste directly to the WSL terminal, in my case Ubuntu
# lp == linux path
# input
# C:\Program Files (x86)\Google
# D:\Code\Github\local_repo

# output for WSL Ubuntu
# cd /mnt/c/Program\ Files\ \(x86\)/Google
# cd /mnt/d/Code/Github/local_repo
import pyperclip
import re

others = [' ', '(', ')']
disks = ['d', 'c', 'f', 'g']
text = pyperclip.paste().replace('\\', '/')

for v in others:
    if(v in text):
        text = text.replace(v, f'\\{v}')

regex = re.compile(r'\w\:')

disk = ''

for d in disks:
    if(text.lower().startswith(d)):
        disk = d

newText = regex.sub(f'cd /mnt/{disk}', text)
pyperclip.copy(newText)
print(newText)
