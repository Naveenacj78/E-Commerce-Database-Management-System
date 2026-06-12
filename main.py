from tkinter import *
from tkinter import messagebox
from dashboard import dashboard_page
from customers import customer_page
from products import product_page
from orders import order_page
from reports import report_page

from dashboard import dashboard_page
from customers import customer_page
from products import product_page
from orders import order_page
from reports import report_page

root = Tk()

root.title("E-Commerce Management System")
root.geometry("1400x800")
root.configure(bg="white")

# ==================================
# MAIN LAYOUT
# ==================================

sidebar = Frame(
    root,
    bg="#2c3e50",
    width=220
)

sidebar.pack(
    side=LEFT,
    fill=Y
)

content = Frame(
    root,
    bg="white"
)

content.pack(
    side=RIGHT,
    fill=BOTH,
    expand=True
)

# ==================================
# PAGE LOADER
# ==================================

def clear_content():

    for widget in content.winfo_children():
        widget.destroy()

# ==================================
# DASHBOARD
# ==================================

def show_dashboard():

    clear_content()

    page = dashboard_page(content)

    page.pack(
        fill=BOTH,
        expand=True
    )

# ==================================
# CUSTOMERS
# ==================================

def show_customers():

    clear_content()

    page = customer_page(content)

    page.pack(
        fill=BOTH,
        expand=True
    )

# ==================================
# PRODUCTS
# ==================================

def show_products():

    clear_content()

    page = product_page(content)

    page.pack(
        fill=BOTH,
        expand=True
    )

# ==================================
# ORDERS
# ==================================

def show_orders():

    clear_content()

    page = order_page(content)

    page.pack(
        fill=BOTH,
        expand=True
    )

# ==================================
# REPORTS
# ==================================

def show_reports():

    clear_content()

    page = report_page(content)

    page.pack(
        fill=BOTH,
        expand=True
    )

# ==================================
# LOGOUT
# ==================================

def logout():

    answer = messagebox.askyesno(
        "Logout",
        "Do you want to logout?"
    )

    if answer:
        root.destroy()

# ==================================
# SIDEBAR TITLE
# ==================================

Label(
    sidebar,
    text="E-Commerce\nSystem",
    bg="#2c3e50",
    fg="white",
    font=("Arial",18,"bold")
).pack(
    pady=20
)

# ==================================
# MENU BUTTONS
# ==================================

Button(
    sidebar,
    text="Dashboard",
    width=20,
    command=show_dashboard
).pack(
    pady=5
)

Button(
    sidebar,
    text="Customers",
    width=20,
    command=show_customers
).pack(
    pady=5
)

Button(
    sidebar,
    text="Products",
    width=20,
    command=show_products
).pack(
    pady=5
)

Button(
    sidebar,
    text="Orders",
    width=20,
    command=show_orders
).pack(
    pady=5
)

Button(
    sidebar,
    text="Reports",
    width=20,
    command=show_reports
).pack(
    pady=5
)

Button(
    sidebar,
    text="Logout",
    width=20,
    command=logout
).pack(
    pady=20
)

# ==================================
# DEFAULT PAGE
# ==================================

show_dashboard()

root.mainloop()