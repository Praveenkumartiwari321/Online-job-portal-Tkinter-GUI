from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import ast

root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)
# photo = PhotoImage(file="img/logo.png")
# photo.iconphoto(False, photo)


def login():
    username = user.get()
    password1 = password.get()

    file = open('login/datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and password1 == r[username]:

        screen = Toplevel(root)
        screen.title("Available Jobs")
        screen.geometry("925x500+300+200")
        screen.config(bg="white")

        heading = Label(screen, text="Available Jobs", fg="#57a1f8",
                        bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
        heading.place(x=350, y=10)
        Frame(screen, width=295, height=2, bg="black").place(x=320, y=60)

    #  <--------->jobs list<-------------->

        frame = Frame(screen, width=800, height=350, bg="white")
        frame.place(x=60, y=80)

        #  job 1

        label1 = Label(screen, text="1:- Full stack developer", fg="#f54242",
                       bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        label1.place(x=10, y=80)

        des1 = Label(frame, text="We required an experience full stack developer, register as soon as possible very few seats left!!! ", fg="#f542f5",
                     bg="white", font=("Microsoft YaHei UI Light", 9, "bold"))
        des1.place(x=0, y=32)

        Button(screen, width=20, pady=7, text="Apply",
               bg="#57a1f8", fg="Black", border=0, font=("Microsoft YaHei UI Light", 8, "bold")).place(x=750, y=80)

        # job 2

        label2 = Label(screen, text="2:- Software Engineer", fg="#f54242",
                       bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        label2.place(x=10, y=160)

        des2 = Label(frame, text="We required a fresh software Engineer , register as soon as possible very few seats left!!! ", fg="#f542f5",
                     bg="white", font=("Microsoft YaHei UI Light", 9, "bold"))
        des2.place(x=0, y=115)

        Button(screen, width=20, pady=7, text="Apply",
               bg="#57a1f8", fg="Black", border=0, font=("Microsoft YaHei UI Light", 8, "bold")).place(x=750, y=160)

        #  job 3

        label3 = Label(screen, text="3:- Data Scientist", fg="#f54242",
                       bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        label3.place(x=10, y=240)

        des3 = Label(frame, text="We required a 5+ years experience Data Scientist , register as soon as possible only 1 seats left!!! ", fg="#f542f5",
                     bg="white", font=("Microsoft YaHei UI Light", 9, "bold"))
        des3.place(x=0, y=194)

        Button(screen, width=20, pady=7, text="Apply",
               bg="#57a1f8", fg="Black", border=0, font=("Microsoft YaHei UI Light", 8, "bold")).place(x=750, y=240)

        # Job 4

        label4 = Label(screen, text="4:- Front end Developer", fg="#f54242",
                       bg="white", font=("Microsoft YaHei UI Light", 15, "bold"))
        label4.place(x=10, y=320)

        des4 = Label(frame, text="We required a freshers React developer , register as soon as possible only 10 seats left!!! ", fg="#f542f5",
                     bg="white", font=("Microsoft YaHei UI Light", 9, "bold"))
        des4.place(x=0, y=270)

        Button(screen, width=20, pady=7, text="Apply",
               bg="#57a1f8", fg="Black", border=0, font=("Microsoft YaHei UI Light", 8, "bold")).place(x=750, y=320)

        screen.mainloop()

    else:
        messagebox.showerror("Invalid", "invalid username or password")


# <-------------------------------------> SignUp Module <---------------------------------->
def signup_command():
    window = Toplevel(root)

    window.title("SignUp")
    window.geometry("925x500+300+200")
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        username = user.get()
        password1 = password.get()
        confrom_pass = conform.get()

        if password1 == confrom_pass:
            try:
                file = open('login/datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password1}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open("login/datasheet.txt", "w")
                w = file.write(str(r))

                messagebox.showinfo("Signup", "Sucessfully sign up")

            except:
                file: open("datasheet.txt", "w")
                pp = str({"Username": "password1"})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror("Invalid", "Both Password should match")

    def sign():

        window.destroy()

    image = Image.open("img/sign-up.png")
    image_resize = image.resize((350, 350))
    img = ImageTk.PhotoImage(image_resize)
    Label(window, image=img, border=0, bg="white").place(x=50, y=50)

    frame = Frame(window, width=350, height=420, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text="Sign up", fg="#57a1f8",
                    bg="white", font=("Microsoft Yahei UI Light", 23, "bold"))
    heading.place(x=100, y=5)


# Entry menu

    def on_enter(e):
        user.delete(0, "end")

    def on_leave(e):
        if user.get() == '':
            user.insert(0, "Username")

    user = Entry(frame, width=25, fg="black", border=0, bg="white",
                 font=("Microsoft Yahei UI Light", 11))
    user. place(x=30, y=80)
    user.insert(0, "Username")
    user.bind("<FocusIn>", on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)


# Email Address

    def on_enter(e):
        email.delete(0, "end")

    def on_leave(e):
        if email.get() == '':
            email.insert(0, "Email Address")

    email = Entry(frame, width=25, fg="black", border=0, bg="white",
                  font=("Microsoft Yahei UI Light", 11))
    email. place(x=30, y=150)
    email.insert(0, "Email Address")
    email.bind("<FocusIn>", on_enter)
    email.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


# Password

    def on_enter(e):
        password.delete(0, "end")

    def on_leave(e):
        if password.get() == '':
            password.insert(0, "Password")

    password = Entry(frame, width=25, fg="black", border=0,
                     bg="white", font=("Microsoft Yahei UI Light", 11))
    password. place(x=30, y=220)
    password.insert(0, "Password")
    password.bind("<FocusIn>", on_enter)
    password.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

# Confirm password

    def on_enter(e):
        conform.delete(0, "end")

    def on_leave(e):
        if conform.get() == '':
            conform.insert(0, "Conform Password")

    conform = Entry(frame, width=25, fg="black", border=0,
                    bg="white", font=("Microsoft Yahei UI Light", 11))
    conform. place(x=30, y=290)
    conform.insert(0, "Conform Password")
    conform.bind("<FocusIn>", on_enter)
    conform.bind("<FocusOut>", on_leave)

    Frame(frame, width=295, height=2, bg="black").place(x=25, y=317)

    Button(frame, width=39, pady=7, text="Sign up",
           bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=350)

    label = Label(frame, text="I have an account", fg="black",
                  bg="white", font=("Microsoft Yahei UI Light", 9))
    label.place(x=90, y=400)

    signin = Button(frame, width=6, text="Log In",
                    border=0, bg='white', cursor="hand2", fg="#57a1f8", command=sign)
    signin.place(x=200, y=402)

    window.mainloop()

# ------------------------------------->End of the SignUp module------------------------->


image = Image.open("img/login.png")
image_resize = image.resize((550, 350))
img = ImageTk.PhotoImage(image_resize)

Label(root, image=img, bg='white').place(x=-20, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Log in", fg="#57a1f8",
                bg="white", font=("Microsoft YaHei UI Light", 23, "bold"))
heading.place(x=100, y=5)

# Username


def on_enter(e):
    user.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, "Username")


user = Entry(frame, width=25, fg="black", border=0, bg="White",
             font=("Microsoft YaHei UI Light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

# Password


def on_enter(e):
    password.delete(0, "end")


def on_leave(e):
    name = user.get()
    if name == '':
        password.insert(0, "Password")


password = Entry(frame, width=25, fg="black", border=0, bg="White",
                 font=("Microsoft YaHei UI Light", 11))
password.place(x=30, y=150)
password.insert(0, "Password")
password.bind("<FocusIn>", on_enter)
password.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)


Button(frame, width=39, pady=7, text="Sign in",
       bg="#57a1f8", fg="white", border=0, command=login).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg="black",
              bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text="Sign up", border=0,
                 bg="white", cursor="hand2", fg="#57a1f8", command=signup_command)
sign_up.place(x=215, y=270)


root.mainloop()
