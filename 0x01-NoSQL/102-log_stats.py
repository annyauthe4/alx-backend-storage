#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
Displays log count, request methods, status checks,
and top 10 most frequent IP addresses.
"""

from pymongo import MongoClient


def log_stats():
    """
    Prints statistics about Nginx logs in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({
        "method": "GET", "path": "/status"
    })
    print(f"{status_count} status check")

    print("IPs:")
    top_ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
