from food import Beverage, Meal
from person import Person


def main():
    # Create an adult and a child
    adult = Person("Dana", age=30)
    child = Person("Eli", age=12)

    # Create beverages
    lemonade = Beverage("Lemonade", contains_alcohol=False)
    wine = Beverage("Wine", contains_alcohol=True)

    # Wash hands before drinking
    adult.wash_hands()
    child.wash_hands()

    # Build and prep a meal
    meal = Meal([lemonade, wine])
    meal.prep()

    # Eat the meal (round-robin)
    meal.eat([adult, child])

    # Show final status
    adult.show_status()
    child.show_status()


if __name__ == "__main__":
    main()