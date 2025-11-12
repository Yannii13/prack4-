num=int(input("Введите четырехзначное число: "))
thous=num//1000
hund=(num%1000)//100
ten=(num%100)//10
one=(num%10)
print('цифра в позиции тысяч:',thous)
print('цифра в позиции тысяч:',hund)
print('цифра в позиции тысяч:',ten)
print('цифра в позиции тысяч:', one)
