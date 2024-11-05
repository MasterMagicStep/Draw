from random import randint
T1_num = 5 # Hell
T2_num = 5 # Heaven
#
score1= randint(1,15)
score2= randint(1,15)
#
time1 = randint(10,1000)
time2 = randint(10, 1000)
#
print("В команде Мастера кода участников: %s ! " % T1_num)
print("Итого сегодня в командах участников: %s и %s !" % (T1_num, T2_num))
print("Команда Волшебники данных решила задач: {} !".format(score2))
print("Волшебники данных решили задачи за {} с !".format(time2))

print(f'Команды решили {score1} и {score2} задач.')

if score1 > score2 or score1 == score2 and time1 < time2:
    challenge_result = 'Победа команды Hell!'
elif score1 < score2 or score1 == score2 and time1 > time2:
    challenge_result = 'Победа команды Heaven!'
else:
    challenge_result = 'Draw!'
print(f'Результат битвы: {challenge_result}')

tasks_total = score1 + score2  # количество задач
time_avg = (time1 + time2) / tasks_total  # среднее время решения
print(f'Сегодня было решено {tasks_total} задач,',
      f'в среднем по {time_avg:.1f} секунды на задачу!')