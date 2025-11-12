m= int(input("Введите кол-во минут: "))
hours = m // 60
remaining_m = m % 60
print(f"{m} мин - это {hours} час {remaining_m} минут")
