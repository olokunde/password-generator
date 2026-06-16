import csv
import os

file_name = "job_applications.csv"

def add_application():
    company = input("Enter company name: ")
    job_title = input("Enter job title: ")
    platform = input("Enter platform (LinkedIn, Sprout, Upwork, etc): ")
    date_applied = input("Enter date applied (YYYY-MM-DD): ")
    status = input("Enter status (Applied, Interview, Rejected, Offer, No Reply): ")
    notes = input("Enter notes: ")

    file_exists = os.path.isfile(file_name)

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Company", "Job Title", "Platform", "Date Applied", "Status", "Notes"])

        writer.writerow([company, job_title, platform, date_applied, status, notes])

    print("Job application added successfully.")


def view_applications():
    if not os.path.isfile(file_name):
        print("No job applications found.")
        return

    with open(file_name, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def update_status():
    if not os.path.isfile(file_name):
        print("No job applications found.")
        return

    applications = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        applications = list(reader)

    if len(applications) <= 1:
        print("No applications to update.")
        return

    print("\nJob Applications:")
    for index, app in enumerate(applications[1:], start=1):
        print(f"{index}. {app[0]} - {app[1]} - Current Status: {app[4]}")

    try:
        choice = int(input("Enter the number of the application to update: "))
        if choice < 1 or choice >= len(applications):
            print("Invalid application number.")
            return

        new_status = input("Enter new status (Applied, Interview, Rejected, Offer, No Reply): ")
        applications[choice][4] = new_status

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(applications)

        print("Application status updated successfully.")

    except ValueError:
        print("Please enter a valid number.")


def delete_application():
    if not os.path.isfile(file_name):
        print("No job applications found.")
        return

    applications = []

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        applications = list(reader)

    if len(applications) <= 1:
        print("No applications to delete.")
        return

    print("\nJob Applications:")
    for index, app in enumerate(applications[1:], start=1):
        print(f"{index}. {app[0]} - {app[1]} - Status: {app[4]}")

    try:
        choice = int(input("Enter the number of the application to delete: "))
        if choice < 1 or choice >= len(applications):
            print("Invalid application number.")
            return

        removed = applications.pop(choice)

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(applications)

        print(f"Deleted application: {removed[0]} - {removed[1]}")

    except ValueError:
        print("Please enter a valid number.")


def view_summary():
    if not os.path.isfile(file_name):
        print("No job applications found.")
        return

    summary = {}

    with open(file_name, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            status = row["Status"]
            summary[status] = summary.get(status, 0) + 1

    print("\nApplication Summary:")
    for status, count in summary.items():
        print(f"{status}: {count}")


while True:
    print("\nJob Application Tracker")
    print("1. Add Job Application")
    print("2. View Applications")
    print("3. Update Application Status")
    print("4. Delete Application")
    print("5. View Application Summary")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        update_status()
    elif choice == "4":
        delete_application()
    elif choice == "5":
        view_summary()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")