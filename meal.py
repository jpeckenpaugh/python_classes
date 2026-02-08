import json

from food import Fruit, Meat


class Meal:
    """Collection of foods that can be prepped and eaten by a group."""

    def __init__(self, foods):
        """Create a meal from a list of foods."""
        self.foods = list(foods)

    def prep(self):
        """Prepare foods by washing/ripening fruit and cooking meat."""
        for food in self.foods:
            if isinstance(food, Fruit):
                if not food.is_washed:
                    food.wash()
                if not food.is_ripe:
                    food.ripen()
                continue

            if isinstance(food, Meat):
                if not food.is_edible:
                    food.cook()
                continue

            if not food.is_edible:
                print(f"No prep method for {food.name}.")

    def eat(self, persons):
        """Feed foods to people using a round-robin strategy."""
        persons = list(persons)
        if not persons:
            print("No persons to eat the meal.")
            return
        original_fullness = {person: person.is_full for person in persons}
        ate_any = {person: False for person in persons}
        for person in persons:
            person.is_full = False

        start_index = 0
        for food in self.foods:
            if food.eaten:
                continue

            ate = False
            for offset in range(len(persons)):
                person = persons[(start_index + offset) % len(persons)]
                before = food.eaten
                food.eat(person)
                if not before and food.eaten:
                    ate = True
                    ate_any[person] = True
                    person.is_full = False
                    start_index = (start_index + offset + 1) % len(persons)
                    break

            if not ate:
                print(f"No one could eat {food.name}.")

        for person in persons:
            if ate_any[person]:
                person.is_full = True
            else:
                person.is_full = original_fullness[person]

    def to_dict(self):
        """Return a dictionary snapshot of the meal state."""
        return {
            "type": self.__class__.__name__,
            "foods": [food.to_dict() for food in self.foods],
        }

    def to_json(self):
        """Print and return a JSON snapshot of the meal state."""
        data = self.to_dict()
        print(json.dumps(data))
        return data