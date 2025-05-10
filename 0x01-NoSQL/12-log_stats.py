#!/usr/bin/env python3
"""
Provides statistics about Nginx logs stored in MongoDB.

Database: logs
Collection: nginx

Displays:
- Total number of logs
- Number of logs for each HTTP method:
  GET, POST, PUT, PATCH, DELETE
- Number of logs with method=GET and path=/status
"""

from pymongo import MongoClient


def log_stats():
    """
    Connects to MongoDB and prints statistics about
    the logs.nginx collection.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
