#!/usr/bin/env python3
"""Changing school topics"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """updating doc with a value as a attr"""
    return mongo_collection.update_many({
        "name": name
    },
    {
        "$set": {
            "topics": topics
        }
    })
