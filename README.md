# Login System using Tkinter and PIL


Welcome to my Login System project! This is a simple GUI-based login application created using Python's Tkinter library for the graphical user interface and PIL (Pillow) for handling images. Below is a detailed description of the project and its components.

# Project Overview
This project demonstrates how to create a basic login system with a graphical interface in Python. The main features include background image handling, a login form with user input fields, and validation logic to check user credentials.

# Key Features: 
## Background Image Handling:

I have added a background image (b_g.jpeg) to enhance the visual appeal of the login window.
The image is loaded and resized to fit the window dimensions (1199x600 pixels) using the PIL library.


## Login Form:

The login form is designed within a frame placed in the center of the window.

## The form includes:
A title ("Login Here") and a subtitle ("Members Login Area") to indicate the purpose of the form.
Labels and entry fields for the username and password.
A "Forgot password?" button for future functionality.
A "Login" button that triggers the login validation process.
![Screenshot 2024-06-18 021336](https://github.com/HemaLalithaMakke/MembersLoginPage/assets/172250819/be8362ce-00b4-48f6-be57-a7ed5fba87fc)


## Validation Logic:

When the "Login" button is clicked, the application checks if the username and password fields are empty.
If either field is empty, an error message prompts the user to fill in all fields.

![Screenshot 2024-06-18 021407](https://github.com/HemaLalithaMakke/MembersLoginPage/assets/172250819/039715d9-fd8f-4748-829a-dea1c7632d57)


The credentials are validated against predefined values (username: 21kq1a0585, password: 123456). If the credentials are incorrect, an error message is displayed. 
If they are correct, a welcome message is shown.


![Screenshot 2024-06-18 021441](https://github.com/HemaLalithaMakke/MembersLoginPage/assets/172250819/3993fb9e-f0db-4ed9-a258-1889ecbe5922)


## Error Handling

The application uses Tkinter's messagebox to display error messages for various scenarios, such as missing fields, incorrect credentials, and missing background image.
User Interaction

The interface is designed to be user-friendly, with clickable buttons and clear error messages to guide the user through the login process.
