#!/usr/bin/env python3
"""Log stats update"""
from pymongo import MongoClient


def nginx_stats_check():
    cl = MongoClient()
    col = cl.logs.nginx
    num_of_documents = col.count_documents({})
    print("{} logs".format(num_of_documents))
    print("Methods:")
    methods_l = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for met in methods_l:
        meth_count = col.count_documents({"method": met})
        print("\tmethod {}: {}".format(met, meth_count))
    st = col.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(st))
if __name__ == "__main__":
