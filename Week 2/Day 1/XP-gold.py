print('\033[92mHello\033[0m \033[91mWorld\033[0m\n' * 5 + '\033[92mI\033[0m \033[91mLove Python\033[0m\n' * 5)

month = int(input('Hello user, please choose a month (1 to 12)'))
if 2 <= month or month == 12 :
    print('Winter')
elif 3 <= month <= 5 :
    print('Spring')
elif 6 <= month <= 8 :
    print('Summer')
elif 9 <= month <= 11 :
    print('Autumn')
else : print('Error !')
