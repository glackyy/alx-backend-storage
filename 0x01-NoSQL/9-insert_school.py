#!/usr/bin/env python3
"""Inserting a doc"""
import pymongo


def insert_school(mongo_collection):
    """inserting a doc into a collection"""
    dt = mongo_collection.insert_one()
    return dt.inserted_id
