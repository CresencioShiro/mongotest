import time
from pymongo import MongoClient
from pprint import pprint

def get_mongo_stats(client):
    # Get the server status data
    db = client.admin
    status = db.command("serverStatus")
    
    # Extract relevant traffic metrics
    connections = status["connections"]["current"]
    network_bytes_in = status["network"]["bytesIn"]
    network_bytes_out = status["network"]["bytesOut"]
    operation_count = status["opcounters"]
    
    # Display traffic data
    print("===== MongoDB Traffic Statistics =====")
    print(f"Active Connections: {connections}")
    print(f"Network Bytes In: {network_bytes_in}")
    print(f"Network Bytes Out: {network_bytes_out}")
    print("Operation Counts:")
    print(f"  Inserts: {operation_count['insert']}")
    print(f"  Queries: {operation_count['query']}")
    print(f"  Updates: {operation_count['update']}")
    print(f"  Deletes: {operation_count['delete']}")
    print(f"  Commands: {operation_count['command']}")
    print("======================================\n")

def main():
    # Connect to the MongoDB server
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the URI if needed
    print("Connected to MongoDB. Monitoring traffic...\n")

    try:
        while True:
            get_mongo_stats(client)
            time.sleep(5)  # Update interval (in seconds)
    except KeyboardInterrupt:
        print("\nStopping the MongoDB Traffic Monitor.")
    finally:
        client.close()

if __name__ == "__main__":
    main()
    print("succes")
