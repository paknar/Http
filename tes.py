import os

dir = os.listdir()
hasil=''
for x in dir :
    hasil+=str(x + '\n')

print(hasil)
