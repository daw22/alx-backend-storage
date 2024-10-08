#!/usr/bin/env python3
"""
pymongo update
"""


def update_topics(mongo_collection, name, topics):
    """
    updates topics of the collection
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
