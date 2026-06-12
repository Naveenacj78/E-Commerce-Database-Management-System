from tkinter import *
from database import connect_db

def dashboard_page(parent):

    frame = Frame(parent,bg="white")

    # ==========================
    # FUNCTIONS
    # ==========================

    def get_total_customers():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM Customers"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_total_products():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM Products"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_total_orders():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM Orders"
        )

        count = cursor.fetchone()[0]

        conn.close()

        return count

    def get_total_revenue():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT IFNULL(
            SUM(total_amount),0)
            FROM Orders
            """
        )

        total = cursor.fetchone()[0]

        conn.close()

        return total

    def get_low_stock():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
            product_name,
            stock
            FROM Products
            WHERE stock < 10
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    def get_recent_orders():

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
            order_id,
            total_amount
            FROM Orders
            ORDER BY order_id DESC
            LIMIT 5
            """
        )

        rows = cursor.fetchall()

        conn.close()

        return rows

    # ==========================
    # TITLE
    # ==========================

    Label(
        frame,
        text="Dashboard",
        font=("Arial",24,"bold"),
        bg="white"
    ).pack(pady=20)

    # ==========================
    # CARDS
    # ==========================

    card_frame = Frame(
        frame,
        bg="white"
    )

    card_frame.pack(pady=20)

    def create_card(
        parent,
        title,
        value,
        color
    ):

        card = Frame(
            parent,
            bg=color,
            width=220,
            height=120
        )

        card.pack_propagate(False)

        Label(
            card,
            text=title,
            bg=color,
            fg="white",
            font=("Arial",14,"bold")
        ).pack(pady=10)

        Label(
            card,
            text=value,
            bg=color,
            fg="white",
            font=("Arial",24,"bold")
        ).pack()

        return card

    create_card(
        card_frame,
        "Customers",
        get_total_customers(),
        "#3498db"
    ).grid(
        row=0,
        column=0,
        padx=10
    )

    create_card(
        card_frame,
        "Products",
        get_total_products(),
        "#2ecc71"
    ).grid(
        row=0,
        column=1,
        padx=10
    )

    create_card(
        card_frame,
        "Orders",
        get_total_orders(),
        "#f39c12"
    ).grid(
        row=0,
        column=2,
        padx=10
    )

    create_card(
        card_frame,
        "Revenue",
        f"₹ {get_total_revenue()}",
        "#e74c3c"
    ).grid(
        row=0,
        column=3,
        padx=10
    )

    # ==========================
    # LOW STOCK
    # ==========================

    low_stock_frame = LabelFrame(
        frame,
        text="Low Stock Products",
        padx=10,
        pady=10
    )

    low_stock_frame.pack(
        fill=X,
        padx=20,
        pady=10
    )

    low_stock = get_low_stock()

    if low_stock:

        for item in low_stock:

            Label(
                low_stock_frame,
                text=f"{item[0]}  | Stock : {item[1]}",
                fg="red"
            ).pack(anchor="w")

    else:

        Label(
            low_stock_frame,
            text="No Low Stock Products"
        ).pack(anchor="w")

    # ==========================
    # RECENT ORDERS
    # ==========================

    recent_frame = LabelFrame(
        frame,
        text="Recent Orders",
        padx=10,
        pady=10
    )

    recent_frame.pack(
        fill=X,
        padx=20,
        pady=10
    )

    orders = get_recent_orders()

    if orders:

        for order in orders:

            Label(
                recent_frame,
                text=f"Order #{order[0]}   |   ₹ {order[1]}"
            ).pack(anchor="w")

    else:

        Label(
            recent_frame,
            text="No Orders Found"
        ).pack(anchor="w")

    return frame