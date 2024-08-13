#!/usr/bin/env python3
"""
pymongo
"""


def list_all(mongo_collection):
    """
    lists all decuments in a collection
    Args:
        mongo_collection: collection object
    """
    docs = []
    for x in mongo_collection.find():
        docs.append(x)
    return docs
