import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# =========================================================
# COLOURS - SAME AS LOGIN.PY
# =========================================================

NAVY = "#102F50"
BLUE = "#087CF0"
WHITE = "#FFFFFF"

LIGHT_BLUE = "#EAF4FC"
INPUT_BG = "#F9FCFF"
BORDER = "#D8E8F5"
GRAY = "#6B7C93"

RED = "#F52F3E"


# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect("tourism.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tourists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    passport TEXT NOT NULL,
    arrival TEXT NOT NULL,
    departure TEXT,
    accommodation TEXT NOT NULL,
    destination TEXT NOT NULL,
    purpose TEXT NOT NULL,
    contact TEXT,
    email TEXT,
    transport TEXT,
    agency TEXT,
    people INTEGER
)
""")

conn.commit()


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("Tourism Record Keeping System")
root.geometry("1100x700")
root.resizable(False, False)
root.configure(bg=LIGHT_BLUE)


# =========================================================
# PAGE TITLE
# =========================================================

tk.Label(
    root,
    text="7. Update / Delete Record",
    font=("Arial", 22, "bold"),
    bg=LIGHT_BLUE,
    fg=NAVY
).place(
    x=30,
    y=25
)


# =========================================================
# SEARCH AREA
# =========================================================

tk.Label(
    root,
    text="Search Tourist Name",
    font=("Arial", 10, "bold"),
    bg=LIGHT_BLUE,
    fg=NAVY
).place(
    x=700,
    y=35
)


search_var = tk.StringVar()


search_entry = tk.Entry(
    root,
    textvariable=search_var,
    font=("Arial", 10),
    bg=WHITE,
    fg=NAVY,
    relief="solid",
    bd=1
)

search_entry.place(
    x=850,
    y=30,
    width=210,
    height=32
)


# =========================================================
# SEARCH RESULTS
# =========================================================

search_list = tk.Listbox(
    root,
    font=("Arial", 9),
    bg=WHITE,
    fg=NAVY,
    relief="solid",
    bd=1,
    height=4
)


# =========================================================
# EDIT TOURIST CARD
# =========================================================

edit_card = tk.Frame(
    root,
    bg=WHITE,
    width=650,
    height=465,
    highlightbackground=BORDER,
    highlightthickness=1
)

edit_card.place(
    x=20,
    y=90
)

edit_card.pack_propagate(False)


# =========================================================
# EDIT HEADER
# =========================================================

edit_header = tk.Frame(
    edit_card,
    bg=WHITE,
    height=55
)

edit_header.pack(
    fill="x"
)


# Icon circle

tk.Label(
    edit_header,
    text="●",
    font=("Arial", 20),
    bg="#EAF4FC",
    fg=NAVY,
    width=3
).pack(
    side="left",
    padx=(15, 8),
    pady=8
)


tk.Label(
    edit_header,
    text="Edit Tourist",
    font=("Arial", 17, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(
    side="left"
)


# =========================================================
# FORM AREA
# =========================================================

form = tk.Frame(
    edit_card,
    bg=WHITE
)

form.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=5
)


# =========================================================
# VARIABLES
# =========================================================

name_var = tk.StringVar()
country_var = tk.StringVar()
passport_var = tk.StringVar()
arrival_var = tk.StringVar()
accommodation_var = tk.StringVar()
destination_var = tk.StringVar()
purpose_var = tk.StringVar()


# =========================================================
# FIELD FUNCTION
# =========================================================

def create_label(parent, text, x, y):

    tk.Label(
        parent,
        text=text,
        font=("Arial", 9, "bold"),
        bg=WHITE,
        fg=NAVY
    ).place(
        x=x,
        y=y
    )


def create_entry(parent, variable, x, y, width=205):

    entry = tk.Entry(
        parent,
        textvariable=variable,
        font=("Arial", 10),
        bg=INPUT_BG,
        fg=NAVY,
        relief="solid",
        bd=1
    )

    entry.place(
        x=x,
        y=y,
        width=width,
        height=34
    )

    return entry


# =========================================================
# FULL NAME
# =========================================================

create_label(
    form,
    "Full Name *",
    0,
    5
)

name_entry = create_entry(
    form,
    name_var,
    0,
    28,
    205
)


# =========================================================
# COUNTRY
# =========================================================

create_label(
    form,
    "Country *",
    230,
    5
)

country_entry = create_entry(
    form,
    country_var,
    230,
    28,
    205
)


# =========================================================
# PASSPORT
# =========================================================

create_label(
    form,
    "Passport Number *",
    0,
    85
)

passport_entry = create_entry(
    form,
    passport_var,
    0,
    108,
    205
)


# =========================================================
# ARRIVAL DATE
# =========================================================

create_label(
    form,
    "Arrival Date *",
    230,
    85
)

arrival_entry = create_entry(
    form,
    arrival_var,
    230,
    108,
    205
)


# =========================================================
# ACCOMMODATION
# =========================================================

create_label(
    form,
    "Accommodation *",
    0,
    165
)

accommodation_entry = create_entry(
    form,
    accommodation_var,
    0,
    188,
    205
)


# =========================================================
# DESTINATION
# =========================================================

create_label(
    form,
    "Destination *",
    230,
    165
)

destination_entry = create_entry(
    form,
    destination_var,
    230,
    188,
    205
)


# =========================================================
# PURPOSE OF VISIT
# =========================================================

create_label(
    form,
    "Purpose of Visit *",
    0,
    245
)

purpose_entry = create_entry(
    form,
    purpose_var,
    0,
    268,
    205
)


# =========================================================
# STORE SELECTED RECORD ID
# =========================================================

selected_id = tk.IntVar(value=0)


# =========================================================
# SEARCH TOURIST
# =========================================================

def search_tourist(*args):

    search_list.delete(
        0,
        tk.END
    )

    search_text = search_var.get().strip()

    if search_text == "":

        search_list.place_forget()

        return


    cursor.execute("""
    SELECT id, name, country
    FROM tourists
    WHERE name LIKE ?
    ORDER BY name
    """, (
        "%" + search_text + "%",
    ))

    results = cursor.fetchall()


    if results:

        for record in results:

            search_list.insert(
                tk.END,
                f"{record[0]} | {record[1]} | {record[2]}"
            )

        search_list.place(
            x=850,
            y=63,
            width=210
        )

    else:

        search_list.place_forget()


search_var.trace_add(
    "write",
    search_tourist
)


# =========================================================
# SELECT SEARCH RESULT
# =========================================================

def select_tourist(event=None):

    selection = search_list.curselection()

    if not selection:
        return


    selected_text = search_list.get(
        selection[0]
    )


    record_id = selected_text.split("|")[0].strip()


    cursor.execute("""
    SELECT *
    FROM tourists
    WHERE id = ?
    """, (
        record_id,
    ))

    record = cursor.fetchone()


    if record:

        selected_id.set(
            record[0]
        )

        name_var.set(
            record[1]
        )

        country_var.set(
            record[2]
        )

        passport_var.set(
            record[3]
        )

        arrival_var.set(
            record[4]
        )

        accommodation_var.set(
            record[6]
        )

        destination_var.set(
            record[7]
        )

        purpose_var.set(
            record[8]
        )


        # Update delete confirmation

        delete_name_label.config(
            text=f"{record[1]}  |  {record[2]}"
        )


    search_list.place_forget()

    search_var.set(
        record[1]
    )


search_list.bind(
    "<ButtonRelease-1>",
    select_tourist
)


# =========================================================
# UPDATE FUNCTION
# =========================================================

def update_record():

    record_id = selected_id.get()


    if record_id == 0:

        messagebox.showwarning(
            "No Tourist Selected",
            "Please search and select a tourist first."
        )

        return


    name = name_var.get().strip()
    country = country_var.get().strip()
    passport = passport_var.get().strip()
    arrival = arrival_var.get().strip()
    accommodation = accommodation_var.get().strip()
    destination = destination_var.get().strip()
    purpose = purpose_var.get().strip()


    # -----------------------------------------------------
    # REQUIRED FIELDS
    # -----------------------------------------------------

    if not name:

        messagebox.showwarning(
            "Required Field",
            "Please enter the full name."
        )

        return


    if not country:

        messagebox.showwarning(
            "Required Field",
            "Please enter the country."
        )

        return


    if not passport:

        messagebox.showwarning(
            "Required Field",
            "Please enter the passport number."
        )

        return


    if not arrival:

        messagebox.showwarning(
            "Required Field",
            "Please enter the arrival date."
        )

        return


    if not accommodation:

        messagebox.showwarning(
            "Required Field",
            "Please enter the accommodation."
        )

        return


    if not destination:

        messagebox.showwarning(
            "Required Field",
            "Please enter the destination."
        )

        return


    if not purpose:

        messagebox.showwarning(
            "Required Field",
            "Please enter the purpose of visit."
        )

        return


    # -----------------------------------------------------
    # UPDATE DATABASE
    # -----------------------------------------------------

    cursor.execute("""
    UPDATE tourists

    SET
        name = ?,
        country = ?,
        passport = ?,
        arrival = ?,
        accommodation = ?,
        destination = ?,
        purpose = ?

    WHERE id = ?
    """, (
        name,
        country,
        passport,
        arrival,
        accommodation,
        destination,
        purpose,
        record_id
    ))


    conn.commit()


    messagebox.showinfo(
        "Update Successful",
        "Tourist record has been updated successfully."
    )


    delete_name_label.config(
        text=f"{name}  |  {country}"
    )


# =========================================================
# CANCEL EDIT
# =========================================================

def cancel_edit():

    selected_id.set(0)

    name_var.set("")
    country_var.set("")
    passport_var.set("")
    arrival_var.set("")
    accommodation_var.set("")
    destination_var.set("")
    purpose_var.set("")

    search_var.set("")

    delete_name_label.config(
        text="No tourist selected"
    )


# =========================================================
# UPDATE BUTTON
# =========================================================

tk.Button(
    edit_card,
    text="Update",
    command=update_record,
    bg=BLUE,
    fg=WHITE,
    activebackground="#0668CE",
    activeforeground=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).place(
    x=440,
    y=410,
    width=120,
    height=38
)


# =========================================================
# CANCEL BUTTON
# =========================================================

tk.Button(
    edit_card,
    text="Cancel",
    command=cancel_edit,
    bg=WHITE,
    fg=NAVY,
    activebackground=LIGHT_BLUE,
    activeforeground=NAVY,
    font=("Arial", 10, "bold"),
    relief="solid",
    bd=1,
    cursor="hand2"
).place(
    x=305,
    y=410,
    width=120,
    height=38
)


# =========================================================
# DELETE CONFIRMATION CARD
# =========================================================

delete_card = tk.Frame(
    root,
    bg=WHITE,
    width=395,
    height=350,
    highlightbackground=BORDER,
    highlightthickness=1
)

delete_card.place(
    x=690,
    y=150
)

delete_card.pack_propagate(False)


# =========================================================
# DELETE TITLE
# =========================================================

tk.Label(
    delete_card,
    text="Delete Confirmation",
    font=("Arial", 17, "bold"),
    bg=WHITE,
    fg=NAVY
).pack(
    anchor="w",
    padx=18,
    pady=(18, 10)
)


# =========================================================
# INNER DELETE BOX
# =========================================================

delete_inner = tk.Frame(
    delete_card,
    bg=WHITE,
    highlightbackground=BORDER,
    highlightthickness=1
)

delete_inner.place(
    x=15,
    y=65,
    width=365,
    height=205
)


# =========================================================
# RED WARNING ICON
# =========================================================

tk.Label(
    delete_inner,
    text="!",
    font=("Arial", 20, "bold"),
    bg=RED,
    fg=WHITE,
    width=2,
    height=1
).pack(
    pady=(18, 5)
)


# =========================================================
# DELETE RECORD TEXT
# =========================================================

tk.Label(
    delete_inner,
    text="Delete Record",
    font=("Arial", 12, "bold"),
    bg=WHITE,
    fg=RED
).pack(
    pady=2
)


# =========================================================
# DELETE MESSAGE
# =========================================================

tk.Label(
    delete_inner,
    text="Are you sure you want to delete this tourist record?",
    font=("Arial", 9),
    bg=WHITE,
    fg=GRAY
).pack(
    pady=7
)


# =========================================================
# TOURIST NAME
# =========================================================

delete_name_label = tk.Label(
    delete_inner,
    text="No tourist selected",
    font=("Arial", 9, "bold"),
    bg=WHITE,
    fg=NAVY
)

delete_name_label.pack()


# =========================================================
# DELETE FUNCTION
# =========================================================

def delete_record():

    record_id = selected_id.get()


    if record_id == 0:

        messagebox.showwarning(
            "No Tourist Selected",
            "Please search and select a tourist first."
        )

        return


    name = name_var.get()
    country = country_var.get()


    answer = messagebox.askyesno(
        "Delete Confirmation",
        f"Are you sure you want to delete this tourist record?\n\n"
        f"{name} | {country}"
    )


    if answer:

        cursor.execute(
            "DELETE FROM tourists WHERE id = ?",
            (record_id,)
        )

        conn.commit()


        messagebox.showinfo(
            "Record Deleted",
            "Tourist record has been deleted successfully."
        )


        cancel_edit()


# =========================================================
# DELETE CANCEL BUTTON
# =========================================================

tk.Button(
    delete_card,
    text="Cancel",
    command=lambda: delete_name_label.config(
        text="Delete cancelled"
    ),
    bg=WHITE,
    fg=NAVY,
    activebackground=LIGHT_BLUE,
    activeforeground=NAVY,
    font=("Arial", 10, "bold"),
    relief="solid",
    bd=1,
    cursor="hand2"
).place(
    x=25,
    y=285,
    width=130,
    height=38
)


# =========================================================
# DELETE BUTTON
# =========================================================

tk.Button(
    delete_card,
    text="Delete",
    command=delete_record,
    bg=RED,
    fg=WHITE,
    activebackground="#D92332",
    activeforeground=WHITE,
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).place(
    x=170,
    y=285,
    width=150,
    height=38
)


# =========================================================
# CLOSE PROGRAM
# =========================================================

def close_program():

    conn.close()
    root.destroy()


root.protocol(
    "WM_DELETE_WINDOW",
    close_program
)


# =========================================================
# RUN
# =========================================================

root.mainloop()