def team_num_count(team, team_num):
    print('В команде %s кода участников: %d ! ' % (team, team_num))


def team_all_count(*team_num):
    print('Итого сегодня в командах участников: %d и %d !' % (team_num[0], team_num[1]))


def team_score(team, score):
    print("Команда {team} решила задач: {score} !".format(team=team, score=score))


def team_time(team, time):
    print("{team} решили задачи за {time} с !".format(team=team, time=time))


def score_count(score1, score2):
    print(f"Команды решили {score1} и {score2} задач.")


def challenge_result(team1, team2, score1, score2, time1, time2):
    if score1 > score2 or score1 == score2 and time1 > time2:
        result = f"Победа команды {team1}!"
    elif score1 < score2 or score1 == score_2 and time1 < time2:
        result = f"Победа команды {team2}!"
    else:
        result = "Ничья!"
    print(result)


def results_of_game(time1, time2, *score):
    tasks_total = sum(score)
    time_avg = tasks_total / (time1 + time2)
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")


team_1 = "Мастера кода"
team_2 = "Волшебники данных"

team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451


team_num_count(team_1, team1_num)
team_num_count(team_2, team2_num)
team_all_count(team_1, team_2)
team_score(team_1, score_1)
team_score(team_2, score_2)
team_time(team_1, team1_time)
team_time(team_2, team2_time)
score_count(score_1, score_2)
results_of_game(team1_time, team2_time, score_1, score_2)
challenge_result(team_1, team_2, score_1, score_2, team1_time, team2_time)

