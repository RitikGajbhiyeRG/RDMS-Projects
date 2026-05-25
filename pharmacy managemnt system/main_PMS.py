import mysql.connector as a

# Database connection
con = a.connect(
    host='localhost',
    user='root',          # change if needed
    password='12345',     # change if needed
    database='PMS'
)

# ================= ADD =================
def Add():
    cur = con.cursor()
    ref = int(input('Enter drug number: '))
    name = input('Enter drug name: ')
    manuftr = input('Enter manufacturer name: ')
    manuftr_date = input('Enter manufacturing date (YYYY-MM-DD): ')
    exp_date = input('Enter expiry date (YYYY-MM-DD): ')
    quantity = int(input('Enter quantity: '))
    category = input('Enter category: ')
    unitpr = int(input('Enter unit price: '))
    totalpr = int(input('Enter total price: '))

    val = (ref, name, manuftr, manuftr_date, exp_date, quantity, category, unitpr, totalpr)
    query = 'INSERT INTO INVENTORY VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'

    cur.execute(query, val)
    con.commit()

    print("✅ Details Added Successfully")
    input("Press ENTER to continue...")
    main()


# ================= DELETE =================
def delete():
    cur = con.cursor()
    ref = int(input('Enter drug number to delete: '))

    query = 'DELETE FROM INVENTORY WHERE ref_num = %s'
    cur.execute(query, (ref,))
    con.commit()

    print("✅ Details Deleted Successfully")
    input("Press ENTER to continue...")
    main()


# ================= UPDATE =================
def update():
    cur = con.cursor()

    print("1. Drug Name")
    print("2. Quantity")
    print("3. Unit Price")
    print("4. Total Price")

    ch = int(input("Enter choice: "))

    if ch == 1:
        val = input("Enter new drug name: ")
        ref = int(input("Enter ref number: "))
        cur.execute('UPDATE INVENTORY SET DrugName=%s WHERE ref_num=%s', (val, ref))

    elif ch == 2:
        val = int(input("Enter new quantity: "))
        ref = int(input("Enter ref number: "))
        cur.execute('UPDATE INVENTORY SET Quantity=%s WHERE ref_num=%s', (val, ref))

    elif ch == 3:
        val = int(input("Enter new unit price: "))
        ref = int(input("Enter ref number: "))
        cur.execute('UPDATE INVENTORY SET Unit_pr=%s WHERE ref_num=%s', (val, ref))

    elif ch == 4:
        val = int(input("Enter new total price: "))
        ref = int(input("Enter ref number: "))
        cur.execute('UPDATE INVENTORY SET Total_pr=%s WHERE ref_num=%s', (val, ref))

    else:
        print("Invalid choice")

    con.commit()
    print("✅ Updated Successfully")
    input("Press ENTER...")
    main()


# ================= SHOW ALL =================
def showall():
    cur = con.cursor()
    cur.execute('SELECT * FROM INVENTORY')
    data = cur.fetchall()

    for i in data:
        print("\nRef:", i[0])
        print("Drug:", i[1])
        print("Manufacturer:", i[2])
        print("MFG Date:", i[3])
        print("Expiry:", i[4])
        print("Quantity:", i[5])
        print("Category:", i[6])
        print("Unit Price:", i[7])
        print("Total Price:", i[8])

    input("\nPress ENTER...")
    main()


# ================= EXPIRED =================
def expired():
    cur = con.cursor()
    query = 'SELECT * FROM INVENTORY WHERE Expiry_date < CURDATE()'
    cur.execute(query)
    data = cur.fetchall()

    print("\n⚠ Expired Medicines:\n")

    for i in data:
        print("Drug:", i[1], "| Expiry:", i[4])

    input("\nPress ENTER...")
    main()


# ================= MAIN =================
def main():
    print("\n===== PHARMACY MANAGEMENT SYSTEM =====")
    print("1. Add drug")
    print("2. Delete drug")
    print("3. Update")
    print("4. Show expired")
    print("5. Show inventory")

    ch = int(input("Enter choice: "))

    if ch == 1:
        Add()
    elif ch == 2:
        delete()
    elif ch == 3:
        update()
    elif ch == 4:
        expired()
    elif ch == 5:
        showall()
    else:
        print("Invalid choice")
        main()


# Start program
main()