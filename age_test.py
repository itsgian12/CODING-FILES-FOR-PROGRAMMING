from datetime import date

birth_year = input('what year were you born?')
current_year = date.today().year

age = int(current_year) - int(birth_year)

print('Your age is ' + str(age) + ' years old')

      