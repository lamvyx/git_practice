def login(username, password):
    # Function to handle user login
    if username == "admin" and password == "password123":
        return "Login successful"
    else:
        return "Invalid credentials"