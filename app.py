from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='zomato_chronicles'
)


@app.route('/')
def home():
    # Fetch dishes from the database
    cursor = db.cursor()
    cursor.execute("SELECT * FROM dishes")
    dishes = cursor.fetchall()
    cursor.close()
    return render_template('index.html', dishes=dishes)

@app.route('/add_dish', methods=['POST'])
def add_dish():
    # Retrieve form data
    name = request.form['name']
    price = request.form['price']
    availability = True if request.form.get('availability') else False

    # Insert new dish into the database
    cursor = db.cursor()
    cursor.execute("INSERT INTO dishes (name, price, availability) VALUES (%s, %s, %s)",
                   (name, price, availability))
    db.commit()
    cursor.close()

    # Redirect to the menu page
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
