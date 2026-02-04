import mysql.connector
import time

db_config = {
    'user': 'usr',
    'password': 'sofe4630u',
    'host': '34.130.233.20',
    'database': 'Readings'
}

def fetch_data():
    try:
        # Establish connection
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        print("--- Fetching Latest 5 Smart Meter Records ---")
        # Query the table populated by Pub/Sub connector
        query = "SELECT * FROM smartMeterReadings ORDER BY time DESC LIMIT 5"
        cursor.execute(query)

        rows = cursor.fetchall()
        for row in rows:
            print(f"ID: {row[0]} | Time: {row[1]} | Device: {row[2]} | Temp: {row[3]}°C")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        fetch_data()
        print("Waiting for new data...\n")
        time.sleep(5) # Poll every 5 seconds