''' List => To-do-list 
    tuple => Passport
    sets => guest_list '''

todo_list = ["Buy groceries", "Clean room", "Study Python", "Buy groceries"]
todo_list.append("Go to gym")  # ✅ Can add more items
todo_list.remove("Clean room") # ✅ Can remove items
print(todo_list)  # ['Buy groceries', 'Study Python', 'Buy groceries', 'Go to gym']

passport_info = ("John Doe", "01-01-2000", "USA")
# passport_info[1] = "02-02-2001" ❌ ERROR! Tuples can't be modified
print(passport_info)  # ('John Doe', '01-01-2000', 'USA')

guest_list = {"Alice", "Bob", "Charlie"}
guest_list.add("David")  # ✅ Can add guests
guest_list.add("Alice")  # ❌ Won't add again (no duplicates allowed)
guest_list.remove("Bob") # ✅ Can remove guests
print(guest_list)  # {'Alice', 'Charlie', 'David'}
