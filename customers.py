from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

def customer_page(parent):

    frame = Frame(parent)

    # ==========================
    # VARIABLES
    # ==========================

    customer_id = StringVar()
    customer_name = StringVar()
    email = StringVar()
    phone = StringVar()
    city = StringVar()

    # ==========================
    # FUNCTIONS
    # ==========================

    def clear_fields():

        customer_id.set("")
        customer_name.set("")
        email.set("")
        phone.set("")
        city.set("")

    def load_data():

        for row in tree.get_children():
            tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Customers
            """
        )

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", END, values=row)

        conn.close()

    def add_customer():

        if customer_name.get() == "":
            messagebox.showerror(
                "Error",
                "Customer Name Required"
            )
            return

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Customers
            (customer_name,email,phone,city)
            VALUES (%s,%s,%s,%s)
            """,
            (
                customer_name.get(),
                email.get(),
                phone.get(),
                city.get()
            )
        )

        conn.commit()
        conn.close()

        load_data()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Customer Added Successfully"
        )

    def get_cursor(event):

        selected = tree.focus()

        values = tree.item(selected,"values")

        if not values:
            return

        customer_id.set(values[0])
        customer_name.set(values[1])
        email.set(values[2])
        phone.set(values[3])
        city.set(values[4])

    def update_customer():

        if customer_id.get() == "":
            return

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Customers
            SET
            customer_name=%s,
            email=%s,
            phone=%s,
            city=%s
            WHERE customer_id=%s
            """,
            (
                customer_name.get(),
                email.get(),
                phone.get(),
                city.get(),
                customer_id.get()
            )
        )

        conn.commit()
        conn.close()

        load_data()

        messagebox.showinfo(
            "Success",
            "Customer Updated"
        )

    def delete_customer():

        if customer_id.get() == "":
            return

        answer = messagebox.askyesno(
            "Delete",
            "Delete this customer?"
        )

        if answer:

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM Customers
                WHERE customer_id=%s
                """,
                (
                    customer_id.get(),
                )
            )

            conn.commit()
            conn.close()

            load_data()
            clear_fields()

    def search_customer():

        keyword = search_entry.get()

        for row in tree.get_children():
            tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Customers
            WHERE customer_name LIKE %s
            """,
            (
                "%" + keyword + "%",
            )
        )

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("", END, values=row)

        conn.close()

    # ==========================
    # TITLE
    # ==========================

    Label(
        frame,
        text="Customer Management",
        font=("Arial",18,"bold")
    ).pack(pady=10)

    # ==========================
    # FORM
    # ==========================

    form = Frame(frame)
    form.pack(pady=10)

    Label(form,text="Name").grid(row=0,column=0,padx=10,pady=5)
    Entry(
        form,
        textvariable=customer_name,
        width=30
    ).grid(row=0,column=1)

    Label(form,text="Email").grid(row=1,column=0,padx=10,pady=5)
    Entry(
        form,
        textvariable=email,
        width=30
    ).grid(row=1,column=1)

    Label(form,text="Phone").grid(row=2,column=0,padx=10,pady=5)
    Entry(
        form,
        textvariable=phone,
        width=30
    ).grid(row=2,column=1)

    Label(form,text="City").grid(row=3,column=0,padx=10,pady=5)
    Entry(
        form,
        textvariable=city,
        width=30
    ).grid(row=3,column=1)

    # ==========================
    # BUTTONS
    # ==========================

    btn_frame = Frame(frame)
    btn_frame.pack(pady=10)

    Button(
        btn_frame,
        text="Add",
        width=12,
        command=add_customer
    ).grid(row=0,column=0,padx=5)

    Button(
        btn_frame,
        text="Update",
        width=12,
        command=update_customer
    ).grid(row=0,column=1,padx=5)

    Button(
        btn_frame,
        text="Delete",
        width=12,
        command=delete_customer
    ).grid(row=0,column=2,padx=5)

    Button(
        btn_frame,
        text="Clear",
        width=12,
        command=clear_fields
    ).grid(row=0,column=3,padx=5)

    # ==========================
    # SEARCH
    # ==========================

    search_frame = Frame(frame)
    search_frame.pack()

    search_entry = Entry(
        search_frame,
        width=30
    )

    search_entry.pack(side=LEFT,padx=5)

    Button(
        search_frame,
        text="Search",
        command=search_customer
    ).pack(side=LEFT)

    # ==========================
    # TABLE
    # ==========================

    tree = ttk.Treeview(
        frame,
        columns=(
            "ID",
            "Name",
            "Email",
            "Phone",
            "City"
        ),
        show="headings"
    )

    tree.heading("ID",text="ID")
    tree.heading("Name",text="Name")
    tree.heading("Email",text="Email")
    tree.heading("Phone",text="Phone")
    tree.heading("City",text="City")

    tree.pack(
        fill=BOTH,
        expand=True,
        pady=10
    )

    tree.bind(
        "<ButtonRelease-1>",
        get_cursor
    )

    load_data()

    return frame