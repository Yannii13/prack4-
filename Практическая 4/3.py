number=int(input("Введите четырехзначное число: "))
thousand=number//1000
hundred=(number%1000)//100
ten=(number%100)//10
one=(number%10)
print('цифра в позиции тысяч:',thousand)
print('цифра в позиции тысяч:',hundred)
print('цифра в позиции тысяч:',ten)
print('цифра в позиции тысяч:', one)