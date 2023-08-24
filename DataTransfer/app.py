from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to transfer record between databases
def transfer_record(record_id, source_conn, dest_conn):
    try:
        # Fetch data from source database
        source_cursor = source_conn.execute("SELECT id, name, description, price FROM products_product WHERE id = ?", (record_id,))
        record_data = source_cursor.fetchone()

        # Insert data into destination database
        dest_conn.execute("INSERT INTO products_product (id, name, description, price) VALUES (?, ?, ?, ?)", record_data)

        # Delete data from source database
        source_conn.execute("DELETE FROM products_product WHERE id = ?", (record_id,))
        
        # Commit changes
        dest_conn.commit()
        source_conn.commit()

        return True
    except Exception as e:
        # Handle errors and roll back changes
        dest_conn.rollback()
        source_conn.rollback()
        print("Error:", e, e.__traceback__.tb_lineno)
        return False
 
@app.route('/transfer_record', methods=['POST'])
def transfer_record_api():
    try:
        # Extract parameters from request
        record_id = request.json['record_id']
        source_db = request.json['source_db']
        dest_db = request.json['dest_db']

        # Connect to databases
        source_conn = sqlite3.connect(source_db)
        dest_conn = sqlite3.connect(dest_db)

        # Transfer record and handle response
        if transfer_record(record_id, source_conn, dest_conn):
            response = {'success': True, 'message': 'Record transferred successfully.'}
        else:
            response = {'success': False, 'message': 'Error transferring record.'}

        # Close connections
        source_conn.close()
        dest_conn.close()

        return jsonify(response)
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/get_all_records', methods=['POST'])
def get_all_records_api():
    try:
        # Extract parameters from request
        db = request.json['db']
    
        # Connect to databases
        db_conn = sqlite3.connect(db)
    
        cursor = db_conn.cursor()
        cursor.execute("SELECT * FROM products_product;")
        records = cursor.fetchall()  # Fetch all records
        db_conn.close()
        # Convert records to a list of dictionaries
        result = [{'id': record[0], 'name': record[1], 'description': record[2], 'price': record[3]} for record in records]

        return jsonify(result)  # Return the records as JSON
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)