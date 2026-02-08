import json


class Person:
    """Represents a person who can eat food and track simple status."""

    HANDS_CLEAN = "Clean"
    HANDS_DIRTY = "Dirty"

    def __init__(self, name, age=21, is_diabetic=False, allergies=None):
        """Create a person with a name, age, and optional dietary restrictions."""
        self.name = name
        self.age = age
        self.is_full = False
        self.is_diabetic = is_diabetic
        self.allergies = list(allergies) if allergies is not None else []
        self.hands = self.HANDS_DIRTY
        self.fruits_eaten = 0

    def use_bathroom(self):
        """Reset fullness and dirty the person's hands."""
        self.is_full = False
        self.hands = self.HANDS_DIRTY
        print("Used the bathroom. Hands are now Dirty.")

    def wash_hands(self):
        """Clean the person's hands."""
        self.hands = self.HANDS_CLEAN
        print("Washed hands. Hands are now Clean.")

    def show_status(self):
        """Print a short summary of the person's status."""
        allergies = ", ".join(self.allergies) if self.allergies else "None"
        full_status = "Full" if self.is_full else "Not full"
        is_vegetarian = isinstance(self, Vegetarian)
        print(
            f"{self.name} (Age {self.age}): {full_status}, Hands: {self.hands}, "
            f"Vegetarian: {is_vegetarian}, Diabetic: {self.is_diabetic}, "
            f"Allergies: {allergies}, Fruits eaten: {self.fruits_eaten}"
        )

    def to_dict(self):
        """Return a dictionary snapshot of the person's state."""
        return {
            "type": self.__class__.__name__,
            "name": self.name,
            "age": self.age,
            "is_full": self.is_full,
            "is_diabetic": self.is_diabetic,
            "allergies": list(self.allergies),
            "hands": self.hands,
            "fruits_eaten": self.fruits_eaten,
        }

    def to_json(self):
        """Print and return a JSON snapshot of the person's state."""
        data = self.to_dict()
        print(json.dumps(data))
        return data


class Vegetarian(Person):
    """Person subclass representing a vegetarian."""

    def __init__(self, name, age=21, is_diabetic=False, allergies=None):
        """Create a vegetarian person."""
        super().__init__(name, age=age, is_diabetic=is_diabetic, allergies=allergies)
