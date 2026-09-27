# Midterm Practical Exam - Pet Adoption Records Manager
# Student: Bondoc, Julien Mark T.


def display_menu():
    print("\nPet Adoption Records")
    print("1. Add a pet")
    print("2. View all pets")
    print("3. Count available vs adopted")
    print("4. Find a pet by name")
    print("5. Remove a pet by name")
    print("6. Exit")
    choice = input("Choose an option: ").strip()
    return choice


def add_pet(pet_list):
    name = input("Enter pet name: ").strip()
    animal_type = input("Enter animal type (e.g., Dog, Cat): ").strip()
    status = input("Enter status (Available / Adopted): ").strip()
    record = f"{name} - {animal_type} - {status}"
    pet_list.append(record)
    print("Pet record added successfully!")


def view_pets(pet_list):
    if not pet_list:
        print("\nNo pet records found.")
        return
    print("\n--- Pet Records ---")
    for pet in pet_list:
        print(pet)


def count_available_adopted(pet_list):
    if not pet_list:
        print("\nNo pet records available.")
        return 0, 0
    available = 0
    adopted = 0
    for pet in pet_list:
        if "Available" in pet:
            available += 1
        elif "Adopted" in pet:
            adopted += 1
    print(f"\nAvailable: {available} | Adopted: {adopted}")
    return available, adopted


def find_pet(pet_list):
    if not pet_list:
        print("\nNo pet records to search.")
        return

    search_name = input("Enter pet name to search: ").strip().lower()
    found = False

    for pet in pet_list:
        pet_name = pet.split(" - ")[0].strip().lower()
        if pet_name == search_name:
            print(f"Found match: {pet}")
            found = True

    if not found:
        print("Pet not found.")


def remove_pet(pet_list):
    if not pet_list:
        print("\nNo pet records to remove.")
        return

    target_name = input("Enter pet name to remove: ").strip().lower()

    for pet in pet_list:
        pet_name = pet.split(" - ")[0].strip().lower()
        if pet_name == target_name:
            pet_list.remove(pet)
            print(f"Removed: {pet}")
            return

    print("Pet not found.")


def main():
    pets = []
    running = True

    while running:
        choice = display_menu()

        if choice == "1":
            add_pet(pets)
        elif choice == "2":
            view_pets(pets)
        elif choice == "3":
            count_available_adopted(pets)
        elif choice == "4":
            find_pet(pets)
        elif choice == "5":
            remove_pet(pets)
        elif choice == "6":
            print("\nExiting program. Goodbye!")
            running = False
        else:
            print("\nInvalid option, please try again.")


if __name__ == "__main__":
    main()
