from flask import Flask, render_template, request
import string
import random
import pandas as pd

app = Flask(__name__)

# Define character sets
letters_upp = string.ascii_uppercase
letters_low = string.ascii_lowercase
numbers = string.digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '-', '_', '|', '\'', '/']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nr_letters_upp = int(request.form['letters_upp'])
        nr_letters_low = int(request.form['letters_low'])
        nr_numbers = int(request.form['numbers'])
        nr_symbols = int(request.form['symbols'])

        # Generate password
        passcode = []
        passcode.extend(random.choices(letters_upp, k=nr_letters_upp))
        passcode.extend(random.choices(letters_low, k=nr_letters_low))
        passcode.extend(random.choices(numbers, k=nr_numbers))
        passcode.extend(random.choices(symbols, k=nr_symbols))
        random.shuffle(passcode)
        password = ''.join(passcode)

        # Save password to CSV file
        df = pd.DataFrame({'Generated Password': [password]})
        df.to_csv('generated_password.csv', index=False)

        return render_template('index.html', password=password)

    return render_template('index.html', password='')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)