# log_ingestor.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = 'logs.db'

# Initialize SQLite database
conn = sqlite3.connect(DB_FILE)
conn.execute('''CREATE TABLE IF NOT EXISTS logs
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              level TEXT,
              message TEXT,
              resourceId TEXT,
              timestamp TEXT,
              traceId TEXT,
              spanId TEXT,
              [commit] TEXT,
              parentResourceId TEXT)''')
conn.commit()
conn.close()

@app.route('/ingest', methods=['POST'])
def ingest_log():
    try:
        log_data = request.json
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO logs (level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (log_data['level'], log_data['message'], log_data['resourceId'], log_data['timestamp'],
              log_data['traceId'], log_data['spanId'], log_data['commit'], log_data['metadata']['parentResourceId']))
        conn.commit()
        conn.close()
        return jsonify({"status": "success"}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3000)
