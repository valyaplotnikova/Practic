from time import sleep


class User:
    """Класс пользователя, содержащий атрибуты никнейм, пароль и возраст"""

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return self.nickname

    def __str___(self):
        return f'{self.nickname} - {self.age}'

    def get_info(self):
        return self.nickname, self.password

    def __eq__(self, other):
        return self.nickname == other.nickname


class Video:
    """Класс видео, содержащий атрибуты"""

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __repr__(self):
        return self.title


class UrTube:
    """Класс UrTube, содержащий атрибуты: users(список объектов User), videos(список объектов Video),
    current_user(текущий пользователь, User)"""

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """Метод для входа в систему.
                Если пароль и никнейм совпадают, пользователь залогинен"""
        self.log_out()
        for user in self.users:
            if user.get_info() == (nickname, hash(password)):  # Сравнение по хэшу пароля
                self.current_user = user
                return user  # Возвращаем пользователя, если логин успешен
        print("Неверный логин или пароль")  # Сообщение, если не найден пользователь

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        """Метод для регистрации пользователя"""
        new_user = User(nickname, password, age)
        if new_user not in self.users:  # Проверка, что такого пользователя нет
            self.users.append(new_user)
            self.log_in(nickname, password)  # Логиним пользователя после регистрации
        else:
            print(f"Пользователь {nickname} уже существует")

    def add(self, *args):
        for video in args:
            if video.title not in [v.title for v in self.videos]:  # Проверка по названию видео
                self.videos.append(video)

    def get_videos(self, value):
        video_list = []
        for video in self.videos:
            if value.lower() in video.title.lower():
                video_list.append(video.title)
        return video_list

    def watch_video(self, video_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == video_name:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    video.time_now += 1
                    print(video.time_now, end=' ')
                    sleep(0.1)
                video.time_now = 0
                print("\nКонец видео")
                return

        print("Видео не найдено")


"""
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
 Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
с такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
что password передаётся в виде строки, а сравнивается по хэшу.

Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
 если пользователя не существует (с таким же nickname). Если существует, выводит на экран:
 "Пользователь {nickname} уже существует".

  После регистрации, вход выполняется автоматически.

Метод log_out для сброса текущего пользователя на None.

Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
если с таким же названием видео ещё не существует. В противном случае ничего не происходит.

Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих
поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
После текущее время просмотра данного видео сбрасывается.
    """

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# # Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

"""
['Лучший язык программирования 2024 года']
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео
Вам нет 18 лет, пожалуйста покиньте страницу
1 2 3 4 5 6 7 8 9 10 Конец видео
Пользователь vasya_pupkin уже существует
urban_pythonist
"""
