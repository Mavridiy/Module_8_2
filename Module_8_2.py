def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for number in numbers:
        try:
            result += number
        except:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        if isinstance(numbers, str):
            numbers = list(numbers)

        if not isinstance(numbers, (list, tuple)):
            raise TypeError("В numbers записан некорректный тип данных")

        total, incorrect_data = personal_sum(numbers)

        count = len(numbers) - incorrect_data
        if count == 0:
            raise ZeroDivisionError("Деление на ноль")

        average = total / count
        return average

    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(str(e))
        return None


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только числа
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
