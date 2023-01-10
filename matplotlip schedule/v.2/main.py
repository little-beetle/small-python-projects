import numpy as np
import matplotlib.pyplot as plt
import sys

def title():
    return "Лабораторна робота №7\n" \
           "студент групи\n" \
           "\n" \
           "Умова. Програма може побудувати графік функції або площину\n" \
           "З необхідними параметрами, які введе користувач.\n"


class Graph:
    """
    Створюємо клас, який має основну функцію - побудова графіка.
    * self означає що перемінні та функції знаходяться на рівні класу
    """
    def __init__(self):
        """
        Створюємо змінну, яку будемо використувувати для друку лінії в меню
        """
        self.coordinate = []
        self.move = "*"*60


    def __str__(self):
        """
        Функція розповідає основну задачу класу
        :return: str
        """
        return "Програма будує графік, які введе користувач"


    def start_finish(self):
        """
        Функція запитує у користувача, які межі та крок графіка він хоче отримати
        Для цього є відповідні умови
        1 - перша точка має бути меншою за другу
        2 - 3 значення (крок) має бути більшим за нуль та більшим за різницю двох попередніх точок
        Якщо умова виконується, то повертаємо значення, якщо ні, то користувач повторно вводить значення
        :return:
        """
        print(self.move)
        print("На даному етапі необхідно обрати початок, та кінець графіка\n"
              "Наприклад: -2 2 0.1\n"
              "Відповідно \n"
              "- перша точка має бути меншою за другу\n"
              "- третє число має бути більшим за нуль та меншим за різницю попередніх чисел\n")
        border = input("--> ").split()  # перетворюємо значення, які введе користувач у тип list

        new_border = []  # сюди зберігає значення

        # перевірка
        if len(border) == 3:
            for i_dot in border:
                if self.is_float(i_dot):  # функція is_float перевіряє чи є значення, яке ввів користувач числом
                    new_border.append(float(i_dot))  # зберігаємо це значення в наш список
                else:
                    print(f"Це значення містить символ, які не є числом - {i_dot}")
                    return self.start_finish()  # повторна спроба
            # перевірка умови програми
            if new_border[1] - new_border[0] > new_border[2] > 0 and new_border[0] < new_border[1]:
                return tuple(new_border)
        # якщо якось з умов не виконалась, то починаємо спочатку
        print("Помилка! Слідкуйте за вказівками")
        return self.start_finish()


    def is_float(self, num):
        """
        Функція перевіряє чи є значення числом
        :param num: str
        :return: bool
        """
        # Структура (try - except) дає можливість спробувати виконати програму, якщо буде помилка
        # то програма про це попередить.
        try:
            float(num)
            return True
        except:
            return False


    def color_line(self):
        """
        Функція запитує у користувача, який колір він хоче отримати для графіка.
        :return: str (колір графіка)
        """
        print(self.move)
        print("Зараз необхідно обрати колір, який є в програмі")
        # створюємо словник, де зберігаються всі можливі варіанти кольорів
        colors = {
            "k": "чорний",
            "y": "жовтий",
            "b": "синій",
            "g": "зелений",
            "r": "червоний",
            "c": "блакитний",
            "m": "фіолетовий",
        }
        print("Ви можете обрати такі кольори!")
        # цикл для виведення всіх кольорів
        for i_key in colors.keys():
            print(f"\t{i_key} => {colors[i_key]}")
        print("Оберіть колір: ")
        user_color = input("--> ").lower().strip()
        # цикл для пошуку кольору, який введе користувач
        if user_color in colors.keys():
            print(f"Ви обрали - {user_color} колір")
            return user_color
        else:
            print("Такого кольору немає! Спробуйте ще раз.")
            return self.color_line()


    def line_view(self):
        """
        Функція дає можливість обрати інший вид прямої
        :return: str (тип прямої)
        """
        print(self.move)
        print("Чи хочете ви обрати інший вид прямої (стандарт це пряма)\n"
              "Введіть 'так' або 'ні' ")
        choice_kind = input("--> ").lower().strip()
        # Якщо користувач не хоче змінити пряму, то відповідно лінія буде у вигляді суцільної лінії
        if choice_kind == "ні":
            return ""
        # якщо користувач хоче змінити пряму, то він має обрати, яка саме буде ця пряма
        elif choice_kind == "так":

            print("Який вид прямої ви хочете мати")
            type_line = {"--": "штрих-пунктирна лінія",
                      "-": "пунктирна лінія"}
            for i_key in type_line:
                print(f"\t{i_key} -> {type_line[i_key]}")
            choice_line = input("--> ")
            # пошук такої прямої в словнику прямих
            if choice_line in type_line:
                return "{line}".format(line=choice_line)
            # якщо таких прямих не знайдено, то програма запропонує ще одну спробу
            else:
                print("Ви ввели не те значення!")
        return self.line_view()


    def do_you_need_point(self):
        """
        Функція запитує чи потрібно змінювати тип та колір точок
        :return: bool
        """
        print(self.move)
        print("Чи хочете ви обрати інший вид точки\n"
              "Введіть 'так' або 'ні' ")
        user_value = input("--> ")  # значення, яке вводить користувач
        if user_value == "так":  # якщо він хоче змінити точку
            return True  # повертаємо значення
        elif user_value == "ні":  # якщо він не хоче змінити точку
            return False  # повертаємо значення
        # Якщо значення не пройшло перевірку, то користувач повторно вводить значення
        print("Програма вас не розуміє, спробуйте ще раз")
        return self.do_you_need_point()  # повертаємо цю саму функцію, для ще однієї спроби


    def type_point(self):
        """
        Функція пропонує користувачу обрати тип точки, який наведений в програмі
        :return: str (тип точки)
        """
        print(self.move)
        print("Ви хочете змінити формат точки. Є такі варіанти")
        # словник з точками, які можуть бути в програмі
        point = {"*": "зірка",
                "^": "трикутник",
                "s": "квадрат",
                "o": "коло"}
        # показуємо ці значення користувачу
        for i_key in point.keys():
            print(f"\t{i_key}-{point[i_key]}")
        # користувач вводить значення (вид точки)
        user_point_type = input("--> ")
        # перевірка чи є такий вид точки в програмі
        if user_point_type in point.keys():
            print(f"Тепер ваша точка виглядає як {point[user_point_type]}")
            return user_point_type  # якщо така точка існує, то повертаємо її
        else:
            print("Програма вас не зрозуміла, спробуйте ще раз!")  # якщо такої точки не існує, то користувач повторно вводить значення
            return self.type_point()


    def equation_line(self, num):
        """
        Функція рахує математичну функцію
        :param num: float
        :return: num
        """
        try:
            return np.sin(num)
        except:
            # якщо така формула не може бути побудована, то програма терміново закривається
            print("Помилка у формулі. Перезавантажте програму.")
            return sys.exit()


    def math_line(self):
        """
        Функція будує графік за допомогою бібліотеки matplotlib
        :return: побудову графіка
        """
        print(self.move)
        border = self.start_finish()  # отримуємо границю та крок графіка
        color = self.color_line()  # отримуємо колір графіка
        type_line = self.line_view()  # отримуємо тип прямої
        line_func = f"{color}{type_line}"  # лінія та колір прямої

        need_dots =self.do_you_need_point()  # запитуємо чи хоче користувач змінити вид точки
        if need_dots:
            point = self.type_point()  # отримуємо значення точки
            print("Оберіть колір для точок графіка")
            color_dots = self.color_line()  # отримуємо колір точки
            dot = f"{color_dots}{point}"  # тип та колір точки
        else:
            dot = "ko"  # якщо користувач не захотів змінити точку, то записуємо точку як чорне коло

        # створюємо особливий тип, який зберігає всі значення які необхідні для побудови
        length = np.arange(*border)
        # початок побудови
        plt.figure()
        # називаємо графік та осі
        plt.title("Графік функції")
        plt.ylabel("Вісь Оy")
        plt.xlabel("Вісь Оx")
        # Також додаємо сітку для графіка
        plt.grid(True)
        # Робимо вікно з графіком великого розміру
        plt.subplot(111)
        # малюємо пряму
        plt.plot(length, self.equation_line(length), line_func,
                 label="Функція",)
        # малюємо точки
        plt.plot(length, self.equation_line(length), dot, label="точки функції")
        # показуємо додаткові значення для графіка
        plt.legend()
        # відкриття вікна з графіком
        plt.show()


class Space:
    """
    Клас який містить фунеції для побудови площини
    """
    def __init__(self):
        """
        створюємо константу, яку будемо використовувати, для того щоб розділяти пункти при вводі
        """
        self.move = "*"*60


    def __str__(self):
        """
        Коротка відомість програми
        :return: str
        """
        return "Зараз необхідно обрати параметри для побудови площини!"


    def details(self):
        """
        Програма запитує у користувачи чи потрібно деталізувати графік
        :return: bool
        """
        print(self.move)  # друкує лінію
        print("Чи хочете, щоб ваш графік був краще деталізованим? (+|-)")
        value = input("--> ").strip()  # користувач вводить значення та перетворюємо у тип (список)
        if value == "+":  # якщо користувач хоче додатково деталізувати графік
            return True
        elif value == "-":  # якщо користувач не хоче додатково деталізувати графік
            return False
        else:  # якщо користувач ввів не те що потрібно, то почати спочатку
            return self.details()


    def space(self):
        """
        побудова площини з необхідними параметроми та функціями
        :return: побудова площини
        """
        print(self.move)
        plane = plt.figure()  # створюємо нову перемінну plane
        space_build = plane.add_subplot(projection='3d')  # створюємо макет для побудови

        coordinate_x, coordinate_y, coordinate_z = self.equation_space()  # отримуємо координати точок

        color = self.color_space()  # отримуємо колір

        shade = self.shadow()  # тінь

        alpha = self.transparency()  # отримуємо прозорість площини

        detail = self.details()  # отримуємо деталізацію графіка
        space_build.plot_surface(
            coordinate_x, coordinate_y, coordinate_z, linewidth=0,
            cmap=color, shade=shade, alpha=alpha, antialiased=detail)
        print("для того, щоб скористатися програмою повторно, закрийте вікно з графіком")
        plt.show()

    def begin_end_space(self):
        """
        Початок та кінець графіка та крок графіка площини відповідних осей
        :return: tuple
        """
        print(self.move)
        print("Зараз вам необхідно обрати початок координат для осей.\n"
              "Початок. Кінець. Крок\n"
              "Наприклад\n"
              "-10 10 100")
        int_num = input("--> ")  # користувач вводить значення
        list_num = int_num.split()  # перетворюємо це значення в типlist
        list_int_num = []  # створюємо пустий список, куди будемо зберігати значення
        # перевірка
        if len(list_num) == 3:
            for i_num in list_num:
                try:
                    list_int_num.append(int(i_num))
                except:
                    print(f"Ви допустили помилку. Ви ввели - {i_num}. Спробуйте ще раз!")
                    return self.begin_end_space()
        else:
            print("Помилка. Повторна спроба!")
            return self.begin_end_space()
        # перевірка значень, які вказані нижче
        if list_int_num[0] < list_int_num[1] and list_int_num[2] > 0:
            return tuple(list_int_num)
        print("Помилка. Повторна спроба!")
        return self.begin_end_space()

    def equation_space(self):
        """
        Функція опрацьовує значення та повертає математичну функцію
        :return:
        """
        try:
            # змінна x
            start, end, step = self.begin_end_space()  # межі графіка по x
            ox = np.linspace(start, end, step)
            # змінна y
            start, end, step = self.begin_end_space()  # межі графіка по y
            oy = np.linspace(start, end, step)

            # утворюємо площину з кординатами x та y
            ox, oy = np.meshgrid(ox, oy)
            # змінна z

            oz = np.sin(ox) + np.sin(oy)

            return ox, oy, oz
        except:
            print("Помилка у формулі. Перевірте чи правиль ви все ввели!!! Та перезавантажте програму.")
            return sys.exit()


    def color_space(self):
        """
        Фунція запитує, який колір буде у площини
        :return: str (колір)
        """
        print(self.move)
        print("Оберіть колір")

        color_list = ["viridis", "plasma", "magma", "inferno", "cividis"]  # список всіх кольорів
        for i_color in color_list:
            print(f"\t{i_color}")
        # введення необхідної інформації, тобто кольорів, які зазначенні вище
        color = input(">>> ")
        # перевірка
        if color in color_list:
            return color
        print("Ви обрали не той колір, який доступний в програмі!. Спробуйте ще раз.")
        # почати спочатку, бо відбулась помилка
        return self.color_space()


    def shadow(self):
        """
        Функція запитує чи потрібні тіні для площини
        :return: bool
        """
        print(self.move)
        print("Чи потрібні тіні? (Введіть '+' або '-')")
        # введення необхідної інформації + або -
        shade = input("> ")
        # перевірка вводу
        if shade == "+":
            return True
        elif shade == "-":
            return False
        print("Ви допустили помилку у вводі, слідкуйте за вказівками на екрані! Спробуйте ще раз.")
        return self.shadow()


    def transparency(self):
        """
        Функція запитує, яка буде прозорість у площини. Можливі варіанти від 1 до 10
        :return:
        """
        print(self.move)
        print("Оберіть від 1 до 10 як буде намальовий графік:\n"
              "\t1 - напівпрозоро\n"
              "\t10 - повністю залитий")
        # введення необхідної інформації від 1 до 10, цілі числа
        alpha = input("> ")
        # перевірка
        if alpha.isnumeric():
            if 10 >= int(alpha) >= 1:
                # якщо все правильно, то повертаємо десяткове число від даного
                return int(alpha) * 0.1
        # почати спочатку, бо відбулась помилка
        return self.transparency()

def user_input():
    """
    Функція перевіряє чи правильно ввів користувач значення, можливі значення 0, 1, 2. Якщо ця умова не виконується,
    функція починається з самого початку.
    :return:
    """
    print("Введіть значення, якщо\n"
          "\t0 - хочете вийти з програми\n"
          "\t1 - хочете побудувати графік\n"
          "\t2 - хочете побудувати прощину")

    number = input(">>> ").strip()  # функція strip() прибирає випадкові пробіли
    if number == "0" or number == "1" or number == "2":  # перевірка умови
        return number  # повернення значення
    print("Ви ввели не те що потрібно. Слідкуйте за вказівками на екрані.")
    return user_input()  # почати спочатку




def menu():
    """
    Функція яка містить основиний функціонал програми
    :return: графік
    """
    option = user_input()  # користувач вводить значення через додаткову функцію, яка перевіряє значення

    # Нижче навередий цикл, який перевіряє, що обрав користува
    if option == "0":
        print("Ви обрали вийти з програми. Бувайте")
        sys.exit()  # Моментальне закриття програми
    elif option == "1":
        print("Ви обрали функцію для побудови графіка функції")

        Graph().math_line()  # Наступний крок, побудова функції
    elif option == "2":
        print("Ви обрали функцію для побудови площини")
        Space().space()  # Наступний крок, побудова площини





if __name__ == '__main__':
    print(title())
    while True:
        menu()
