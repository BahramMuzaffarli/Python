#1
def printFunc(msg):
    if isinstance(msg, str):
        print(msg)
    else:
        print("You should write string, but you wrote ", type(msg))


printFunc(31)


#2
def gameLoading(a):
    c = 100 - a
    if a >= 0 and a <= 100:
        print(f'Remain {c}%  ')
    else:
        print('ERROR')


gameLoading(17)


#3 Try/Except

num1 = input('1st number: ')
num2 = input('2nd number: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    print('Answer: ', num1/num2)

except ValueError:
    print('Write number ')

except ZeroDivisionError:
    print('You can not divide to Zero')


#4
#import sys
#sys.path.append('C:\Users\FX505DT\PycharmProjects\Python')
#import JupyterTest as j

def capet():
    print('Ugurlu Emeliyyat')

capet()


#strip,lower,upper,split,replace,capitalize
a = '       salam exi necesen        '
print(a)
print(a.strip())
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.replace('e', 'ə'))

#list,tuple,dict,set




