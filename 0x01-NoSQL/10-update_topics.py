#!/usr/bin/env python3
"""This module contains a function that changes all topics
of a school document based on the name.
"""


def update_topics(mongo_collection, name, topics):
    """Updates topic based on the name.

    Args:
        mongo_collection: MongoDb data collection.
        name (str): the school name to update.
        topicts (List of str): List of topics to set
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
