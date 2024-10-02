import time

class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, adult_mode = False):
        self.title = title              #заголовок
        self.duration = duration        #продолжительность, сек
        self.adult_mode = adult_mode    #ограничение по возрасту
        self.time_now = 0               #сек остановки

    def __str__(self):
        return self.title

class UrTube:

    def __init__(self):
        self.users = []                 #список пользователей
        self.videos = []                #список видео
        self.current_user = None        #текущий пользователь

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False

    def register (self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f'Пользователь {nickname} уже существует')
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out (self):
        self.current_user = None

    def add (self, *videos):
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)


    def get_videos (self, word):
        result = []
        for video in self.videos:
            if word.lower() in video.title.lower():
                result.append(str(video))
        return result

    def watch_video (self, name_video):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        elif self.current_user.age < 18 and any([video.adult_mode for video in self.videos
                                                 if video.title == name_video]):
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
            for video in self.videos:
                if video.title == name_video:
                    for sec in range(1, video.duration + 1):
                        print(sec, end='')
                        time.sleep(0)
                    print(' Конец видео')
                    break
            else:
                return 'urban_pythonist'


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode = True)

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

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')







