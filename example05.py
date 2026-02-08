from food import Beverage
from person import Person


def main():
    # Create an adult and a child
    adult = Person("Dana", age=25)
    child = Person("Eli", age=15)

    # Create beverages
    juice = Beverage("Orange Juice", contains_alcohol=False)
    beer = Beverage("Beer", contains_alcohol=True)

    # Wash hands before drinking
    adult.wash_hands()
    child.wash_hands()

    # Non-alcoholic drink is allowed for both
    juice.drink(adult)
    juice2 = Beverage("Orange Juice", contains_alcohol=False)
    juice2.drink(child)

    # Alcoholic drink is blocked for child
    beer.drink(child)

    # Adult can drink alcohol
    beer2 = Beverage("Beer", contains_alcohol=True)
    beer2.drink(adult)


if __name__ == "__main__":
    main()