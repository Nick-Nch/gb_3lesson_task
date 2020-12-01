# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def about_user(**kwargs):
   return kwargs


print(about_user(
name = input('Enter your name: '), surname = input('Enter your surname: '),
date = input('Enter your date of birth: '), city = input('Enter your city: '),
email = input('Enter your email: '), number = input('Enter your phone-number: ')
))

