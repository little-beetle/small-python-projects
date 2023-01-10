import matplotlib.pyplot as plt
import numpy as np
import sys


def main():
    print(title())
    while True:
        choice()


def title():
    """
    Заголовок програми з інструкцією

    :return: загаловок програми
    """
    return "Лабораторна робота №7\n" \
           "Фізико-математичного факультету\n" \
           "Студентки 1 курсу\n" \
           "Ім'я\n" \
           "{line}\n" \
           "Можливість програми:\n" \
           "Розроблена програма виконує побудову графіків,\n" \
           "які запропонує користувач.\n " \
           "З можливістю обирати колір та межі функції\n" \
           "{line}".format(line="-" * 40)


def choice():
    """
    Функція, в залежності від вибору користувача, пропонує наступний дії
    1 - побудову графіка функції, яка вже введена в програмі
    2 - побудова площини, яка вже введена в програмі
    3 - вихід з програми

    :return: відповідний розвиток подій або побудова графіка або побудова площини, або вихід
    """
    print("Оберіть пункт:\n"
          "1 - побудова графіка на площині;\n"
          "2 - побудова графіка у тривимірному просторі;\n"
          "3 - вихід з програми.\n")
    choice_num = check_input()
    if choice_num == 1:
        graph_construction()
    elif choice_num == 2:
        plane_construction()
    elif choice_num == 3:
        print("Вихід!")
        sys.exit()


def graph_construction():
    """
    Функція будує графік за допомогою бібліотеки matplotlib. Функція plot будує графік. Також ця функція має атрибути:
    line_formula(t) - початок та кінець відповідного графіка, та з яким кроком будується графік.
    'ro' - це червоні точки на графіку.
    label - назва лінії/точки.
    color - колір заливки графіка функції
    :return: побудований графік
    """
    print("Зараз необхідно обрати межі для майбутнього графіка.")
    # функція для перевірки вводу необхідних чисел. В даному випадку це початок та кінець графіка та крок побудови.
    border = check_border()
    # функція для вибору кольору графіка функції
    color_line = color_choice()
    print("*Підсказка. Щоб ще раз скористатися програмою, закрийте вікно з графіком!")
    # за допомогою бібліотеки numpy створюємо об'єкт типу ndarray, який містить рівномірно розташовані зачення
    # [початок, кінець, крок]
    length = np.arange(*border)
    plt.figure()  # створюємо нову фігуру/об'єкт
    plt.title("Функція")  # Назва об'єкту
    plt.ylabel("Y")  # Вісь OY
    plt.xlabel("X")  # Вісь Ox
    plt.subplot(111)  # Розміщення та розмір екрану

    plt.plot(length, line_formula(length), "go", label="точки функції")  # Розміщення на графіку точок
    plt.plot(length, line_formula(length), color=color_line, label="функція")  # Побудова графіка

    # побудова осей графіка, тобто пряма Ox та Oy
    ax = plt.gca()
    ax.axhline(y=0, color="k")
    ax.axvline(x=0, color="k")
    # legend - розміщує текст на осях
    plt.legend()
    # побудова графіка
    plt.show()


def plane_construction():
    """
    Функція за допомогою допоміжних функцій будує площину за допомогою математичної функції, який вже є в коді.
    :return: побудовану площину
    """
    fig = plt.figure()  # створюємо нову фігуру/об'єкт
    ax = fig.add_subplot(projection="3d")  # створюємо 3d фігуру/об'єкт

    # створення сітки
    x, y, z = plane_formula()
    # функція для вибору кольору
    color = color_plane()
    # функція вибору тіні
    shade = choice_shade()
    # функція можливості заливки
    alpha = choice_alpha()

    # antialised=False - вимнуте зглажування, щоб програма краще працювала, cmap - колір, linewidth - товщина лінії,
    # shade - тінь, alpha - заливка
    ax.plot_surface(x, y, z, linewidth=0, cmap=color, antialiased=False, shade=shade, alpha=alpha)
    # побудова графіка
    plt.show()


def choice_alpha():
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
    return choice_alpha()


def choice_shade():
    print("Чи потрібні тіні? (Введіть '+' або '-')")
    # введення необхідної інформації + або -
    shade = input("> ")
    # перевірка вводу
    if shade == "+":
        return True
    elif shade == "-":
        return False
    print("Ви допустили помилку у вводі, слідкуйте за вказівками на екрані! Спробуйте ще раз.")
    return choice_shade()


def color_choice():
    """
    :return: повертає колір прямої
    """
    print("Оберіть колір для функції\n"
          "Можливі такі варіанти:\n"
          "\tb - синій\tg - зелений\tr - червоний\n"
          "\tk - чорний\ty - жовтий\tm - рожевий\n"
          "Введіть відповідну літеру для вибору:")
    return color_check()


def color_plane():
    """
    :return: повертає колір заливки площини
    """
    print("Оберіть колір\n"
          "\tviridis\tplasma\tinferno\n"
          "\tmagma\tcividis")
    # введення необхідної інформації, тобто кольорів, які зазначенні вище
    color = input("> ")
    # перевірка
    if color == "viridis" or color == "plasma" or color == "inferno" or color == "magma" or color == "cividis":
        return color
    print("Ви обрали не той колір, який доступний в програмі!. Спробуйте ще раз.")
    # почати спочатку, бо відбулась помилка
    return color_plane()


def check_border():
    """
    Функція виконує важливу роботу для перевірки вводу початку та кінця графіка, щоб це були числа з відповідними
    умовами :return: початок та кінець графіка і відповідно з яким кроком буде побудований графік
    """
    print("-" * 30)
    print("Введіть, будь ласка, межі у форматі через пробіл\n"
          "'початок' 'кінець' 'крок'\n"
          "Наприклад: 1 5 0.1")
    # введення необхідної інформації
    border = input("> ")
    # перетворення str в list
    border_list = border.split()
    # створення нового списку, куди будуть входити фінальний результат
    answer = []
    # перевірка
    if len(border_list) == 3:
        for i_elem in border_list:
            if not is_float(i_elem):
                print("Ви ввели некоректний формат вводу. Виникла помилка! Спробуйте ще раз!")
                return check_border()
            else:
                answer.append(float(i_elem))
        # Перевірка відповідних умов, що початок має бути меншим за кінець.
        # А крок має бути меншим за різницю кінця та початку
        if answer[0] < answer[1] and answer[1] - answer[0] > answer[2] > 0:
            return tuple(answer)
    print("Відбулась помилку! Спробуйте ще раз!")
    return check_border()


def check_input():
    """
    Функція для переврки вводу
    :return: 1 або 2 або 3
    """
    print("Натистніть на клавіатурі клавіши '1' або '2' або '3' відповідно до заданих вище пунктів: ")
    check = input("> ")
    if check.isnumeric():
        if 4 > int(check) > 0:
            return int(check)
    print("Ви допустили помилку! Спробуйте ще раз!")
    return check_input()


def is_float(num):
    """
    Функція перевіряє та повертає число
    :param num:
    :return: число типу float
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def color_check():
    """
    функція перевіряє чи правильно користувач ввід колір
    :return: колір
    """
    color = input("> ").lower()
    # умова для перевірки
    if color.startswith("b") or color.startswith("g") or color.startswith("r") or \
            color.startswith("k") or color.startswith("y") or color.startswith("m"):
        return color[0]
    print("Ви обрали не ту літеру!")
    return color_check()


def border_plane():
    """
    Функція виконує важливу роботу для перевірки вводу початку та кінця площини, щоб це були числа з відповідними
    умовами :return: початок та кінець площини і відповідно з яким кроком буде побудований графік
    """
    print("Введіть початок та кінець координати та крок з яким буде будуватися графік (через пробіл):")
    int_num = input("> ")
    list_num = int_num.split()
    list_int_num = []
    # перевірка
    if len(list_num) == 3:
        for i_num in list_num:
            try:
                list_int_num.append(int(i_num))
            except:
                print(f"Помилки, ви не правильно ввели символ - {i_num}. Спробуйте ще раз спочатку!")
                return border_plane()
    else:
        print("Відбулась помилка! Спробуйте ще раз!")
        return border_plane()
    # відповідна умова
    if list_int_num[0] < list_int_num[1] and list_int_num[2] > 0:
        return tuple(list_int_num)
    print("Відбулась помилка! Спробуйте ще раз!")
    return border_plane()


# математичні функції
def line_formula(t):
    """
    Якщо користувач зробить помилку в цьому фрагменті і графік не зможе бути побудованим, то програма перестає
    працювати і попереджає користу, щоб він виправив цю помилку
    :param t:
    :return: математичну функцію
    """
    try:
        return np.exp(-t) * np.cos(2 * np.pi * t)
    except:
        print("Помилка у формулі. Перевірте чи правиль ви все ввели!!! Та перезавантажте програму.")
        return sys.exit()


def plane_formula():
    """
    Якщо користувач зробить помилку в цьому фрагменті і графік не зможе бути побудованим, то програма перестає
    працювати і попереджає користу, щоб він виправив цю помилку
    :return: математичну функцію
    """
    try:
        # створення сітки
        start, end, step = border_plane()  # межі графіка
        # змінна x
        x = np.linspace(start, end, step)
        start, end, step = border_plane()
        # змінна y
        y = np.linspace(start, end, step)
        x, y = np.meshgrid(x, y)

        # змінна z
        z = np.power((np.power(x, 2) + np.power(y, 2)), 0.5)

        return x, y, z
    except:
        print("Помилка у формулі. Перевірте чи правиль ви все ввели!!! Та перезавантажте програму.")
        return sys.exit()


# перевірка, яка файл не імпортується, то запустити програму
if __name__ == "__main__":
    main()
