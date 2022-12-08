#!/usr/bin/python3
"""Contains the FileStorage class model

"""

import json



from models.base_model import BaseModel

from models.user import User

from models.state import State

from models.amenity import Amenity

from models.city import City

from models.place import Place

from models.review import Review



classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,

           "Place": Place, "Review": Review, "State": State, "User": User}



class FileStorage:

    """

    serializes instances to a JSON file and

    deserializes JSON file to instances

    """



    __file_path = "file.json"

    __objects = {}



    def all(self):

        """

        Returns the dictionary __objects

        """

        return self.__objects



    def new(self, obj):

        """

        sets in __objects the `obj` with key <obj class name>.id

        """

        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj



    def save(self):

        """

        Serialize __objects to the JSON file

        """

        with open(self.__file_path, mode="w") as f:

            dict_storage = {}

            for k, v in self.__objects.items():

                dict_storage[k] = v.to_dict()

            json.dump(dict_storage, f)



    def reload(self):

        """

        Deserializes the JSON file to __objects

        -> Only IF it exists!

        """

        try:

            with open(self.__file_path, 'r') as f:

                jo = json.load(f)

            for key in jo:

                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])

        except:

            pass
