name_list = input('name : ').split()

print (name_list)
q_name = input('name : ')
flag = True
for i in range( len(name_list)):
    if name_list[i] == q_name:
        flag = False
        print( f'{q_name} in the list')
if flag == True:
    print(f'{q_name} not exist in the list')

""""""
name_list = input('name : ').split()
q_name = input('name : ')
flag = True
for name in name_list:
    if name == q_name:
        flag = False
        print(f'{q_name} in the list')
if flag :
    print(f'{q_name} not exist in the list')

""""""
name_list = input('name : ').split()
q_name = input('name : ')
print('yes' if q_name in name_list else 'no')