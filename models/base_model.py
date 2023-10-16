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
        [__init__(): Initializes a new instance of BaseModel.] <---changed
        __str__(): Returns a string representation of the instance.
        save(): Updates the 'updated_at' attribute with current datetime.
        to_dict(): Converts the instance to a dictionary for serialization.

    Additional Methods:
        __init__(self, *args, **kwargs): Initializes a new instance of
        BaseModel using *args and kwargs*
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel using *args and **kwargs.

        If **kwargs is not empty:
        o Each key of kwargs becomes an attribute name
        o Each value of kwargs becomes the value of corresponding attributes.
        o 'created_at' and 'updated_at' and 'created_at' are converted from
        string to datetime object.

        If **kwargs is emoty:
        o Create a new instance with id and created_at attributes.

        Args:

         o *args: Not used.
         o **kwargs:Key-value pairs representing attributes and their values

        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        """
                        Convert 'created_at' and 'updated_at'
                        string to datetime
                        """
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

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
