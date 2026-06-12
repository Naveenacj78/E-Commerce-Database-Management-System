from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

def product_page(parent):

    frame = Frame(parent)

    product_id = StringVar()
    product_name = StringVar()
    category = StringVar()
    price = StringVar()
    stock = StringVar()

    def clear_fields():

        product_id.set("")
        product_name.set("")
        category.set("")
        price.set("")
        stock.set("")

    def load_products():

        for row in tree.get_children():
            tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Products
            """
        )

        rows = cursor.fetchall()

        for row in rows:

            tag = ""

            if int(row[4]) < 10:
                tag = "lowstock"

            tree.insert(
                "",
                END,
                values=row,
                tags=(tag,)
            )

        conn.close()

    def add_product():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Products
            (product_name,category,price,stock)
            VALUES(%s,%s,%s,%s)
            """,
            (
                product_name.get(),
                category.get(),
                price.get(),
                stock.get()
            )
        )

        conn.commit()
        conn.close()

        load_products()
        clear_fields()

        messagebox.showinfo(
            "Success",
            "Product Added"
        )

    def get_cursor(event):

        selected = tree.focus()

        values = tree.item(
            selected,
            "values"
        )

        if not values:
            return

        product_id.set(values[0])
        product_name.set(values[1])
        category.set(values[2])
        price.set(values[3])
        stock.set(values[4])

    def update_product():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Products
            SET
            product_name=%s,
            category=%s,
            price=%s,
            stock=%s
            WHERE product_id=%s
            """,
            (
                product_name.get(),
                category.get(),
                price.get(),
                stock.get(),
                product_id.get()
            )
        )

        conn.commit()
        conn.close()

        load_products()

        messagebox.showinfo(
            "Success",
            "Product Updated"
        )

    def delete_product():

        if product_id.get() == "":
            return

        answer = messagebox.askyesno(
            "Delete",
            "Delete Product?"
        )

        if answer:

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM Products
                WHERE product_id=%s
                """,
                (
                    product_id.get(),
                )
            )

            conn.commit()
            conn.close()

            load_products()
            clear_fields()

    def search_product():

        keyword = search_entry.get()

        for row in tree.get_children():
            tree.delete(row)

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Products
            WHERE product_name LIKE %s
            """,
            (
                "%" + keyword + "%",
            )
        )

        rows = cursor.fetchall()

        for row in rows:
            tree.insert("",END,values=row)

        conn.close()

    Label(
        frame,
        text="Product Management",
        font=("Arial",18,"bold")
    ).pack(pady=10)

    form = Frame(frame)
    form.pack()

    Label(form,text="Product Name").grid(row=0,column=0,padx=10,pady=5)

    Entry(
        form,
        textvariable=product_name,
        width=30
    ).grid(row=0,column=1)

    Label(form,text="Category").grid(row=1,column=0,padx=10,pady=5)

    Entry(
        form,
        textvariable=category,
        width=30
    ).grid(row=1,column=1)

    Label(form,text="Price").grid(row=2,column=0,padx=10,pady=5)

    Entry(
        form,
        textvariable=price,
        width=30
    ).grid(row=2,column=1)

    Label(form,text="Stock").grid(row=3,column=0,padx=10,pady=5)

    Entry(
        form,
        textvariable=stock,
        width=30
    ).grid(row=3,column=1)

    btn_frame = Frame(frame)
    btn_frame.pack(pady=10)

    Button(
        btn_frame,
        text="Add",
        width=12,
        command=add_product
    ).grid(row=0,column=0,padx=5)

    Button(
        btn_frame,
        text="Update",
        width=12,
        command=update_product
    ).grid(row=0,column=1,padx=5)

    Button(
        btn_frame,
        text="Delete",
        width=12,
        command=delete_product
    ).grid(row=0,column=2,padx=5)

    Button(
        btn_frame,
        text="Clear",
        width=12,
        command=clear_fields
    ).grid(row=0,column=3,padx=5)

    search_frame = Frame(frame)
    search_frame.pack()

    search_entry = Entry(
        search_frame,
        width=30
    )

    search_entry.pack(
        side=LEFT,
        padx=5
    )

    Button(
        search_frame,
        text="Search",
        command=search_product
    ).pack(side=LEFT)

    tree = ttk.Treeview(
        frame,
        columns=(
            "ID",
            "Name",
            "Category",
            "Price",
            "Stock"
        ),
        show="headings"
    )

    tree.heading("ID",text="ID")
    tree.heading("Name",text="Name")
    tree.heading("Category",text="Category")
    tree.heading("Price",text="Price")
    tree.heading("Stock",text="Stock")

    tree.tag_configure(
        "lowstock",
        background="lightcoral"
    )

    tree.pack(
        fill=BOTH,
        expand=True,
        pady=10
    )

    tree.bind(
        "<ButtonRelease-1>",
        get_cursor
    )

    load_products()

    return frame