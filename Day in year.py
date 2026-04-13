D = input("Введите день:").strip()
M = input("Ведите месяц:").strip()
Y = input("Ведите год:").strip()


def num_day_years(day, month, is_leap_year=False):
    if (not is_leap_year) and month == 2 and day > 28:
        return 0
    if is_leap_year and month == 2 and day > 29:
        return 0

    feb = 28 if not is_leap_year else 29
    count_of_days = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return sum(count_of_days[:month - 1]) + d


if all([D.isdigit(), M.isdigit(), Y.isdigit()]):
    d = int(D)
    m = int(M)
    y = int(Y)
    if all([1 <= d <= 31, 1 <= m <= 12, 1 <= y <= 9999]):
        res = num_day_years(d, m, any([y % 400 == 0, (y % 4 == 0) and (not (y % 100 == 0))]))
        if not res:
            print("Некоректный ввод данных")
        else:
            print(res)
    else:
        print("Некоректный ввод данных")
else:
    print("Некоректный ввод данных")
