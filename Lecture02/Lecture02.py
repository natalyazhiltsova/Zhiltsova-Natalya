#1 Спросить пользователя и получить строку в ответ
s = input("Please, enter the number: ")
s = s.strip()

#2 Проверить корректность ввода

if not (1 <= len(s) <= 2):
    print("Invalid input")
    exit(1)
    
# Завершает программу если ввод некорректный 
    
if not s.isdigits():
    print("Invalid input")
    exit(1)

digits = "0123456789"

if s[0] not in digits:
    print("Invalid input")
    exit(1)

if len(s) > 1 and s[1] not in digits:
    print("Invalid input")
    exit(1)
    
#3 Преобразование строки в число

n = int(s)

#4 Проверка диапазона

if not(0 <= n <= 99):
    print("Invalid input")
    exit(1)

#5 Формирование ответа

answer = ""

if n // 10 == 2:
    answer += "двадцать "
elif n // 10 == 3:
    answer += "тридцать "
elif n // 10 == 4:
    answer += "тридцать "
elif n // 10 == 5:
    answer += "тридцать "
elif n // 10 == 6:
    answer += "тридцать "
elif n // 10 == 7:
    answer += "тридцать "
elif n // 10 == 8:
    answer += "тридцать "
elif n // 10 == 9:
    answer += "тридцать "

    
if n == 0 and n:
    answer = answer + "нуль"
elif n % 10 == 1:
    answer += "один"
elif n % 10 == 2:
    answer += "два"
elif n % 10 == 3:
    answer += "три"
elif n % 10 == 4:
    answer += "четыре"
elif n % 10 == 5:
    answer += "пять"
elif n % 10 == 6:
    answer += "шесть"
elif n % 10 == 7:
    answer += "семь"
elif n % 10 == 8:
    answer += "восемь"
elif n % 10 == 9:
    answer += "девять"
elif n == 10:
    answer += "десять"
elif n == 11:
    answer += "одиннадцать"
elif n == 12:
    answer += "двенадцать"
elif n == 13:
    answer += "тринадцать"
elif n == 14:
    answer += "четырнадцать"
elif n == 15:
    answer += "пятнадцать"
elif n == 16:
    answer += "шестнадцать"
elif n == 17:
    answer += "семнадцать"
elif n == 18:
    answer += "восемнадцать"
elif n == 19:
    answer += "девятнадцать"

answer = answer.rstrip()

print(f"Result: {answer}")
