# 1. Создайте файл, содержащий следующие сведения о квартирах: количество
# комнат, общая и жилая площадь, этаж, наличие телефона, цена, адрес. Данные
# из файла запишите в словарь и выполните поиск по словарю по следующим
# параметрам: количество комнат, этаж (не ниже и не выше) и наличие
# телефона; жилая площадь (диапазон) и цена (не более); общая площадь
# (диапазон). Определите минимальную и максимальную цену из списка
# подходящих квартир.
from site import abs_paths

#комнаты;общая;жилая;этаж;телефон;цена;адрес

def load_flats(filename):
    flats = {}

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            rooms, total, living, floor, phone, price, address = line.strip().split(";")

            flats[i] = {
                "Комнаты": int(rooms),
                "Общая площадь": float(total),
                "Жилая площадь": float(living),
                "Этаж": int(floor),
                "Номер телефона": phone == "yes",
                "Цена": int(price),
                "Адрес": address
            }

    return flats


def get_search_params():
    print("Введите параметры поиска:")

    params = {
        "Комнаты": int(input("Количество комнат: ")),
        "Минимальный этаж": int(input("Минимальный этаж: ")),
        "Максимальный этаж": int(input("Максимальный этаж: ")),
        "Номер телефона": input("Наличие телефона (yes/no): ").lower() == "yes",
        "Минимальная жилая площадь": float(input("Минимальная жилая площадь: ")),
        "Максимальная жилая площадь": float(input("Максимальная жилая площадь: ")),
        "Максимальная цена": int(input("Максимальная цена: ")),
        "Минимальная общая площадь": float(input("Минимальная общая площадь: ")),
        "Максимальная общая площадь": float(input("Максимальная общая площадь: "))
    }

    return params


def filter_flats(flats, params):
    result = []

    for flat in flats.values():
        if (
            flat["Комнаты"] == params["Комнаты"] and
            params["Минимальный этаж"] <= flat["Этаж"] <= params["Максимальный этаж"] and
            flat["Номер телефона"] == params["Номер телефона"] and
            params["Минимальная жилая площадь"] <= flat["Жилая площадь"] <= params["Максимальная жилая площадь"] and
            flat["Цена"] <= params["Максимальная цена"] and
            params["Минимальная общая площадь"] <= flat["Общая площадь"] <= params["Максимальная жилая площадь"]
        ):
            result.append(flat)

    return result


def print_result(flats):
    if not flats:
        print("Подходящих квартир не найдено")
        return

    prices = [flat["Цена"] for flat in flats]

    print("\nПодходящие квартиры:\n")
    for flat in flats:
        print(flat)

    print("\nМинимальная цена:", min(prices))
    print("Максимальная цена:", max(prices))


def main():
    flats = load_flats("apartaments.txt")
    params = get_search_params()
    result = filter_flats(flats, params)
    print_result(result)


main()