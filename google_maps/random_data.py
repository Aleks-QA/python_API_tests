import random
import string
import datetime


# генерация числа случайного в промежутке от 1 до 100 с шагом 1
random_age = random.randrange(0, 101, 1)
print(f"random_age {random_age}")


# генерация числа с плавающей точкой в промежутке от 5.2 до 7.9
random_float = random.uniform(0, 100)
print(f"random_float {random_float}")


# генерация строки из 10 случайных символов
letters = string.ascii_letters
random_password = ''.join(random.choice(letters) for i in range(10))
print(f'password {random_password}')


# выбор случайного значения из list
name = random.choice(['Oliver', 'William', 'James', 'Alex', 'Rick', 'Anna', 'Bob', 'Jack'])
random_mail = name+'@'+random.choice(['mail.ru', 'gmail.com', 'ya.ru'])
print("name " + name, "mail " + random_mail)


# генерация случайной даты между двумя датами
start_date = datetime.date(1920, 1, 1)
end_date = datetime.date(2023, 2, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
birthday = start_date + datetime.timedelta(days=random_number_of_days)


