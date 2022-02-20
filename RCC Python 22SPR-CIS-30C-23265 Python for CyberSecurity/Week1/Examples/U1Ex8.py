#U1Ex8.py

#dictionary - key:value or key:item
user_Acc = {
            'username':'mSmith',
            'password':'P@ssword1',
            'e-mail':'mSmith@company.com',
            'department':'IT',               
            }
print(user_Acc)

#update dictionary
user_Acc.update({'title':'Tech 1'})
print(user_Acc)

#using len()
print(len(user_Acc))

print('\nUsing keys...')
#using .keys()
print(user_Acc.keys())

print('\nUsing values or items...')
#using items()
print(user_Acc.items())

print('\nFor loop...')
#for loop to display content
for key, value in user_Acc.items():
    print(key,value)



