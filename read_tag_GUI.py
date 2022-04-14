from tkinter import *
from test_connection_db import read_card_uid, add_visit


# def read_user():
#     user_info = read_card_uid()
#     entrytext.set(user_info[2])

ZAID = 987654
TAYANE = 123456

def new_visit():
    add_visit(read_card_uid()[0], TAYANE)


# -------------------------------------------------------------
#                   INITIALIZATION
# -------------------------------------------------------------


WIDTH = 700
HEIGHT = 600

root = Tk()
root.title("READ CLIENT TAG")
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

# -------------------------------------------------------------
#                       FRAMES
# -------------------------------------------------------------

bg_frame = Frame(root, bg='red')
bg_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

holder_frame = Frame(root)
holder_frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

prompt_frame = Frame(holder_frame)
prompt_frame.place(relwidth=1, relx=0, relheight=0.3, rely=0)

labels_frame = Frame(prompt_frame)
labels_frame.place(relwidth=0.6, relx=0, relheight=1, rely=0)

entries_frame = Frame(prompt_frame)
entries_frame.place(relwidth=0.4, relx=0.6, relheight=1, rely=0)

# -------------------------------------------------------------
#                           GUI
# -------------------------------------------------------------

# # ==================== Labels ==================================
# folder_name_label = Label(labels_frame, text='Enter a name for the output folder :',
#                           fg='Black', font=('Helvetica', 15))
# folder_name_label.place(relx=0.1, rely=0.4)
#
# default_folder_name = Label(labels_frame, text='(Nb: The default folder name is set to: Output)',
#                             font=('Helvetica', 11), fg='red')
# default_folder_name.place(relx=0.1, rely=0.55)
#
# status_label = Label(holder_frame, font=('Helvetica', 15))
# status_label.place(relx=0.42, rely=0.85)
#
# # ==================== Entries ==================================
entrytext = StringVar()

# username = Entry(entries_frame, font=('Helvetica', 13), textvariable=entrytext)
# username.place(relx=0, relwidth=0.5, rely=0.43, relheight=0.15)
#
# # ==================== Buttons ==================================
visite_BTN = Button(holder_frame, text='New Visit', font=('Helvetica', 13),
                  command=lambda: new_visit())
visite_BTN.place(relx=0.35, relwidth=0.3, rely=0.5)

# -------------------------------------------------------------
#                        MAIN LOOP
# -------------------------------------------------------------
if __name__ == '__main__':
    # font_test()
    root.mainloop()
