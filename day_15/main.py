from os import system, name
from art import logo
import time

# determine money denomination that can be inserted into the machine
money_denomination = [
    5_000,
    10_000,
    20_000,
    50_000,
    75_000,
    100_000,
]

# List of ingredients
HAZELNUT_SYRUP = "hazelnut syrup"
PASSION_FRUIT_SYRUP = "passion fruit syrup"
MILK = "milk"
TEA = "tea"
SUGAR = "sugar"
BROWN_SUGAR = "brown sugar"
WATER = "water"
PERL = "perl"
GRASS_JELLY = "grass jelly"

ingredients_unit = {
    HAZELNUT_SYRUP: "ml",
    PASSION_FRUIT_SYRUP: "ml",
    MILK: "ml",
    TEA: "ml",
    SUGAR: "g",
    BROWN_SUGAR: "ml",
    WATER: "ml",
    PERL: "g",
    GRASS_JELLY: "g",
}

drinks = {
    "hazelnut milk tea": {
        "ingredients": {
            HAZELNUT_SYRUP: 25,
            MILK: 100,
            TEA: 50,
            SUGAR: 25,
            WATER: 500,
        },
        "price": 45_000,
    },
    "passion fruit juice": {
        "ingredients": {
            PASSION_FRUIT_SYRUP: 25,
            SUGAR: 25,
            WATER: 650,
        },
        "price": 35_000,
    },
    "brown sugar with fresh milk": {
        "ingredients": {
            BROWN_SUGAR: 75,
            MILK: 300,
            WATER: 325,
        },
        "price": 40_000,
    },
}

toppings = {
    PERL: {
        "serving": 25,
        "price": 5_000,
    },
    GRASS_JELLY: {
        "serving": 25,
        "price": 5_000,
    }
}

# Ingredients stock in the machine
ingredients = {
    HAZELNUT_SYRUP: 100,
    WATER: 1_000,
    SUGAR: 100,
    MILK: 500,
    TEA: 500,
    PASSION_FRUIT_SYRUP: 100,
    BROWN_SUGAR: 100,
    PERL: 100,
    GRASS_JELLY: 100,
}

# Money stock in the machine
money_bank = 0


def update_money_bank(money):
    global money_bank
    money_bank += money


def print_report():
    """Print list of ingredients and money available inside the machine."""
    print("Bahan-bahan yang tersedia:")
    print("==========================")
    i = 1
    for ingredient in ingredients:
        print(f"{i}) {ingredient.capitalize()}: {ingredients[ingredient]}{ingredients_unit[ingredient]}")
        i += 1
    print("==========================")
    print(f"Total uang yang tersedia: {money_format(money_bank)}")
    input("Enter untuk kembali ")


def valid_string_int(text, minimum=None, maximum=None):
    """Validate string representative of integer.
    Returns True if it is a valid integer and between the minimum and maximum value."""
    if not text.isdigit():
        return False

    text = int(text)

    if minimum is not None and maximum is not None:
        if text not in range(minimum, maximum + 1):
            return False
    elif minimum is None and maximum is None:
        return True
    elif minimum is not None:
        if text >= minimum:
            return True
    elif maximum is not None:
        if text <= maximum:
            return True

    return True


def choose_drink(drinks_menu):
    print("PILIH MINUMAN")
    print("==========================")

    i = 1
    menu = []
    for drink in drinks_menu:
        menu.append(drink)
        print(f"{i}) {drink.capitalize()}: {money_format(drinks_menu[drink]['price'])}")
        i += 1

    min_number = 1
    max_number = len(drinks_menu)

    prompt = f"Silahkan pilih antara no {min_number} - {max_number}: "
    choice = input(prompt)

    while not valid_string_int(choice, min_number, max_number):
        print("Maaf, input salah.")
        choice = input(prompt)

    return menu[int(choice) - 1]


def get_available_drinks():
    available_drinks = {}
    for drink in drinks:
        has_enough_ingredients = True
        for igr in drinks[drink]["ingredients"]:
            if ingredients[igr] < drinks[drink]["ingredients"][igr]:
                has_enough_ingredients = False
                break

        if has_enough_ingredients:
            available_drinks[drink] = drinks[drink]

    return available_drinks


def get_available_topping():
    available_topping = {}
    for topping in toppings:
        if ingredients[topping] >= toppings[topping]["serving"]:
            available_topping[topping] = toppings[topping]

    return available_topping


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def money_format(money):
    m = '{:,}'.format(money).replace(',', '.')
    return f"Rp{m}"


def choose_topping(available_topping):
    print("PILIH TOPPING")
    print("==========================")

    print("0) Tidak pakai topping")
    i = 1
    menu = []
    for topping in available_topping:
        menu.append(topping)
        print(f"{i}) {topping.capitalize()}: +{money_format(available_topping[topping]['price'])}")
        i += 1

    min_number = 0
    max_number = len(available_topping)
    prompt = f"Silahkan pilih antara no {min_number} - {max_number}: "
    choice = input(prompt)

    while not valid_string_int(choice, min_number, max_number):
        print("Maaf, input salah.")
        choice = input(prompt)

    choice = int(choice)

    if choice == 0:
        return

    return menu[choice - 1]


def insert_money():
    print("MASUKKAN UANG")
    print("==========================")

    money_sum = 0

    for denom in money_denomination:
        money = input(f"Pecahan {money_format(denom)}: ")
        if valid_string_int(money, 0, None):
            money_sum += int(money) * denom

    update_money_bank(money_sum)

    return money_sum


def choose_command():
    print("1) Pesan minum")
    print("2) Print laporan")
    print("3) Matikan")
    min_number = 1
    max_number = 3
    prompt = f"Silahkan pilih antara no {min_number} - {max_number}: "
    choice = input(prompt)
    while not valid_string_int(choice, min_number, max_number):
        print("Maaf, input salah.")
        choice = input(prompt)

    return int(choice)


def create_drink(drink, topping):
    print("MINUMAN SEDANG DIBUAT")
    print("==========================")
    for igr in drinks[drink]["ingredients"]:
        print(f"Mencampur {igr.capitalize()}...")
        time.sleep(0.500)
        ingredients[igr] -= drinks[drink]["ingredients"][igr]

    if topping is not None:
        print(f"Mencampur {topping.capitalize()}...")
        time.sleep(0.200)
        serving = toppings[topping]["serving"]
        ingredients[topping] -= serving

    print("Shaking...")
    time.sleep(1)
    print("Selesai!")


def order_drink():
    clear()
    available_drinks = get_available_drinks()
    if len(available_drinks) == 0:
        print("Maaf, bahan baku habis")
        input("Enter untuk kembali ")
        return
    drink = choose_drink(available_drinks)

    clear()
    available_topping = get_available_topping()
    if len(available_topping) == 0:
        return
    topping = choose_topping(available_topping)

    drink_price = drinks[drink]["price"]
    topping_price = toppings[topping]["price"]
    total_price = drink_price + topping_price

    clear()
    print(f"TOTAL BAYAR: {money_format(total_price)}")
    money = insert_money()

    if money < total_price:
        update_money_bank(-money)
        print(f"Maaf uang Anda tidak cukup. Silahkan ambil uang Anda {money_format(money)}")
        input("Enter untuk kembali ")
        return

    clear()
    create_drink(drink, topping)

    if money > total_price:
        update_money_bank(-(money - total_price))
        print(f"Silahkan ambil uang kembalian Anda {money_format(money - total_price)}")

    input("Enter untuk kembali ")


def run():
    clear()
    is_machine_on = True
    while is_machine_on:
        print(logo)
        command = choose_command()
        clear()
        if command == 1:
            order_drink()
        elif command == 2:
            print_report()
        elif command == 3:
            is_machine_on = False
            continue

        clear()


run()
