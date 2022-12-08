#!/usr/bin/python3
"""Module for define console actions"""

from models.base_model import BaseModel

from models.user import User

from models.state import State

from models.amenity import Amenity

from models.city import City

from models.place import Place

from models.review import Review

from models import storage

from utils import Utils





class Actions:

    """Handle console actions"""

    __classes = {'BaseModel': BaseModel, 'User': User, 'State': State,

                 'Amenity': Amenity, 'City': City, 'Place': Place,

                 'Review': Review}



    @staticmethod

    def class_exists(class_name):

        """Check if the class exists"""

        classes = Actions.__classes.keys()

        return class_name in set(classes)



    @staticmethod

    def valid_arguments(arg):

        """Check if the argument (tuple) is valid"""

        if not arg:

            print('** class name missing **')

            return False



        k_class = arg[0]

        if not Actions.class_exists(k_class):

            print('** class doesn\'t exist **')

            return False



        return True



    @staticmethod

    def tuple2value(arg, idx):

        """Returns the value of a tuple, or None"""

        return None if len(arg) < idx + 1 else arg[idx]



    @staticmethod

    def object_exists(arg):

        """Check if the id is a valid object id"""

        # id_obj = None if len(arg) < 2 else arg[1]

        id_obj = Actions.tuple2value(arg, 1)

        if not id_obj:

            print('** instance id missing **')

            return



        obj = storage.get_object(arg[0], id_obj)

        if obj is None:

            print('** no instance found **')

            return None



        return obj



    @staticmethod

    def create(arg):

        """Create a new instance of class @arg[0]"""

        if not Actions.valid_arguments(arg):

            return



        k_class = arg[0]

        obj = Actions.__classes[k_class]()

        obj.save()

        print(obj.id)



    @staticmethod

    def show(arg):

        """Show an instance"""

        if not Actions.valid_arguments(arg):

            return



        obj = Actions.object_exists(arg)

        if not obj:

            return



        print(obj)



    @staticmethod

    def destroy(arg):

        """Destroy an instance"""

        if not Actions.valid_arguments(arg):

            return



        obj = Actions.object_exists(arg)

        if not obj:

            return



        storage.delete(arg[0], arg[1])

        storage.save()



    @staticmethod

    def all(arg):

        """Prints string representation of all instances based"""

        if not arg:

            print(storage.get_objects())

            return



        class_name = arg[0]

        if not Actions.class_exists(class_name):

            print('** class doesn\'t exist **')

            return



        print(storage.get_objects(class_name))



    @staticmethod

    def update(arg):

        """Update an instance"""

        if not Actions.valid_arguments(arg):

            return



        obj = Actions.object_exists(arg)

        if not obj:

            return



        attribute = Actions.tuple2value(arg, 2)

        if not attribute:

            print('** attribute name missing **')

            return



        value = Actions.tuple2value(arg, 3)

        if not value:

            print('** value missing **')

            return

        # 0         1                           2          3    4     5

        # email "aibnb@holbertonschool.com" first_name "Betty" test "lol"

        cast_type = type(attribute).__name__

        value = eval('{}(value)'.format(cast_type))



        values = arg[2:]

        for idx in range(0, len(values), 2):

            setattr(obj, values[idx], values[idx + 1].lstrip('"').rstrip('"'))



        storage.save()



    @staticmethod

    def get_function(action, path=None):

        """Return the function that do the action"""

        actions = {'all': Actions.all, 'count': Actions.count,

                   'show': Actions.show, 'destroy': Actions.destroy,

                   'update': Actions.update}



        if action not in set(actions.keys()):

            print('*** Unknown syntax: {}'.format(path))

            return None



        return actions.get(action)



    @staticmethod

    def count(class_name):

        """Retrieve the number of instances of a class: <class name>.count()"""

        objects = storage.get_objects(class_name[0])

        length = len(objects)

        print(length)



    @staticmethod

    def default(arg):

        """Handle default cmd"""

        path = arg[0]

        if '.' not in path:

            print('*** Unknown syntax: {}'.format(path))

            return



        class_name, action = path.split('.')

        if not Actions.class_exists(class_name):

            print('** class doesn\'t exist **')

            return



        if not action:

            print('*** Unknown syntax: {}'.format(path))

            return



        action, arguments = Utils.split_action(arg)



        act = Actions.get_function(action, arg[0])

        if not act:

            return



        act(arguments)
