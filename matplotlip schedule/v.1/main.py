"""
Лабораторна робота №7
Побудова графіка та площини
"""
# імпортує основні бібліотеки
import numpy as np  # використовуємо numpy для швидкого рахування
import matplotlib.pyplot as plt  # використовуємо matplotlib для побудови графіка та площини
import sys  # використовуємо sys для закриття програми

LINE = "-" * 80


def cap():
    return "Лабораторна робота № 7\n" \
           "Виконав студент групи ГРУПА ПРІЗВИЩЕ ТА ІМ'Я, варіант 17\n\n" \
           "Що робить програма?\n" \
           "Програма будує або графік або площину.\n" \
           "Функцію, яких користувач вводить в код програми і обирає, що побудувати\n" \
           "Програмає має можливості\n" \
           "\t1 - побудова графіка\n" \
           "\t2 - побудова площини\n" \
           "\t0 - вихід"


# Основна функція програми. Приймає всі значення та обробляє їх, щоб отримати побудаваний графік/площину
def main():
    menu()  # викливаємо функці menu(), яка дає вибір користувачу, що буде робити програма


# Функція містить 3 можливості, які може обрати користувач. 1 - побудова графіка. 2 - побудова площини. 3 - вихід.
def menu():
    option = proof_user_input()  # користувач вводить значення через додаткову функцію, яка перевіряє значення

    # Нижче навередий цикл, який перевіряє, що обрав користува
    if option == "0":
        print("Ви обрали вийти з програми. Бувайте")
        sys.exit()  # Моментальне закриття програми
    elif option == "1":
        print("Ви обрали функцію для побудови графіка функції")
        line()  # Наступний крок, побудова функції
    elif option == "2":
        print("Ви обрали функцію для побудови площини")
        space()  # Наступний крок, побудова площини


# Функція перевіряє чи правильно ввів користувач значення, можливі значення 0, 1, 2. Якщо ця умова не виконується,
# функція починається з самого початку.
def proof_user_input():
    print(LINE)
    print("Введіть значення, якщо\n"
          "\t0 - хочете вийти з програми\n"
          "\t1 - хочете побудувати графік\n"
          "\t2 - хочете побудувати прощину")

    number = input(">>> ").strip()  # функція strip() прибирає випадкові пробіли
    if number == "0" or number == "1" or number == "2":  # перевірка умови
        return number  # повернення значення
    print("Ви ввели не те що потрібно. Слідкуйте за вказівками на екрані.")
    return proof_user_input()  # почати спочатку


# Функція виконує роботу перевірки. Тобто, якщо користувач ввів значення, яке не може бути перетворенення в тип 'float',
# то попередити його, та запустити функцію повторно
def proof_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


# Функція запитує у користувача, який буде початок, кінець та крок для побудови графіка функції.
# Якщо значення будуть неправильними за умовами, які наведені нижче, то програма попросить ввести значення ще раз
def begin_end_line():
    print(LINE)  # переміння, яка містить в собі звичайну лінію. Це для зручності користувача
    print("Зараз вам необхідно ввести початкову точку графіка та кінцеву і відповідно\n"
          "Умова вводу:\n"
          "\t1) початкове число має бути меншим за друге число\n"
          "\t2) різниця 2 числа та 1 має бути більшою за 3\n"
          "\t3) 3 число має бути більшим за 0\n"
          "Наприклад\n"
          "\t-5 5 0.1\n"
          "*Підсказка: чим менший крок, ти кращий графік\n")
    border_line = input(">>> ").split()  # Користувач вводить значення та ці значення перетвоються відразу в тип list()

    return_border = []  # Створюємо пустий список, куди программа буде вписувати необхідні відповіді

    # Перевірка умови
    if len(border_line) == 3:  # список має бути дорівнювати 3 елементам
        for i_elem in border_line:  # перевіряємо кожен з цих елементів
            if proof_float(i_elem):  # якщо число може бути дробовим, то продовжуємо
                return_border.append(float(i_elem))  # записуємо значення в список return_border
            else:  # інакше починаємо спочатку
                print("Ви допустили помилки у вводі чисел. Спробуйте ще раз!")
                return begin_end_line()  # Ще одна спроба

        # Якщо всі значення є числами, то перевіряємо чи підходять вони для умови
        if return_border[0] < return_border[1] and return_border[1] - return_border[0] > return_border[2] > 0:
            return tuple(return_border)  # якщо так, то повертаємо кортеж з цими значеннями
    print(
        "Ви допустили помилку, слідкуйте за вказівками на екрані")  # інакше програма повідомляє, що користувач
    # допустив помилку
    return begin_end_line()


# Функція запитує у користувача, який колір графік він хоче мати. Якщо станеться помилка, то програма попередить про
# це користувача, і почнеться з самого початку
def line_color():
    print(LINE)
    colors = {"b": "синій",
              "g": "зелений",
              "r": "червоний",
              "c": "блакитний",
              "m": "фіолетовий",
              "y": "жовтий",
              "k": "чорний"
              }
    print("Програма містить такі кольори:")
    for i_key, i_value in colors.items():
        print(f"\tназва {i_key} - колір {i_value}")
    print("Введіть колір.")
    color = input(">>> ").lower().strip()
    if color in colors.keys():
        print("Ви обрали - {color_line} колір".format(color_line=colors[color]))
        return color
    else:
        print("Ви допустили помилку при вводі. Такий колір програма не може відобразити")
        return line_color()


# Функція запитує у користувача, який тип лінії він хоче отримати, для побудови графіка. Тобто це може бути прямо лінія
# або пунктирна, або штрих пунктирна лінія
def type_line():
    print(LINE)
    print("Який тип прямої ви хочете отримати?")
    t_line = {".": "пряма",
              "--": "штрих-пунктир",
              "-": "пунктир"}
    for i_key, i_value in t_line.items():
        print(f"\t{i_key} -> {i_value}")
    choice = input(">>> ")
    if choice in t_line.keys():
        if choice == ".":
            return ""
        else:
            return choice
    else:
        print("Щось пішло не так! Спробуйте ще раз!")
        return type_line()


# Функція запитує чи хоче користувач точки на графіку
def need_dot():
    print(LINE)
    print("Чи ви змінити точки (+|-)")
    choice = input(">>> ").strip()
    if choice == "+":
        return True
    elif choice == "-":
        return False
    else:
        print("Ви ввели не те що потрібно")
        return need_dot()


# Функція пропонує обрати тип точки
def type_dots():
    print(LINE)  # Друкуємо лінію, для зручності користувача
    print("Якого типу ви хочете точки на графіку. Можливі варіанти")
    dots = {"*": "зірка",
            "^": "трикутник",
            "s": "квадрат",
            "o": "коло"}
    for i_key, i_value in dots.items():
        print(f"\t{i_key}-{i_value}")
    type_dot = input(">>> ")
    if type_dot in dots.keys():
        print(f"Ви обрали тип точки - {dots[type_dot]}")
        return type_dot
    else:
        print("Програма вас не розуміє")
        return type_dots()


# Рівняння функції
def equation_line(t):
    try:
        return np.sin(t) * np.cos(t)
    except:
        print("Помилка у формулі. Перевірте чи правиль ви все ввели!!! Та перезавантажте програму.")
        return sys.exit()


# Функція будує графік, використовуючи допоміжні функції та бібліотеки
def line():
    print(LINE)
    border = begin_end_line()
    print("Оберіть колір для графіка")
    color = line_color()

    type_line_func = type_line()
    line_func = f"{color}{type_line_func}"
    need_dots = need_dot()
    if need_dots:
        dots = type_dots()
        print("Оберіть колір для точок графіка")
        color_dots = line_color()
        dot = f"{color_dots}{dots}"
    else:
        dot = "ko"
    length = np.arange(*border)

    plt.figure()

    plt.title("Функція")
    plt.ylabel("Вісь Оy")
    plt.xlabel("Вісь Оx")
    plt.grid(True)
    plt.subplot(111)

    plt.plot(length, equation_line(length), line_func, label="функція")  # Побудова графіка
    plt.plot(length, equation_line(length), dot, label="точки функції")  # Розміщення на графіку точок

    plt.legend()
    print("для того, щоб скористатися програмою повторно, закрийте вікно з графіком")
    plt.show()


# функція запитує у користувачи потрібно додаткова деталізація графіка
def antialias():
    print(LINE)
    print("Чи хочете, щоб ваш графік був краще деталізованим? (+|-)")
    value = input(">>> ").strip()
    if value == "+":
        return True
    elif value == "-":
        return False
    else:
        return antialias()


# Функція будує площину, за допомогою додаткових функцій та бібліотеки matplotlib
def space():
    print(LINE)
    plane = plt.figure()  # створюємо нову перемінну plane
    space_build = plane.add_subplot(projection='3d')  # створюємо макет для побудови

    coordinate_x, coordinate_y, coordinate_z = equation_space()  # отримуємо координати точок

    color = color_space()  # отримуємо колір

    shade = shadow()  # тінь

    alpha = transparency()  # отримуємо густину площини

    straighten = antialias()  # отримуємо деталізацію графіка
    space_build.plot_surface(
        coordinate_x, coordinate_y, coordinate_z, linewidth=0,
        cmap=color, shade=shade, alpha=alpha, antialiased=straighten)
    print("для того, щоб скористатися програмою повторно, закрийте вікно з графіком")
    plt.show()


# Функція запитує який буде початок та кінець площини, та крок.
# Спочатку для координати 'x', потім для 'y', а координату 'z' програма рахує самостійно
def begin_end_space():
    print(LINE)
    print("Зараз вам необхідно обрати початок координат для осей.\n"
          "Початок. Кінець. Крок\n"
          "Наприклад\n"
          "-10 10 100")
    int_num = input(">>> ")
    list_num = int_num.split()
    list_int_num = []  # створюємо пустий список, куди будемо зберігати значення
    # перевірка
    if len(list_num) == 3:
        for i_num in list_num:
            try:
                list_int_num.append(int(i_num))
            except:
                print(f"Ви допустили помилку. Ви ввели - {i_num}. Спробуйте ще раз!")
                return begin_end_space()
    else:
        print("Помилка. Повторна спроба!")
        return begin_end_space()
    # перевірка значень, які вказані нижче
    if list_int_num[0] < list_int_num[1] and list_int_num[2] > 0:
        return tuple(list_int_num)
    print("Помилка. Повторна спроба!")
    return begin_end_space()


# Рівняння для площини
def equation_space():
    try:
        # змінна x
        start, end, step = begin_end_space()  # межі графіка по x
        x_coordinate = np.linspace(start, end, step)
        # змінна y
        start, end, step = begin_end_space()  # межі графіка по y
        y_coordinate = np.linspace(start, end, step)

        # утворюємо площину з кординатами x та y
        x_coordinate, y_coordinate = np.meshgrid(x_coordinate, y_coordinate)
        # змінна z

        z_coordinate = np.sin(x_coordinate) * np.cos(y_coordinate)
        # z_coordinate = np.power((np.power(x_coordinate, 2) + np.power(x_coordinate, 2)), 0.5)

        return x_coordinate, y_coordinate, z_coordinate
    except:
        print("Помилка у формулі. Перевірте чи правиль ви все ввели!!! Та перезавантажте програму.")
        return sys.exit()


# Фунція запитує, який колір буде у площини
def color_space():
    print(LINE)
    print("Оберіть колір")

    color_list = ["viridis", "plasma", "magma", "inferno", "cividis"]
    for i_color in color_list:
        print(f"\t{i_color}")
    # введення необхідної інформації, тобто кольорів, які зазначенні вище
    color = input(">>> ")
    # перевірка
    if color in color_list:
        return color
    print("Ви обрали не той колір, який доступний в програмі!. Спробуйте ще раз.")
    # почати спочатку, бо відбулась помилка
    return color_space()


# Функція запитує чи потрібні тіні для площини
def shadow():
    print(LINE)
    print("Чи потрібні тіні? (Введіть '+' або '-')")
    # введення необхідної інформації + або -
    shade = input("> ")
    # перевірка вводу
    if shade == "+":
        return True
    elif shade == "-":
        return False
    print("Ви допустили помилку у вводі, слідкуйте за вказівками на екрані! Спробуйте ще раз.")
    return shadow()


# Функція запитує, яка буде прозорість у площини. Можливі варіанти від 1 до 10
def transparency():
    print(LINE)
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
    return transparency()


if __name__ == '__main__':
    print(cap())
    while True:
        main()
