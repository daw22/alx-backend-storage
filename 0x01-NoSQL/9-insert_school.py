#!/usr/bin/env python3
"""
pymongo insert
"""


def insert_school(mongo_collection, **kwargs):
    """
    inserts a document to scools collection
    and returns the new _id
    """
    x = mongo_collection.insert_one(kwargs)
    return x.inserted_id
