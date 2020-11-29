user1 = input('Enter first number ')
user2 = input('Enter secound number ')
user3 = str(input('Enter operator '))
user = user1 + user3 +user2
if user == '45*3':
    print(555)
elif user =='56+9':
    print(77)
elif user == '56/6':
    print(4)
else:
    if '*' in user:
        print(int(user1) * int(user2))
    elif '+' in user:
        print(int(user1) + int(user2))
    elif '-' in user:
        print(int(user1) - int(user2))
    elif '/' in user:
        print(int(user1) / int(user2))
