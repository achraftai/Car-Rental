from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)


def connect_db():
    return sqlite3.connect('rental.db')

@app.route('/')
def index():
    try:
        conn = connect_db()
        cur = conn.cursor()
        # cur.execute('SELECT * FROM booking')
        cur.execute('SELECT booking.id, booking.start_date, booking.end_date, customer.first, customer.last, customer.phone_number, customer.email, vehicle.make, vehicle.model FROM booking INNER JOIN vehicle ON booking.vin = vehicle.vin INNER JOIN  customer ON booking.license_number = customer.license_number;')
        data = cur.fetchall()
        conn.close()
        # for row in data:
        #     r = row.split(',')
        #     print(r)
        return render_template('index.html', data=data)
        
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
@app.route('/customer')
def other_page():
    return render_template('customer.html')

@app.route('/form1', methods=['POST'])
def form1():
    print("Reached submit route")
    if request.method == 'POST':
            fname = request.form['fname']
            lname = request.form['lname']
            address = request.form['address']
            phone = request.form['phone_number']
            email = request.form['email']
            license = request.form['license']

            print(request.form)

            
            conn = sqlite3.connect('rental.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO customer (first, last, address, phone_number, email, license_number) VALUES (?, ?, ?, ?, ?, ?)', (fname, lname, address, phone, email, license))
            conn.commit()
            conn.close()
            
            return 'Data submitted successfully'

   
def increment():
    conn=sqlite3.connect('rental.db')
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT (*) as row_count FROM booking;')
    numrows = cursor.fetchall()
    numrows=numrows[0][0] + 1
    conn.close()

    return "B" + str(numrows)

@app.route('/form2', methods=['POST'])
def form2():
    print("Reached submit route")
    if request.method == 'POST':
        try:
            b_id = increment() 
            start = request.form['start']
            end = request.form['end']
            amount = request.form['amount']
            vin = request.form['vin']
            license = request.form['license']

            print(request.form)

            
            conn = sqlite3.connect('rental.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO booking (id, start_date, end_date, amount, vin, license_number) VALUES (?, ?, ?, ?, ?, ?)', (b_id, start, end, amount, vin, license))
            conn.commit()
            conn.close()
            
            return 'Data submitted successfully'
        except Exception as e:
            print('Error:', e)

@app.route('/form3', methods=['POST'])
def form3():
    print("Reached submit route")
    if request.method == 'POST':
        try:
            vin = request.form['vin']
            type = request.form['type']
            make = request.form['make']
            model = request.form['model']
            year = request.form['year']

            print(request.form)

            
            conn = sqlite3.connect('rental.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO vehicle (vin, type, make, model, year) VALUES (?, ?, ?, ?, ?)', (vin, type, make, model, year))
            conn.commit()
            conn.close()
            
            return 'Data submitted successfully'
        except Exception as e:
            print('Error:', e)



# if __name__ == "__main__":
#     index()
#     app.run()
    