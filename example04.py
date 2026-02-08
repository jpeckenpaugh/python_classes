from food import Fruit, Meat
from person import Person, Vegetarian


def main():
    # Create people with dietary rules
    alice = Vegetarian("Alice", allergies=["peanut", "nut"])
    ben = Person("Ben", is_diabetic=True)

    # Create foods
    apple = Fruit("Apple")
    peanut_bar = Fruit("Peanut Bar")
    steak = Meat("Steak")

    # Wash hands before eating
    alice.wash_hands()
    ben.wash_hands()

    # Allergy check (Alice)
    peanut_bar.wash()
    peanut_bar.ripen()
    peanut_bar.eat(alice)

    # Vegetarian check (Alice)
    steak.cook()
    steak.eat(alice)

    # Diabetic fruit limit (Ben)
    apple.wash()
    apple.ripen()
    apple.eat(ben)

    apple2 = Fruit("Apple")
    apple2.wash()
    apple2.ripen()
    apple2.eat(ben)


if __name__ == "__main__":
    main()