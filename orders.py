from tkinter import *
from tkinter import ttk, messagebox
from database import connect_db

def order_page(parent):

    frame = Frame(parent)

    customer_var = StringVar()
    product_var = StringVar()
    quantity_var = StringVar()
    total_var = StringVar()

    customer_map = {}
    product_map = {}

    # =====================================
    # LOAD CUSTOMERS
    # =====================================

    def load_customers():

        customer_combo["values"] = []

        conn = connect_db()

        if not conn:
            return

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT customer_id,
                   customer_name
            FROM Customers
            """
        )

        rows = cursor.fetchall()

        names = []

        customer_map.clear()

        for row in rows:

            customer_map[row[1]] = row[0]
            names.append(row[1])

        customer_combo["values"] = names

        conn.close()

    # =====================================
    # LOAD PRODUCTS
    # =====================================

    def load_products():

        product_combo["values"] = []

        conn = connect_db()

        if not conn:
            return

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT product_id,
                   product_name,
                   price,
                   stock
            FROM Products
            """
        )

        rows = cursor.fetchall()

        names = []

        product_map.clear()

        for row in rows:

            product_map[row[1]] = {
                "id": row[0],
                "price": float(row[2]),
                "stock": int(row[3])
            }

            names.append(row[1])

        product_combo["values"] = names

        conn.close()

    # =====================================
    # CALCULATE TOTAL
    # =====================================

    def calculate_total(event=None):

        try:

            product = product_var.get()

            if product not in product_map:
                total_var.set("")
                return

            qty = int(quantity_var.get())

            price = product_map[product]["price"]

            total = qty * price

            total_var.set(str(total))

        except:
            total_var.set("")

    # =====================================
    # PLACE ORDER
    # =====================================

    def place_order():

        try:

            customer = customer_var.get()
            product = product_var.get()

            if customer == "" or product == "":
                messagebox.showerror(
                    "Error",
                    "Please select customer and product"
                )
                return

            qty = int(quantity_var.get())

            if qty <= 0:
                messagebox.showerror(
                    "Error",
                    "Quantity must be greater than zero"
                )
                return

            customer_id = customer_map[customer]
            product_id = product_map[product]["id"]

            available_stock = product_map[product]["stock"]

            if qty > available_stock:

                messagebox.showerror(
                    "Stock Error",
                    f"Only {available_stock} items available"
                )

                return

            total = float(total_var.get())

            conn = connect_db()

            cursor = conn.cursor()

            # Insert Order

            cursor.execute(
                """
                INSERT INTO Orders
                (
                    customer_id,
                    product_id,
                    quantity,
                    total_amount
                )
                VALUES (%s,%s,%s,%s)
                """,
                (
                    customer_id,
                    product_id,
                    qty,
                    total
                )
            )

            # Reduce Stock

            cursor.execute(
                """
                UPDATE Products
                SET stock = stock - %s
                WHERE product_id = %s
                """,
                (
                    qty,
                    product_id
                )
            )

            conn.commit()
            conn.close()

            messagebox.showinfo(
                "Success",
                "Order Placed Successfully"
            )

            quantity_var.set("")
            total_var.set("")

            load_products()
            load_orders()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =====================================
    # LOAD ORDERS
    # =====================================

    def load_orders():

        for row in tree.get_children():
            tree.delete(row)

        conn = connect_db()

        if not conn:
            return

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
                o.order_id,
                c.customer_name,
                p.product_name,
                o.quantity,
                o.total_amount,
                o.order_date

            FROM Orders o

            JOIN Customers c
            ON o.customer_id = c.customer_id

            JOIN Products p
            ON o.product_id = p.product_id

            ORDER BY o.order_id DESC
            """
        )

        rows = cursor.fetchall()

        for row in rows:

            tree.insert(
                "",
                END,
                values=row
            )

        conn.close()

    # =====================================
    # TITLE
    # =====================================

    Label(
        frame,
        text="Order Management",
        font=("Arial",18,"bold")
    ).pack(pady=10)

    # =====================================
    # FORM
    # =====================================

    form = Frame(frame)
    form.pack(pady=10)

    Label(
        form,
        text="Customer"
    ).grid(row=0,column=0,padx=10,pady=5)

    customer_combo = ttk.Combobox(
        form,
        textvariable=customer_var,
        width=30,
        state="readonly"
    )

    customer_combo.grid(row=0,column=1)

    Label(
        form,
        text="Product"
    ).grid(row=1,column=0,padx=10,pady=5)

    product_combo = ttk.Combobox(
        form,
        textvariable=product_var,
        width=30,
        state="readonly"
    )

    product_combo.grid(row=1,column=1)

    product_combo.bind(
        "<<ComboboxSelected>>",
        calculate_total
    )

    Label(
        form,
        text="Quantity"
    ).grid(row=2,column=0,padx=10,pady=5)

    qty_entry = Entry(
        form,
        textvariable=quantity_var,
        width=33
    )

    qty_entry.grid(row=2,column=1)

    qty_entry.bind(
        "<KeyRelease>",
        calculate_total
    )

    Label(
        form,
        text="Total Amount"
    ).grid(row=3,column=0,padx=10,pady=5)

    Entry(
        form,
        textvariable=total_var,
        width=33,
        state="readonly"
    ).grid(row=3,column=1)

    Button(
        form,
        text="Place Order",
        bg="green",
        fg="white",
        width=20,
        command=place_order
    ).grid(
        row=4,
        column=1,
        pady=10
    )

    # =====================================
    # ORDER TABLE
    # =====================================

    tree = ttk.Treeview(
        frame,
        columns=(
            "ID",
            "Customer",
            "Product",
            "Quantity",
            "Total",
            "Date"
        ),
        show="headings"
    )

    tree.heading("ID", text="Order ID")
    tree.heading("Customer", text="Customer")
    tree.heading("Product", text="Product")
    tree.heading("Quantity", text="Quantity")
    tree.heading("Total", text="Total Amount")
    tree.heading("Date", text="Order Date")

    tree.column("ID", width=80)
    tree.column("Customer", width=150)
    tree.column("Product", width=150)
    tree.column("Quantity", width=100)
    tree.column("Total", width=120)
    tree.column("Date", width=180)

    tree.pack(
        fill=BOTH,
        expand=True,
        pady=10
    )

    load_customers()
    load_products()
    load_orders()

    return frame