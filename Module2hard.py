left_stone = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
right_stone = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password_ = []
parol = ''
print('Какое число на левом камне?')
kod = input()
if kod.isdigit():
    left_number = int(kod)
       if left_number in range(3,21):   # У меня сдесь было in left_stone, а так можно не создавать список left_stone
        for i in right_stone:           # здесь тоже надо использовать range(1, 21)
            for j in right_stone:       # здесь тоже надо использовать range(1, 21), тогда списки left_stone, right_stone не нужны
                if left_number % (i + j) == 0:
                    para = [i, j]
                    if sorted(para) not in password_:
                        if str(i) != str(j):
                            password_.append(para)
                            parol = parol + str(i) + str(j)
        print('Ваш пароль :', parol)
    else: print('Вы ввели неверное число. Вам кирдык.')
else: print('Вы ввели какую-то ерунду. Вам кирдык.')
