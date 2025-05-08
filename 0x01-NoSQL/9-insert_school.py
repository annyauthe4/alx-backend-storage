#!/usr/bin/env python3
"""This module inserts a new document in a collection
based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection.

    Args:
        mongo_collection: The pymongo collection obj
        **kwargs: Key-value pairs rep the doc fields.

    Returns:
        The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
        
