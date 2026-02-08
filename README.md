# Python Classes Demo

This repo is a small, progressive demo of Python classes, inheritance, and simple business rules using a food-themed domain. It includes base classes, subclasses, and behavior rules to illustrate how state and logic can live on objects.

## What’s Inside

- `food.py`
  - Base class: `Food`
  - Subclasses: `Fruit`, `Meat`, `Beverage`
- `meal.py`
  - Composition: `Meal`
- `person.py`
  - Base class: `Person`
  - Subclass: `Vegetarian`

## Key Principles Illustrated

- Inheritance and method overriding (`Fruit.eat`, `Meat.eat`, `Beverage.drink`)
- Composition (`Meal` contains multiple `Food` items)
- State and validation inside methods (edibility, allergies, hand-washing)
- Polymorphism (different `Food` types can be handled uniformly)
- Simple domain rules (vegetarian restriction, diabetic fruit limit, alcohol age check)

## Rules Modeled

- People must wash hands before eating/drinking.
- `Fruit` must be washed and ripe before it can be eaten.
- `Meat` must be cooked before it can be eaten.
- `Vegetarian` cannot eat `Meat`.
- Diabetics can only eat one fruit.
- Alcoholic beverages require age 21+.
- During a `Meal`, people only become full at the end of the meal.

## Examples

Run any example with:

```bash
python example01.py
```

Example progression:

- `example01.py` — Minimal: 1 `Person`, 1 `Food`
- `example02.py` — `Meat` cooking requirement
- `example03.py` — `Fruit` washing/ripening + `Meat`
- `example04.py` — Allergies, `Vegetarian`, and diabetic fruit limit
- `example05.py` — `Beverage` with adult vs child
- `example06.py` — Allergy restriction example
- `example07.py` — `Meal` with beverages and age rules
- `example.py` — Full demo combining multiple features

## Files

- `food.py`
- `meal.py`
- `person.py`
- `example.py`
- `example01.py`
- `example02.py`
- `example03.py`
- `example04.py`
- `example05.py`
- `example06.py`
- `example07.py`