class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль
    """

# Функция создания юзера.
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

# Функция создания базы данных. Пока пустой словарь.
class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input('Приветствую! Выберете действие: \n1 - Вход\n2 - Регистрация\n')
        user = User(input('Введите логин: '),
        password := input('Введите пароль: '),
        password2 := input('Повторите пароль: '))
        # Блок информации условия для надежности пароля.

        def check_password(password):
            # password = input('Введите пароль:')
            digits = '1234567890'
            upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lower_letters = 'abcdefghijklmnopqrstuvwxyz'
            symbols = '!@#$%^&*()-+'
            acceptable = digits + upper_letters + lower_letters + symbols

            passwd = set(password)
            if any(char not in acceptable for char in passwd):
                print('Ошибка. Запрещенный спецсимвол')
            else:
                recommendations = []
                if len(password) < 8:
                    recommendations.append(f'увеличить число символов - {12 - len(password)}')
                for what, message in ((digits, 'цифру'),
                                      (symbols, 'спецсимвол'),
                                      (upper_letters, 'заглавную букву'),
                                      (lower_letters, 'строчную букву')):
                    if all(char not in what for char in passwd):
                        recommendations.append(f'добавить 1 {message}')

                if recommendations:
                    print("Слабый пароль. Рекомендации:", ", ".join(recommendations))
                else:
                    print('Сильный пароль.')


        # tests
        for test in ("qwety", "Qwert_Y", "Q123wer123tY", "A^B@C*D", "@PowerRangers123@"):
            print("Password:", test)
            check_password(test)
            print()


        if password != password2:
          exit()
        database.add_user(user.username,user.password)
        print(database.data)

