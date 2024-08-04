from tkinter import messagebox


def insert_person(people):
    f_name = input("name: ")
    l_name = input("family: ")
    age = input("age: ")
    if not f_name and not l_name and not age:
        messagebox.showinfo(
            "erorr", "اطلاعات را باید به طور کامل و صحیح وارد کنید!!!")
        insert_person(people)
    if not age.isdigit():
        messagebox.showinfo(
            "erorr", "در داده های عددی مثل (سن) باید عدد وارد شود !!!")
        insert_person(people)

    person_id = len(people) + 1
    people[person_id] = {
        "name": f_name,
        "family": l_name,
        "age": age
    }
    print(f"{f_name} {l_name} comleted.")


def remove_person(people):
    person_id = int(input("who remove? select id: "))

    if person_id in people:
        del people[person_id]
        print("remove compelted.")
    else:
        messagebox.showinfo("erorr", "شناسه انتخواب شده معتبر نیست !!!")
        remove_person(people)


def update_person(people):
    person_id = int(input("who update: "))

    if person_id in people:
        f_name = input("new name : ")
        l_name = input("new family : ")
        age = input("new age : ")

        people[person_id] = {
            "name": f_name,
            "family": l_name,
            "age": age
        }
        print("update complated.")
    else:
        messagebox.showinfo("erorr", "شناسه انتخواب شده معتبر نیست !!!")
        update_person(people)


people = {}

while True:
    print("\nWhat action do you want to take?")
    print("i - (Insert)")
    print("r -  (Remove)")
    print("u -  (Update)")
    print("s - (show)")
    print("q -  (Quit)")

    choice = input("chouse: ").lower()
    if choice != 'i' and choice != 'r' and choice != 'u' and choice != 's' and choice != 'q':
        messagebox.showinfo("erorr", "درخواست شما معتبر نیست!!!")
        continue

    if choice == 'i':
        insert_person(people)
    elif choice == 'r':
        remove_person(people)
    elif choice == 'u':
        update_person(people)
    elif choice == 's':
        if not people:
            messagebox.showinfo("erorr", "هیچی داخل منو وجود ندارد!!!")
            continue
        for person_id, person_info in people.items():
            print(
                f" id: {person_id}\n full name:{person_info['name']} {person_info['family']}\n age: {person_info['age']}")

    elif choice == 'q':
        print("byby!!")
        break
