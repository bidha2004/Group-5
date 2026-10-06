import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =========================
# COLOURS
# =========================

NAVY = "#102F50"
BLUE = "#087CF0"
WHITE = "#FFFFFF"

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("Tourism Record Keeping System")
root.geometry("1100x700")
root.resizable(False, False)

# =========================
# PARO TAKTSANG IMAGE
# =========================

# Make sure the image is in the SAME folder as login.py
image = Image.open("paro_taktsang.jpg")

# Resize image to window size
image = image.resize((1100, 700), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image)

background = tk.Label(
    root,
    image=background_image
)

background.place(
    x=0,
    y=0,
    width=1100,
    height=700
)

# Keep image reference
background.image = background_image


# =========================
# LEFT DARK PANEL
# =========================

left_panel = tk.Frame(
    root,
    bg=NAVY,
    width=480,
    height=700
)

left_panel.place(
    x=0,
    y=0
)

left_panel.pack_propagate(False)


# =========================
# TITLE
# =========================

tk.Label(
    left_panel,
    text="🏔",
    font=("Arial", 55),
    bg=NAVY,
    fg=WHITE
).pack(pady=(110, 10))


tk.Label(
    left_panel,
    text="Tourism Record\nKeeping System",
    font=("Arial", 27, "bold"),
    bg=NAVY,
    fg=WHITE,
    justify="center"
).pack()


tk.Label(
    left_panel,
    text="Explore  •  Record  •  Manage",
    font=("Arial", 12),
    bg=NAVY,
    fg="#D6E8FA"
).pack(pady=15)


tk.Label(
    left_panel,
    text="Your gateway to organized\nand efficient tourism management.",
    font=("Arial", 12, "italic"),
    bg=NAVY,
    fg=WHITE,
    justify="center"
).pack(pady=35)


# =========================
# LOGIN CARD
# =========================

login_card = tk.Frame(
    root,
    bg=WHITE,
    width=390,
    height=480
)

login_card.place(
    x=650,
    y=110
)

login_card.pack_propagate(False)


# =========================
# LOGIN TITLE
# =========================

tk.Label(
    login_card,
    text="Welcome Back!",
    font=("Arial", 24, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(pady=(55, 5))


tk.Label(
    login_card,
    text="Login to your account",
    font=("Arial", 11),
    bg=WHITE,
    fg="gray"
).pack()


# =========================
# USERNAME
# =========================

tk.Label(
    login_card,
    text="Username",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(
    anchor="w",
    padx=45,
    pady=(35, 5)
)


username_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    relief="solid",
    bd=1
)

username_entry.pack(
    padx=45,
    fill="x",
    ipady=9
)


# =========================
# PASSWORD
# =========================

tk.Label(
    login_card,
    text="Password",
    font=("Arial", 10, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(
    anchor="w",
    padx=45,
    pady=(20, 5)
)


password_entry = tk.Entry(
    login_card,
    font=("Arial", 12),
    show="*",
    relief="solid",
    bd=1
)

password_entry.pack(
    padx=45,
    fill="x",
    ipady=9
)


# =========================
# SHOW PASSWORD
# =========================

show_password = tk.BooleanVar()


def toggle_password():

    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


tk.Checkbutton(
    login_card,
    text="Show Password",
    variable=show_password,
    command=toggle_password,
    bg=WHITE,
    fg=NAVY,
    activebackground=WHITE
).pack(
    anchor="w",
    padx=45,
    pady=8
)


# =========================
# LOGIN FUNCTION
# =========================

def login():

    username = username_entry.get().strip()
    password = password_entry.get()

    if username == "admin" and password == "admin123":

        messagebox.showinfo(
            "Login Successful",
            "Welcome to Tourism Record Keeping System!"
        )

        root.destroy()

        import records

    else:

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )


# =========================
# LOGIN BUTTON
# =========================

tk.Button(
    login_card,
    text="Login",
    command=login,
    bg=BLUE,
    fg=WHITE,
    activebackground="#0668CE",
    activeforeground=WHITE,
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2"
).pack(
    padx=45,
    fill="x",
    pady=25,
    ipady=9
)


# =========================
# EXTRA TEXT
# =========================

tk.Label(
    login_card,
    text="Forgot Password?",
    font=("Arial", 9),
    bg=WHITE,
    fg=BLUE
).pack()


tk.Label(
    login_card,
    text="Tourism Record Management System",
    font=("Arial", 9),
    bg=WHITE,
    fg="gray"
).pack(pady=15)


# =========================
# ENTER KEY
# =========================

password_entry.bind(
    "<Return>",
    lambda event: login()
)

username_entry.focus()


# =========================
# RUN
# =========================

root.mainloop()