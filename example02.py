from food import Meat
from person import Person


def main():
    # Create a person and a meat item
    ben = Person("Ben")
    steak = Meat("Steak")

    # Wash hands before eating
    ben.wash_hands()

    # Try to eat before cooking (should fail)
    steak.eat(ben)

    # Cook and eat
    steak.cook()
    steak.eat(ben)


if __name__ == "__main__":
    main()