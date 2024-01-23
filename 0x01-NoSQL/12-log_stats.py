#!/usr/bin/env python3
"""Providing stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """Providing stats about Nginx logs"""
    items = {}
    if option:
        val = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        prin(f"\tmethod {option}: {val}")
        return


if __name__ == "__main__":
