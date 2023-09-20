###########################################
#
# Welcome to the glorious and definitely not copied ChatGPT code for this uhhh idk productivity code
# We are just going to be typing and revising and doing whatever we want on this freaking thing and see what happens
#
###########################################

# Dictionaries
notes = {}
tasks = {}

###########################################

# Functions
# Note | Add
def add_note(title, content):
    notes[title] = content
    print(f"Note '{title}' added.")

# Note | View
def view_note(title):
    if title in notes:
        print(f"Title: {title}\nContent: {notes[title]}")
    else:
        print("Note not found.")

# Note | Display List
def list_notes():
    if notes:
        print("Available Notes:")
        for title in notes:
            print(f"- {title}")
    else:
        print("No notes available.")

# Note | Delete
def delete_note(title):
    if title in notes:
        del notes[title]
        print(f"Note '{title}' deleted.")
    else:
        print("Note not found.")

# Task | Add
def add_task(task):
    tasks[task] = False
    print(f"Task '{task}' added to the list.")

# Task | Display
def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, (task, completed) in enumerate(tasks.items(), start=1):
            status = "Done" if completed else "Not Done"
            print(f"{i}. {task} - {status}")
    else:
        print("Your To-Do List is empty.")

# Task | Done
def mark_done(task):
    if task in tasks:
        tasks[task] = True
        print(f"Task '{task}' marked as done.")
    else:
        print("Task not found in the list.")

# Task | Removal
def remove_task(task):
    if task in tasks:
        del tasks[task]
        print(f"Task '{task}' removed from the list.")
    else:
        print("Task not found in the list.")

###########################################

# Program Introduction
print("**********************")
print("  Welcome to UnifyIQ")
print("**********************")

###########################################

# Main Program Loop
while True:
    print("\nOptions:")
    print("1. Add a new note")
    print("2. View a note")
    print("3. List all notes")
    print("4. Delete a note")
    print("5. Add a task")
    print("6. Display tasks")
    print("7. Mark a task as done")
    print("8. Remove a task")
    print("9. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter the note title: ")
        content = input("Enter the note content: ")
        add_note(title, content)
    elif choice == "2":
        title = input("Enter the title of the note to view: ")
        view_note(title)
    elif choice == "3":
        list_notes()
    elif choice == "4":
        title = input("Enter the title of the note to delete: ")
        delete_note(title)
    elif choice == "5":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "6":
        display_tasks()
    elif choice == "7":
        task = input("Enter the task to mark as done: ")
        mark_done(task)
    elif choice == "8":
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == "9":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")

###########################################
