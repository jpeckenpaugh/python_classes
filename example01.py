from food import Food
from person import Person


def main():
    # Create one person and one food item
    person = Person("Alex")
    food = Food("Bread")

    # Wash hands before eating
    person.wash_hands()

    # Eat the food
    food.eat(person)

    # JSON snapshots
    person.to_json()
    food.to_json()


if __name__ == "__main__":
    main()