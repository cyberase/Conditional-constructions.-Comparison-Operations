age = int(input('Введите возраст: '))
if 18 <= age <= 27:
  children = int(input('Введите количество детей: '))
else:
  print('Непризывной возраст')
if children == 0:
  student = input('Вы учитесь на данный момент? ')
else:
  print('Не допущен')
if student == 'да' or 'Да' or 'дА':
  print('Не допущен')
elif student == 'нет' or 'Нет' or 'НЕТ':
  print('Допущен')
height = int(input('Введите рост: '))
if height < 170:
  print('В танкисты')
elif height < 185:
  print('На флот')
elif height < 200:
  print('В десантники')
else:
  print('В другие войска')
if 18 <= age <= 27:
  children = int(input('Введите количество детей: '))
else:
  print('Непризывной возраст')
if children == 0:
  student = input('Вы учитесь на данный момент? ')
else:
  print('Не допущен')
if student == 'да' or 'Да' or 'ДА':
  print('Не допущен')
elif student == 'нет' or 'Нет' or 'НЕТ':
  print('Допущен')
height = int(input('Введите рост: '))
if height < 170:
  print('В танкисты')
elif height < 185:
  print('На флот')
elif height < 200:
  print('В десантники')
else:
  print('В другие войска')

