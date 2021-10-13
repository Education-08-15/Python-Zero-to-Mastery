#  password checker practice

user_name = input('Enter username')
password = input('Enter password')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name} your password {hidden_password} is {password_length} letters long.')
# Shikshya  your password **** is 4 letters long.

print('*' * 3) # ***