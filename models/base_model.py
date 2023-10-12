#!/usr/bin/python3
""" This module defines a base class for all models in the hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): The date and time when the instance is created.
        updated_at (datetime): The date and time when the instance is last
                               updated.

    Methods:
        __init__(): Initializes a new instance of BaseModel.
        __str__(): Returns a string representation of the instance.
        save(): Updates the 'updated_at' attribute with current datetime.
        to_dict(): Converts the instance to a dictionary for serialization.
    """

    def __init__(self):
        """Initializes a new instance of BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """Update the 'updated_at' attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the instance to a dictionary for serialization.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
