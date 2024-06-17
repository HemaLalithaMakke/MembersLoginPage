#Login System using Tkinter and PIL


Welcome to my Login System project! This is a simple GUI-based login application created using Python's Tkinter library for the graphical user interface and PIL (Pillow) for handling images. Below is a detailed description of the project and its components.

#Project Overview
This project demonstrates how to create a basic login system with a graphical interface in Python. The main features include background image handling, a login form with user input fields, and validation logic to check user credentials.

#Key Features
Background Image Handling

I have added a background image (b_g.jpeg) to enhance the visual appeal of the login window.
The image is loaded and resized to fit the window dimensions (1199x600 pixels) using the PIL library.


#Login Form

The login form is designed within a frame placed in the center of the window.

#The form includes:
A title ("Login Here") and a subtitle ("Members Login Area") to indicate the purpose of the form.
Labels and entry fields for the username and password.
A "Forgot password?" button for future functionality.
A "Login" button that triggers the login validation process.
Validation Logic

When the "Login" button is clicked, the application checks if the username and password fields are empty. If either field is empty, an error message prompts the user to fill in all fields.
The credentials are validated against predefined values (username: 21kq1a0585, password: 123456). If the credentials are incorrect, an error message is displayed. If they are correct, a welcome message is shown.


#Error Handling

The application uses Tkinter's messagebox to display error messages for various scenarios, such as missing fields, incorrect credentials, and missing background image.
User Interaction

The interface is designed to be user-friendly, with clickable buttons and clear error messages to guide the user through the login process.
