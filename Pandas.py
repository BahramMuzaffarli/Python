import pandas as pd
my1= pd.read_csv('C:\\Users\\FX505DT\\Desktop\\my1.csv')
my2= pd.read_csv('C:\\Users\\FX505DT\\Desktop\\my2.csv')
my3= pd.read_csv('C:\\Users\\FX505DT\\Desktop\\my3.csv')

#print(test)

if {'Open','Close'}.issubset(my1.columns):
    my1['Change'] = (my1['Close'] - my1['Open'])/my1['Open']

if {'Open','Close'}.issubset(my2.columns):
    my2['Change'] = (my2['Close'] - my2['Open'])/my2['Open']

if {'Open','Close'}.issubset(my3.columns):
    my3['Change'] = (my3['Close'] - my3['Open'])/my3['Open']

print(my1)
print(my2)
print(my3)


my1.to_csv('C:\\Users\\FX505DT\\Desktop\\output1.csv')
my2.to_csv('C:\\Users\\FX505DT\\Desktop\\output2.csv')
my3.to_csv('C:\\Users\\FX505DT\\Desktop\\output3.csv')