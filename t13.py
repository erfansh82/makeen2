my_list=[(),(2,3,4,),('a','b','c',),(),]
for i in my_list:
    if i==():
        my_list.remove(i)
print(f'my_list after change{my_list}')