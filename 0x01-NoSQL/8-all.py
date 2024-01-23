#!/usr/bin/env python3
"""Listing all documents"""
import pymongo


def list_all(mongo_collection):
    """Function listing all doc in a collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [p for p in docs]
