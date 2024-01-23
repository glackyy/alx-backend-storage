#!/usr/bin/env python3
"""Log stats update"""
from pymongo import MongoClient


def nginx_stats_check():
    cl = MongoClient()
    col = cl.logs.nginx
    num_of_documents = col.count_documents({})
    print("{} logs".format(num_of_documents))
    print("Methods:")

if __name__ == "__main__":
