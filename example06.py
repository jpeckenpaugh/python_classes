from food import Beverage, Fruit
from person import Person


def main():
    # Create a person with an allergy
    alex = Person("Alex", allergies=["apple"])

    # Create foods and drinks
    apple = Fruit("Apple")
    apple_juice = Beverage("Apple Juice", contains_alcohol=False)

    # Wash hands before eating/drinking
    alex.wash_hands()

    # Allergy restriction blocks both apple and apple juice
    apple.wash()
    apple.ripen()
    apple.eat(alex)

    apple_juice.drink(alex)

    # JSON snapshots
    alex.to_json()
    apple.to_json()
    apple_juice.to_json()


if __name__ == "__main__":
    main()