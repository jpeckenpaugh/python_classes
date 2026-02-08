from food import Fruit, Meat, Meal
from person import Person, Vegetarian


def main():
    # Create people
    alice = Vegetarian("Alice", allergies=["peanut", "nut"])
    ben = Person("Ben", is_diabetic=True)

    # Create foods
    apple = Fruit("Apple")
    banana = Fruit("Banana")
    steak = Meat("Steak")

    # Wash hands before eating
    alice.wash_hands()
    ben.wash_hands()

    # Wash and ripen fruit, then eat
    apple.wash()
    apple.ripen()
    apple.eat(alice)

    # Cook meat and try to eat (vegetarian blocked)
    steak.cook()
    steak.eat(alice)

    # Diabetic fruit limit
    banana.wash()
    banana.ripen()
    banana.eat(ben)
    banana2 = Fruit("Banana")
    banana2.wash()
    banana2.ripen()
    banana2.eat(ben)

    # Meal prep and round-robin eating
    meal = Meal([apple, banana, steak])
    meal.prep()
    meal.eat([alice, ben])

    # JSON snapshots
    alice.to_json()
    ben.to_json()
    apple.to_json()
    steak.to_json()
    meal.to_json()


if __name__ == "__main__":
    main()