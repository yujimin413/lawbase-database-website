from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# for Window
# def get_database_connection():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="lawbase")
#     return conn

# for Mac
def get_database_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="lawbase",
        auth_plugin='mysql_native_password')
    return conn


@app.route('/')
def index():
    return render_template('index.html')

#THIS AREA IS FOR DATA VIEWING

@app.route('/view_data')
def view_data():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases")
    data_from_database = cursor.fetchall()
    cursor.close()
    return render_template('view_data.html', data=data_from_database)



@app.route('/view_data/case')
def view_cases():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cases")
    cases_data = cursor.fetchall()
    cursor.close()
    return render_template('case.html', cases_data=cases_data)

@app.route('/view_data/client')
def view_client():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM client")
    client_data = cursor.fetchall()
    cursor.close()
    return render_template('client.html', client_data=client_data)

@app.route('/view_data/court')
def view_court():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM court")
    court_data = cursor.fetchall()
    cursor.close()
    return render_template('court.html', court_data=court_data)

@app.route('/view_data/document')
def view_document():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM document")
    document_data = cursor.fetchall()
    cursor.close()
    return render_template('document.html', document_data=document_data)

@app.route('/view_data/lawyer')
def view_lawyer():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM lawyer")
    lawyer_data = cursor.fetchall()
    cursor.close()
    return render_template('lawyer.html', lawyer_data=lawyer_data)

@app.route('/view_data/user')
def view_user():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    user_data = cursor.fetchall()
    cursor.close()
    return render_template('user.html', user_data=user_data)

# THIS AREA IS FOR DATA UPDATING

@app.route('/update_data')
def update_data():
    return render_template('update_data.html')

@app.route('/update_data/up_case', methods=['GET', 'POST'])
def update_case():
    if request.method == 'POST':
        case_id = request.form['case_id']
        client_id = request.form['client_id']
        title = request.form['title']
        department = request.form['department']
        open_date = request.form['open_date']
        close_date = request.form['close_date']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE cases SET client_ID = %s, title = %s, department = %s, open_date = %s, close_date = %s WHERE case_ID = %s",
                       (client_id, title, department, open_date, close_date, case_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_cases'))
    else:
        return render_template('up_case.html')

@app.route('/update_data/up_client', methods=['GET', 'POST'])
def update_client():
    if request.method == 'POST':
        client_id = request.form['client_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_no = request.form['contact_no']
        specialization = request.form['specialization']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE client SET first_name = %s, last_name = %s, contact_no = %s, specialization = %s WHERE client_ID = %s",
            (first_name, last_name, contact_no, specialization, client_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_client'))
    else:
        return render_template('up_client.html')


@app.route('/update_data/up_court', methods=['GET', 'POST'])
def update_court():
    if request.method == 'POST':
        court_id = request.form['court_id']
        name = request.form['name']
        court_type = request.form['court_type']
        location = request.form['location']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE court SET name = %s, court_type = %s, location = %s WHERE court_ID = %s",
                       (name, court_type, location, court_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_court'))
    else:
        return render_template('up_court.html')


@app.route('/update_data/up_document', methods=['GET', 'POST'])
def update_document():
    if request.method == 'POST':
        document_id = request.form['document_id']
        document_type = request.form['document_type']
        document_content = request.form['document_content']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE document SET document_type = %s, document_content = %s WHERE document_id = %s",
                       (document_type, document_content, document_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_document'))

    else:
        conn = get_database_connection()
        document_id = request.args.get('document_id')
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM document WHERE document_id = %s", (document_id,))
        document = cursor.fetchone()
        cursor.close()
        return render_template('up_document.html', document=document)


@app.route('/update_data/up_lawyer', methods=['GET', 'POST'])
def update_lawyer():
    if request.method == 'POST':
        lawyer_id = request.form['lawyer_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_no = request.form['contact_no']
        department = request.form['department']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE lawyer SET first_name = %s, last_name = %s, contact_no = %s, department = %s WHERE lawyer_ID = %s",
            (first_name, last_name, contact_no, department, lawyer_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_lawyer'))

    else:
        conn = get_database_connection()
        lawyer_id = request.args.get('lawyer_id')
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lawyer WHERE lawyer_ID = %s", (lawyer_id,))
        lawyer = cursor.fetchone()
        cursor.close()
        return render_template('up_lawyer.html', lawyer=lawyer)


@app.route('/update_data/up_user', methods=['GET', 'POST'])
def update_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE user SET first_name = %s, last_name = %s, email = %s, username = %s, password = %s WHERE user_ID = %s",
            (first_name, last_name, email, username, password, user_id))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_user'))
    else:
        conn = get_database_connection()
        user_id = request.args.get('user_id')
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE user_ID = %s", (user_id,))
        user = cursor.fetchone()
        cursor.close()

        return render_template('up_user.html', user=user)

# THIS AREA IS FOR DATA DELETION

@app.route('/delete_data')
def delete_data():
    return render_template('delete_data.html')


@app.route('/delete_data/del_case', methods=['GET', 'POST'])
def delete_case():
    if request.method == 'POST':
        case_id = request.form['case_id']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cases WHERE case_ID = %s", (case_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_cases'))

    else:
        return render_template('del_case.html')


@app.route('/delete_data/del_client', methods=['GET', 'POST'])
def delete_client():
    if request.method == 'POST':
        client_id = request.form['client_id']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM client WHERE client_ID = %s", (client_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_client'))

    else:
        return render_template('del_client.html')


@app.route('/delete_data/del_court', methods=['GET', 'POST'])
def delete_court():
    if request.method == 'POST':
        court_ID = request.form['court_ID']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM court WHERE court_ID = %s", (court_ID,))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_court'))

    else:
        return render_template('del_court.html')


@app.route('/delete_data/del_document', methods=['GET', 'POST'])
def delete_document():
    if request.method == 'POST':
        document_id = request.form['document_id']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM document WHERE document_ID = %s", (document_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_document'))

    else:
        return render_template('del_document.html')


@app.route('/delete_data/del_lawyer', methods=['GET', 'POST'])
def delete_lawyer():
    if request.method == 'POST':
        lawyer_id = request.form['lawyer_id']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lawyer WHERE lawyer_ID = %s", (lawyer_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_lawyer'))

    else:
        return render_template('del_lawyer.html')


@app.route('/delete_data/del_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE user_ID = %s", (user_id,))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_user'))

    else:
        return render_template('del_user.html')

# THIS AREA IS FOR DATA INSERTION

@app.route('/insert_data')
def insert_data():
    return render_template('insert_data.html')

@app.route('/insert_data/i_case', methods=['GET', 'POST'])
def insert_case():
    if request.method == 'POST':
        case_id = request.form['case_id']
        client_id = request.form['client_id']
        title = request.form['title']
        department = request.form['department']
        open_date = request.form['open_date']
        close_date = request.form['close_date']

        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cases (case_ID, client_ID, title, department, open_date, close_date) VALUES (%s, %s, %s, %s, %s, %s)",
                       (case_id, client_id, title, department, open_date, close_date))
        conn.commit()
        cursor.close()
        return redirect(url_for('view_cases'))

    else:
        return render_template('i_case.html')

@app.route('/insert_data/i_client', methods=['GET', 'POST'])
def insert_client():
    if request.method == 'POST':
        client_id = request.form['client_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_no = request.form['contact_no']
        specialization = request.form['specialization']

        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO client (client_ID, first_name, last_name, contact_no, specialization) VALUES (%s, %s, %s, %s, %s)",
                       (client_id, first_name, last_name, contact_no, specialization))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_client'))

    else:
        return render_template('i_client.html')

@app.route('/insert_data/i_court', methods=['GET', 'POST'])
def insert_court():
    if request.method == 'POST':
        name = request.form['name']
        court_type = request.form['court_type']
        location = request.form['location']

        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO court (name, court_type, location ) VALUES (%s, %s, %s)",
                       (name, court_type,location))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_court'))

    else:
        return render_template('i_court.html')

@app.route('/insert_data/i_document', methods=['GET', 'POST'])
def insert_document():
    if request.method == 'POST':
        document_type = request.form['document_type']
        document_content = request.form['document_content']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO document (document_type, document_content) VALUES (%s, %s)",
                       (document_type, document_content))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_document'))
    else:
        return render_template('i_document.html')

@app.route('/insert_data/i_lawyer', methods=['GET', 'POST'])
def insert_lawyer():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        contact_no = request.form['contact_no']
        department = request.form['department']
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO lawyer (first_name, last_name, contact_no, department) VALUES (%s, %s, %s, %s)",
                       (first_name, last_name, contact_no, department))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_lawyer'))

    else:

        return render_template('i_lawyer.html')

@app.route('/insert_data/i_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (first_name, last_name, email, username, password) VALUES (%s, %s, %s, %s, %s)",
                       (first_name, last_name, email, username, password))
        conn.commit()
        cursor.close()

        return redirect(url_for('view_user'))
    else:
        return render_template('i_user.html')


@app.route('/more_index')
def more_options():
    return render_template('more_index.html')

@app.route('/more_index/set_comp', methods=['GET', 'POST'])
def active_cases():
    conn = get_database_connection()
    with conn.cursor() as cursor:
        sql = """
            SELECT c.client_ID, c.first_name, c.last_name, c.contact_no, c.specialization
            FROM client c
            INNER JOIN cases ca ON c.client_ID = ca.client_ID
            WHERE ca.close_date = 'Not Closed'
        """
        cursor.execute(sql)
        active_clients = cursor.fetchall()
    return render_template('Active_cases.html', active_clients=active_clients)


@app.route('/more_index/lawyer_dept', methods=['GET', 'POST'])
def lawyer_dept():
    if request.method == 'POST':
        department = request.form['department']
        query = "SELECT * FROM lawyer WHERE department IN (SELECT specialization FROM client WHERE department = %s)"
        conn = get_database_connection()
        cursor = conn.cursor()
        cursor.execute(query, (department,))
        lawyers = cursor.fetchall()
        return render_template('lawyer_dept.html', lawyers=lawyers)
    else:
        return render_template('lawyer_dept.html')


@app.route('/more_index/multiple_cases')
def multiple_cases():
    query = """
        WITH ActiveCases AS (
            SELECT client_ID
            FROM cases
            WHERE close_date = 'Not Closed'
            GROUP BY client_ID
            HAVING COUNT(*) > 1
        )
        SELECT c.client_ID, c.first_name, c.last_name
        FROM client c
        JOIN ActiveCases ac ON c.client_ID = ac.client_ID
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    clients = cursor.fetchall()
    conn.close()
    return render_template('multiple_cases.html', clients=clients)


@app.route('/more_index/case_stats')
def case_stats():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            l.department,
            COUNT(DISTINCT c.case_ID) AS total_cases,
            COUNT(DISTINCT c.case_ID) / COUNT(DISTINCT l.lawyer_ID) AS avg_cases_per_lawyer
        FROM 
            cases c
        JOIN
            lawyer l ON c.department = l.department 
        GROUP BY 
            l.department;
    """)
    case_statistics = cursor.fetchall()
    cursor.close()
    return render_template('case_stats.html', case_statistics=case_statistics)


@app.route('/more_index/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        conn = get_database_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM document WHERE document_content LIKE %s", ('%' + keyword + '%',))
        documents = cursor.fetchall()
        conn.close()
        return render_template('search.html', documents=documents, keyword=keyword)
    else:
        return render_template('search.html', documents=None, keyword=None)



@app.route('/more_index/department_stats')
def department_stats():
    conn = get_database_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            department,
            COUNT(*) AS total_cases
        FROM 
            cases
        GROUP BY 
            department WITH ROLLUP;
    """)
    department_statistics = cursor.fetchall()
    cursor.close()
    return render_template('department_stats.html', department_statistics=department_statistics)


# EXIT STATUS

@app.route('/exit')
def exit():
    return "This was Group 4. Thanks for hanging out.  Goodbye!"


if __name__ == '__main__':
    app.run(debug=True)