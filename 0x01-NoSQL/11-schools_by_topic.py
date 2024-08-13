#!/usr/bin/env python3
"""
pymongo find with params
"""


def schools_by_topic(mongo_collection, topic):
    """
    find schools teaching a topic
    """
    query = {"topics": {"$in": [topic]}}
    schools = mongo_collection.find(query)
    return schools
