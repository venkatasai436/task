import os
import sys

# --- DATA STORAGE (In-Memory) ---
# Tasks structure: {'id': int, 'title': str, 'done': bool}
tasks = []

# Habits structure: {'id': int, 'title': str, 'done_today': bool}
# Pre-populating with some common habits
habits = [
    {'id': 1, 'title': 'Drink 2L Water', 'done_today': False},
    {'id': 2, 'title': 'Exercise 15 mins', 'done_today': False},
    {'id': 3, 'title': 'Read a book', 'done_today': False}
]

def clear_screen():
    """Clears the console for a cleaner UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Prints a styled header."""
    print("\n" + "="*40)
    print(f" {title.center(36)} ")
    print("="*40)

# --- TASK FUNCTIONS ---

def add_task():
    print_header("ADD NEW TASK")
    title = input("Enter task description: ").strip()
    if title:
        new_id = len(tasks) + 1
        tasks.append({'id': new_id, 'title': title, 'done': False})
        print(f" Task '{title}' added!")
    else:
        print("  Task cannot be empty.")
    input("\nPress Enter to return...")

def view_tasks():
    print_header("YOUR TO-DO LIST")
    if not tasks:
        print("  (No tasks yet. Add one!)")
    else:
        for t in tasks:
            status = "[x]" if t['done'] else "[ ]"
            print(f"  {t['id']}. {status} {t['title']}")

def mark_task_done():
    view_tasks()
    if not tasks:
        input("\nPress Enter to return...")
        return

    try:
        task_id = int(input("\nEnter ID of task to complete: "))
        # Find task by ID (adjusting for list index 0 if IDs are sequential)
        # Doing a robust search instead of index assumption
        found = False
        for t in tasks:
            if t['id'] == task_id:
                t['done'] = True
                print(f"🎉 Great job! '{t['title']}' completed.")
                found = True
                break
        if not found:
            print(" Invalid ID.")
    except ValueError:
        print(" Please enter a valid number.")
    input("\nPress Enter to return...")

# --- HABIT FUNCTIONS ---

def track_habits():
    print_header("HABIT TRACKER")
    print("Which habit did you complete today?\n")
    
    for h in habits:
        status = " DONE" if h['done_today'] else "🌱 TODO"
        print(f"  {h['id']}. {status} : {h['title']}")
    
    print("\n  0. Return to Menu")
    
    try:
        choice = int(input("\nEnter Habit ID to toggle: "))
        if choice == 0:
            return
        
        found = False
        for h in habits:
            if h['id'] == choice:
                # Toggle the status
                h['done_today'] = not h['done_today'] 
                msg = "completed!" if h['done_today'] else "un-checked."
                print(f"👍 Habit marked as {msg}")
                found = True
                break
        if not found:
            print(" Invalid Habit ID.")
            
    except ValueError:
        print(" Please enter a number.")
    
    input("\nPress Enter to continue...")

# --- INSIGHT ENGINE ---

def get_insight():
    print_header(" DAILY WELLNESS INSIGHT")
    
    # Calculate metrics
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t['done'])
    total_habits = len(habits)
    completed_habits = sum(1 for h in habits if h['done_today'])
    
    # Calculate percentage (avoid division by zero)
    task_progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    habit_progress = (completed_habits / total_habits * 100) if total_habits > 0 else 0
    
    print(f" Stats: Tasks: {completed_tasks}/{total_tasks} | Habits: {completed_habits}/{total_habits}")
    print("-" * 40)
    
    # Logic for Insights
    if total_tasks == 0:
        print(" Insight: You have a clean slate. Plan your day to reduce anxiety!")
    elif task_progress == 100 and habit_progress == 100:
        print(" Insight: UNSTOPPABLE! You have mastered your day perfectly.")
    elif task_progress > 70 and habit_progress < 30:
        print(" Insight: You are working hard, but neglecting self-care.")
        print("   -> Take a break and drink some water.")
    elif task_progress < 30 and habit_progress > 70:
        print(" Insight: You are very zen today, but productivity is low.")
        print("   -> Try the '5 Minute Rule' to start one work task.")
    elif task_progress > 50:
        print(" Insight: Solid progress. Finish one more big task to feel great.")
    else:
        print(" Insight: Slow start? Pick the smallest task and just do that one.")
        
    input("\nPress Enter to return...")

# --- MAIN LOOP ---

def main():
    while True:
        clear_screen()
        print_header("SMART COMPANION v1.0")
        print("  1. 📝 Add New Task")
        print("  2. ✅ Mark Task Done")
        print("  3. 👀 View All Tasks")
        print("  4. 🌱 Track Habits")
        print("  5. 🧠 Get Daily Insight")
        print("  6. 🚪 Exit")
        print("="*40)
        
        choice = input("Select an option (1-6): ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_done()
        elif choice == '3':
            view_tasks()
            input("\nPress Enter to return...")
        elif choice == '4':
            track_habits()
        elif choice == '5':
            get_insight()
        elif choice == '6':
            print("\n Goodbye! Stay productive.")
            sys.exit()
        else:
            input("\n Invalid option. Press Enter to try again...")

if __name__ == "__main__":
    main()