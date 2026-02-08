from food import Fruit, Meat
from person import Person


def main():
    # Create a person and two food items
    person = Person("Casey")
    apple = Fruit("Apple")
    steak = Meat("Steak")

    # Wash hands before eating
    person.wash_hands()

    # Fruit must be washed and ripe
    apple.eat(person)
    apple.wash()
    apple.ripen()
    apple.eat(person)

    # Meat must be cooked
    steak.eat(person)
    steak.cook()
    steak.eat(person)

    # JSON snapshots
    person.to_json()
    apple.to_json()
    steak.to_json()


if __name__ == "__main__":
    main()