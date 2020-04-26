import re
import os

png_header = b'\x89PNG'
iend_header = b'\x00IEND\xae\x42\x60\x82\x00'

if not os.path.exists('./png'):
    os.mkdir('png')
    
def findAll(search, text, end=False):
    if end:
        return [m.end() for m in re.finditer(search, text)]
    else:
        return [m.start() for m in re.finditer(search, text)]

with open('./1p', 'rb') as fp:
    data = fp.read()

png_headers = findAll(png_header, data)
iend_headers = findAll(iend_header, data, True)

for i in range(len(png_headers)):
    h1 = png_headers[i]
    h2 = iend_headers[i]
    data2 = data[h1:h2]
    
    with open('./png/'+str(i)+'.png', 'wb') as fp:
        fp.write(data2)
