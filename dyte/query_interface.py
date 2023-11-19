# query_interface.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = 'logs.db'

def execute_query(query, params=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

@app.route('/search', methods=['GET'])
def search_logs():
    try:
        query_params = request.args
        filters = []
        for key, value in query_params.items():
            filters.append(f"{key} = ?")
        if filters:
            query = f"SELECT * FROM logs WHERE {' AND '.join(filters)}"
            params = tuple(query_params.values())
        else:
            query = "SELECT * FROM logs"
            params = None
        result = execute_query(query, params)
        return jsonify({"status": "success", "data": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
