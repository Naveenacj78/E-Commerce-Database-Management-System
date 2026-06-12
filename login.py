from tkinter import *
from tkinter import messagebox
from database import connect_db

root = Tk()

root.title("E-Commerce Management System")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="white")

# ==========================
# TITLE
# ==========================

title = Label(
    root,
    text="E-Commerce Management System",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="#2c3e50"
)

title.pack(pady=30)

# ==========================
# USERNAME
# ==========================

Label(
    root,
    text="Username",
    font=("Arial", 12),
    bg="white"
).pack()

username = Entry(
    root,
    width=30,
    font=("Arial", 12)
)

username.pack(pady=5)

# ==========================
# PASSWORD
# ==========================

Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="white"
).pack()

password = Entry(
    root,
    show="*",
    width=30,
    font=("Arial", 12)
)

password.pack(pady=5)

# ==========================
# LOGIN FUNCTION
# ==========================

def login():

    user = username.get().strip()
    pwd = password.get().strip()

    if user == "" or pwd == "":

        messagebox.showerror(
            "Error",
            "Please Enter Username and Password"
        )

        return

    try:

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Admins
            WHERE username=%s
            AND password=%s
            """,
            (
                user,
                pwd
            )
        )

        result = cursor.fetchone()

        conn.close()

        if result:

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            root.destroy()

            import main

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Username or Password"
            )

    except Exception as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )

# ==========================
# BUTTONS
# ==========================

Button(
    root,
    text="Login",
    width=20,
    bg="green",
    fg="white",
    font=("Arial", 11, "bold"),
    command=login
).pack(pady=20)

Button(
    root,
    text="Exit",
    width=20,
    bg="red",
    fg="white",
    font=("Arial", 11, "bold"),
    command=root.destroy
).pack()

# ==========================
# FOOTER
# ==========================

Label(
    root,
    text="Default Login : admin / admin123",
    bg="white",
    fg="gray"
).pack(side=BOTTOM, pady=15)

root.mainloop()