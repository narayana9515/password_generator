import random
alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
  'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dig=['1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','&']
print("in this page you can generate password!!!")
letter_n=int(input("enter how many letters u want in u'r password:"))
dig_n=int(input("enter how many digits u want in u'r password:"))
if dig_n<2:
    print("the password must require minimus 2 digit for more pravacy!! ")
else:    
    sym_n=int(input("enter how many symbols want in u'r password:"))
    if sym_n<1:
        print("the password must require minimum 1 symbol for more privacy!!")
    else:
        total_size=letter_n+dig_n+sym_n
        if  total_size>=8:
            list=[]
            for i in range(1,letter_n+1):
                list+=random.choice(alp)
            for i in range(1,dig_n+1):
                list+=random.choice(dig)
            for i in range(1,sym_n+1):
                list+=random.choice(sym)    
            random.shuffle(list)
            password="" 
            for j in list:
                password+=j  
            print(password) 
        else:
             print("THE PASSWORD MUST REQUIRE MINIMUM (8) CHARACTERS ")              
