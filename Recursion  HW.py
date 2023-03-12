import os
file = r'_C:\Users'
if os.path.exists(file):
    print(f'File{file} exists')
else:
    print(f'File{file} does not exists')

home_folder = os.path.expanduser('~')
print(home_folder)
my_dir = os.path.join(home_folder, 'Desktop')
print(os.listdir(my_dir))


for f in os.listdir(my_dir):
    desc = 'd' if os.path.isdir(f) \
else '-'
    print(f'{desc} {f}')

