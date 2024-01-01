import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
         's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J',
         'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']

symbols=['!','@','#','$','%','^','&','*','(',')']

print("WELCOME TO PASSWORD GENERATOR")
n_letters=int(input("HOW MANY LETTERS YOU WANT IN YOUR PASSWORD:"))
n_num=int(input("HOW MANY NUMBERS YOU WANT IN YOUR PASSWORD:"))
n_sym=int(input("HOW MANY SYMBOLS YOU WANT IN YOUR PASSWORD:"))

password_list=[]  #EMPTY LIST

for i in range(1,n_letters+1):  #it creates a random letters
    char=random.choice(letters)
    password_list += char

for i in range(1,n_num+1):   #it creates a random numbers
    char=random.choice(numbers)
    password_list += char

for i in range(1,n_sym+1):  #it creates a random symbols
    char=random.choice(symbols)
    password_list += char    
    
password=""
random.shuffle(password_list)

for i in password_list:
    password += i

print("PASSWORD=", password)   













