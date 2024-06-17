from tkinter import *  # Importing all necessary functions and classes from Tkinter for GUI development
from PIL import ImageTk, Image  # Importing ImageTk and Image classes from the Pillow library for image handling
from tkinter import messagebox  # Importing messagebox for creating pop-up message boxes
import os  # Importing os module to handle file path checking

class Login:
    def __init__(self, root):
        self.root = root  # Setting the root window to the one passed to this class
        self.root.title("Login System")  # Setting the title of the window
        self.root.geometry("1199x600+100+50")  # Setting the size and position of the window
        self.root.resizable(False, False)  # Disabling the option to resize the window

        # Step 1: Load and resize the background image
        image_path = 'b_g.jpeg'  # Define the path to the background image
        if os.path.exists(image_path):  # Check if the image file exists
            self.original_image = Image.open(image_path)  # Open the image file
            self.resized_image = self.original_image.resize((1199, 600), Image.LANCZOS)  # Resize the image to fit the window size using LANCZOS filter for high quality
            self.bg = ImageTk.PhotoImage(self.resized_image)  # Convert the resized image to a PhotoImage object suitable for Tkinter

            # Step 2: Set the background image on a Label widget
            self.bg_image = Label(self.root, image=self.bg)  # Create a Label widget and set the image
            self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)  # Place the Label widget to cover the entire window
        else:
            messagebox.showerror("Error", f"Image file '{image_path}' not found.", parent=self.root)  # Show error message if the image file is not found

        # Step 3: Create a frame for the login form
        Frame_login = Frame(self.root, bg="white")  # Create a Frame widget with white background color
        Frame_login.place(x=330, y=150, width=500, height=400)  # Position the frame in the window with specific size

        # Step 4: Add title and subtitle to the login form
        title = Label(Frame_login, text="Login Here", font=("Serif", 35, "bold"), fg="#6162FF", bg="white")  # Create the title Label with specified font and colors
        title.place(x=90, y=30)  # Position the title Label within the frame
        subtitle = Label(Frame_login, text="Members Login Area", font=("Goudy old style", 15, "bold"), fg="#1d1d1d", bg="white")  # Create the subtitle Label
        subtitle.place(x=90, y=100)  # Position the subtitle Label within the frame

        # Step 5: Add username label and text entry field
        lbl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")  # Create the username Label
        lbl_user.place(x=90, y=140)  # Position the username Label within the frame
        self.username = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6")  # Create the username Entry widget with specific font and background color
        self.username.place(x=90, y=170, width=320, height=35)  # Position the username Entry widget within the frame

        # Step 6: Add password label and text entry field
        lbl_password = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="grey", bg="white")  # Create the password Label
        lbl_password.place(x=90, y=210)  # Position the password Label within the frame
        self.password = Entry(Frame_login, font=("Goudy old style", 15), bg="#E7E6E6", show='*')  # Create the password Entry widget and mask the input with '*'
        self.password.place(x=90, y=240, width=320, height=35)  # Position the password Entry widget within the frame

        # Step 7: Add "forgot password" button
        forget = Button(Frame_login, text="Forgot password?", bd=0, cursor="hand2", font=("Goudy old style", 15), fg="grey", bg="white")  # Create the forgot password Button
        forget.place(x=90, y=280)  # Position the forgot password Button within the frame

        # Step 8: Add login button
        submit = Button(Frame_login, command=self.check_function, cursor="hand2", text="Login", bd=0, font=("Goudy old style", 15), bg="#6162ff", fg="white")  # Create the login Button and bind it to the check_function method
        submit.place(x=90, y=320, width=180, height=40)  # Position the login Button within the frame

    # Method to check login credentials
    def check_function(self):
        # Step 9: Check if any field is empty
        if self.username.get() == "" or self.password.get() == "":  # Get the text from username and password Entry widgets
            messagebox.showerror("Error", "All fields are required", parent=self.root)  # Show error message if any field is empty
        # Step 10: Check if username and password are correct
        elif self.username.get() != "21kq1a0585" or self.password.get() != "123456":  # Check if the entered username and password match the predefined ones
            messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)  # Show error message if the credentials are incorrect
        else:
            # Step 11: Display welcome message if login is successful
            messagebox.showinfo("Welcome", f"Welcome {self.username.get()}")  # Show a welcome message if credentials are correct

# Step 12: Create the main window and run the application
root = Tk()  # Initialize the Tkinter root window
obj = Login(root)  # Create an instance of the Login class, passing the root window as an argument
root.mainloop()  # Enter the main event loop to make the window responsive
