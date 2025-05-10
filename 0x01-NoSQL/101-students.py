#!/usr/bin/env python3
"""Module to return all students sorted by average score"""
from pymongo.collection import Collection


def top_students(mongo_collection: Collection):
    """
    Returns all students sorted by their average topic score

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of students sorted by averageScore (descending)
    """
    return list(mongo_collection.aggregate([
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]))
