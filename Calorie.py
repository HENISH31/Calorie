
# Predefined food database (per 100g)
FOOD_DATABASE = {
    "apple": {"calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2},
    "banana": {"calories": 96, "protein": 1.3, "carbs": 27, "fat": 0.3},
    "rice": {"calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
    "chicken breast": {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
    "egg": {"calories": 155, "protein": 13, "carbs": 1.1, "fat": 11},
    "milk": {"calories": 42, "protein": 3.4, "carbs": 5, "fat": 1},
    "bread": {"calories": 265, "protein": 9, "carbs": 49, "fat": 3.2},
    "moong dal": {"calories": 347, "protein": 24, "carbs": 63, "fat": 1.2},
    "soya chunks": {"calories": 336, "protein": 52, "carbs": 33, "fat": 1.5}
}

def display_foods():
    """Display available foods and their nutritional values."""
    print("\nAvailable Foods (per 100g):")
    print("-" * 50)
    for food, values in FOOD_DATABASE.items():
        print(f"{food.title():<15} | "
              f"Calories: {values['calories']} kcal, "
              f"Protein: {values['protein']} g, "
              f"Carbs: {values['carbs']} g, "
              f"Fat: {values['fat']} g")
    print("-" * 50)

def get_food_choice():
    """Get a valid food choice from the user."""
    while True:
        choice = input("Enter food name (or 'done' to finish): ").strip().lower()
        if choice == "done":
            return None
        if choice in FOOD_DATABASE:
            return choice
        print("Invalid food name. Please choose from the list.")

def get_quantity():
    """Get a valid quantity in grams from the user."""
    while True:
        try:
            qty = float(input("Enter quantity in grams: "))
            if qty > 0:
                return qty
            else:
                print("Quantity must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("=== Calorie Calculator App ===")
    total_calories = total_protein = total_carbs = total_fat = 0.0

    while True:
        display_foods()
        food = get_food_choice()
        if food is None:
            break
        qty = get_quantity()

        # Calculate based on quantity
        factor = qty / 100
        total_calories += FOOD_DATABASE[food]["calories"] * factor
        total_protein += FOOD_DATABASE[food]["protein"] * factor
        total_carbs += FOOD_DATABASE[food]["carbs"] * factor
        total_fat += FOOD_DATABASE[food]["fat"] * factor

    # Display results
    print("\n=== Daily Nutritional Summary ===")
    print(f"Total Calories: {total_calories:.2f} kcal")
    print(f"Protein: {total_protein:.2f} g")
    print(f"Carbs: {total_carbs:.2f} g")
    print(f"Fat: {total_fat:.2f} g")
    print("=================================")

if __name__ == "__main__":
    main()
