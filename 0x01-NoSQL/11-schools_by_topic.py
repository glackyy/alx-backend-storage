#!/usr/bin/env python3
"""Listing school topics"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returning list of school having a specific topic"""
    return mongo_collection.find({"topic": {"$in": [topic]}})
