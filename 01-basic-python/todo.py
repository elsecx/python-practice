todos = [
    {"task": "Contoh", "done": True}
]

def tampilkan_menu():
    print("\nPilih Menu:")
    print("1. Tambah todo")
    print("2. Tampilkan semua todo")
    print("3. Tandai todo sebagai selesai")
    print("4. Hapus todo")
    print("0. Keluar")

def tambah_todo(todo):
    todos.append({"task": todo, "done": False})
    print("✅ Todo berhasil ditambahkan!")
    tampilkan_todos()

def tampilkan_todos():
    if not todos:
        print("Belum ada task.")
        return
    
    for i, todo in enumerate(todos, start=1):
        if todo["done"]:
            print(f"{i}. [x] {todo['task']}")
        else:
            print(f"{i}. [ ] {todo['task']}")

def checklist_todo(num):
    i = num - 1

    if i < 0 or i >= len(todos):
        print("Index tidak valid. Silakan masukkan nomor yang sesuai.")
        return
    else:
        todo = todos[i]
        if todo["done"]:
            print("Task tersebut sudah selesai")
            return

        todo["done"] = True
        print(f"Task: {todo['task']}\nberhasil ditandai selesai.")
        tampilkan_todos()

def hapus_todo(num):
    i = num - 1

    if i < 0 or i >= len(todos):
        print("Index tidak valid. Silakan masukkan nomor yang sesuai.")
        return
    else:
        del todos[i]
        print("Todo berhasil dihapus!")
        tampilkan_todos()

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        todo = input("Masukkan todo: ")
        tambah_todo(todo)
    elif pilihan == "2":
        tampilkan_todos()
    elif pilihan == "3":
        tampilkan_todos()
        try:
            num = int(input("Masukkan nomor todo: "))
            checklist_todo(num)
        except ValueError:
            print("❌ Masukkan harus berupa angka.")
    elif pilihan == "4":
        tampilkan_todos()
        try:
            num = int(input("Masukkan nomor todo: "))
            hapus_todo(num)
        except ValueError:
            print("❌ Masukkan harus berupa angka.")
    elif pilihan == "0":
        break
    else:
        print("❌ Pilihan tidak valid. Silakan coba lagi.")