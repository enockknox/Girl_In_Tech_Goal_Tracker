import json
import os

# This file will store goals
GOAL_FILE = "goals.json"

# Load existing goals from file (if any)
def load_goals():
    if os.path.exists(GOAL_FILE):
        with open(GOAL_FILE, "r") as file:
            return json.load(file)
    else:
        return []  # Start with empty list if file doesn't exist

# Save goals back to file
def save_goals(goals):
    with open(GOAL_FILE, "w") as file:
        json.dump(goals, file, indent=4)

# Add a new goal
def add_goal(goals):
    print("\n--- Add New Goal ---")
    title = input("What is your goal? ")
    goal = {
        "title": title,
        "status": "Not Started"
    }
    goals.append(goal)
    save_goals(goals)
    print("✅ Goal added successfully!")

# View all goals
def view_goals(goals):
    print("\n--- Your Goals ---")
    if not goals:
        print("You have no goals yet. Start by adding one.")
    else:
        for index, goal in enumerate(goals, start=1):
            print(f"{index}. {goal['title']} - [{goal['status']}]")

# Update goal progress
def update_goal(goals):
    view_goals(goals)
    if not goals:
        return  # Skip if no goals

    try:
        choice = int(input("Enter the number of the goal to update: "))
        if 1 <= choice <= len(goals):
            print("Choose new status:")
            print("1. Not Started")
            print("2. In Progress")
            print("3. Completed")
            status_choice = input("Enter your choice (1-3): ")

            status_map = {
                "1": "Not Started",
                "2": "In Progress",
                "3": "Completed"
            }

            if status_choice in status_map:
                goals[choice - 1]["status"] = status_map[status_choice]
                save_goals(goals)
                print("✅ Goal updated!")
            else:
                print("❌ Invalid status choice.")
        else:
            print("❌ Invalid goal number.")
    except ValueError:
        print("❌ Please enter a valid number.")

# Show motivational quote
def show_quote():
    quotes = [
        "Keep going, you're doing great! 💪",
        "Every line of code is a step closer to your dreams. ✨",
        "Your future in tech is bright! 🚀",
        "Believe in your code, believe in yourself. 🌱"
    ]
    import random
    print("\n💬 Motivation: " + random.choice(quotes))

# Main menu loop
def main():
    print("🎯 Welcome to the Goal Tracker App!\n")
    show_quote()
    goals = load_goals()

    while True:
        print("\n--- Menu ---")
        print("1. Add a new goal")
        print("2. View goals")
        print("3. Update goal progress")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_goal(goals)
        elif choice == "2":
            view_goals(goals)
        elif choice == "3":
            update_goal(goals)
        elif choice == "4":
            print("Goodbye! Stay focused and keep coding! 😊")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

# Run the program
if __name__ == "__main__":
    main()
