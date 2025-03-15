def calculate_weighted_mark():
    subjects = {
        "English": 100,
        "Mathematics": 100,
        "Afrikaans": 100,
        "History": 50,
        "Geography": 50,
        "Physics": 50,
        "Life Sciences (Biology)": 50,
        "Drama": 25,
        "EBS": 33.33,
        "Art": 33.33,
        "Sport Science": 33.33
    }

    total_weight = sum(subjects.values())  # Should be 624.99
    weighted_score = 0

    print("Enter your percentage score (0-100) for each subject:")

    for subject, weight in subjects.items():
        while True:
            try:
                percentage = float(input(f"{subject}: "))
                if 0 <= percentage <= 100:
                    weighted_score += (percentage / 100) * weight  # Convert percentage to weighted score
                    break
                else:
                    print("Invalid input! Please enter a percentage between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")

    overall_percentage = (weighted_score / total_weight) * 100
    print(f"\nYour weighted total score: {weighted_score:.2f} / {total_weight:.2f}")
    print(f"Your final percentage: {overall_percentage:.2f}%")


# Ensure proper script execution
if __name__ == "__main__":
    calculate_weighted_mark()
