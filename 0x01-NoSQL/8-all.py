#!/usr/bin/env python3
"""This module contains function that lists all
documents in a collection.
"""


def list_all(mongo_collection):
    """Lists all documents."""
    if mongo_collection:
        return list(mongo_collection.find())
    return []
