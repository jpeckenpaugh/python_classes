import re
import json

from person import Person, Vegetarian


class Food:
    """Base class for food items with shared eating behavior and state."""

    is_edible = True
    eaten = False

    def __init__(self, name):
        """Create a food item with a name."""
        self.name = name
        self.eater = None

    def eat(self, person):
        """Attempt to eat the food with a Person, enforcing rules."""
        if not isinstance(person, Person):
            print("Can only eat food with a Person.")
            return

        if not self.is_edible:
            print(f"{self.name} is not edible.")
            return

        if self.eaten:
            print(f"{self.name} has already been eaten by {self.eater}.")
            return

        if person.hands != Person.HANDS_CLEAN:
            print(f"{person.name} cannot eat {self.name}. Hands are not clean.")
            person.show_status()
            return

        if person.is_full:
            print(f"{person.name} cannot eat {self.name}. They are already full.")
            person.show_status()
            return

        allergy_match = None
        for allergy in person.allergies:
            if re.search(allergy, self.name, flags=re.IGNORECASE):
                allergy_match = allergy
                break

        if allergy_match is not None:
            print(f"{person.name} cannot eat {self.name}. Allergy match: {allergy_match}")
            person.show_status()
            return

        self.eaten = True
        self.eater = person.name
        person.is_full = True

        if isinstance(self, Fruit) and person.is_diabetic:
            person.fruits_eaten += 1

        print(f"{person.name} has eaten {self.name}.")
        person.show_status()

    def to_dict(self):
        """Return a dictionary snapshot of the food state."""
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "is_edible": self.is_edible,
            "eaten": self.eaten,
            "eater": self.eater,
        }

    def to_json(self):
        """Print and return a JSON snapshot of the food state."""
        data = self.to_dict()
        print(json.dumps(data))
        return data


class Fruit(Food):
    """Food subclass that must be washed and ripe before it can be eaten."""

    is_edible = False

    def __init__(self, name):
        """Create a fruit with default unwashed and unripe state."""
        super().__init__(name)
        self.is_ripe = False
        self.is_washed = False

    def wash(self):
        """Wash the fruit so it can be eaten."""
        self.is_washed = True
        print(f"{self.name} has been washed.")

    def ripen(self):
        """Ripen the fruit and mark it edible."""
        self.is_ripe = True
        self.is_edible = True
        print(f"{self.name} is now ripe.")

    def eat(self, person):
        """Require washing before delegating to base eating rules."""
        if not self.is_washed:
            print(f"{self.name} cannot be eaten until it is washed.")
            if isinstance(person, Person):
                person.show_status()
            return

        if isinstance(person, Person) and person.is_diabetic and person.fruits_eaten >= 1:
            print(f"{person.name} cannot eat {self.name}. Diabetic fruit limit reached.")
            person.show_status()
            return

        super().eat(person)

    def to_dict(self):
        """Return a dictionary snapshot of the fruit state."""
        data = super().to_dict()
        data["is_ripe"] = self.is_ripe
        data["is_washed"] = self.is_washed
        return data


class Meat(Food):
    """Food subclass that requires cooking and blocks vegetarian eaters."""

    is_edible = False

    def cook(self):
        """Cook the meat to make it edible."""
        self.is_edible = True
        print(f"{self.name} has been cooked and is now edible.")

    def eat(self, person):
        """Block vegetarians before delegating to base eating rules."""
        if isinstance(person, Vegetarian):
            print(f"{person.name} cannot eat {self.name}. They are vegetarian.")
            person.show_status()
            return

        super().eat(person)


class Beverage(Food):
    """Food subclass representing a drinkable beverage."""

    def __init__(self, name, contains_alcohol=False):
        """Create a beverage with an alcohol flag."""
        super().__init__(name)
        self.contains_alcohol = contains_alcohol

    def drink(self, person):
        """Drink the beverage using base eating rules."""
        if not isinstance(person, Person):
            print("Can only drink beverages with a Person.")
            return

        if self.contains_alcohol and person.age < 21:
            print(f"{person.name} cannot drink {self.name}. Must be 21+.")
            person.show_status()
            return

        if not self.is_edible:
            print(f"{self.name} is not edible.")
            return

        if self.eaten:
            print(f"{self.name} has already been drunk by {self.eater}.")
            return

        if person.hands != Person.HANDS_CLEAN:
            print(f"{person.name} cannot drink {self.name}. Hands are not clean.")
            person.show_status()
            return

        if person.is_full:
            print(f"{person.name} cannot drink {self.name}. They are already full.")
            person.show_status()
            return

        allergy_match = None
        for allergy in person.allergies:
            if re.search(allergy, self.name, flags=re.IGNORECASE):
                allergy_match = allergy
                break

        if allergy_match is not None:
            print(f"{person.name} cannot drink {self.name}. Allergy match: {allergy_match}")
            person.show_status()
            return

        self.eaten = True
        self.eater = person.name
        person.is_full = True

        print(f"{person.name} has drunk {self.name}.")
        person.show_status()

    def eat(self, person):
        """Alias to drink for compatibility with Food interface."""
        self.drink(person)

    def to_dict(self):
        """Return a dictionary snapshot of the beverage state."""
        data = super().to_dict()
        data["contains_alcohol"] = self.contains_alcohol
        return data