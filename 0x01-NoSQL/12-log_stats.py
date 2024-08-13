#!/usr/bin/env python3
"""
provides some stats about nginx server
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        query = {"method": method}
        method_count = nginx_collection.count_documents(query)
        print(f"\tmethod {method}: {method_count}")

    status_checks = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
        )
    print(f"{status_checks} status check")
