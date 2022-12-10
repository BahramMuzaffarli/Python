import os
path='C:/Users/FX505DT/Desktop'
l=[]
def find_files(path):
    files=os.listdir(path)
    for item in files:
        if os.path.isdir(os.path.join(path,item)):
            find_files((os.path.join(path,item)))
        else:
            if item.endswith(''):
                l.append(item)
(find_files(path))
print ('FileCount' , len(l))

def getfilesize (filename):
    return os.stat(filename).st_size
size = getfilesize('C:/Users/FX505DT/Desktop')
print(f'FileSize: {size}')



