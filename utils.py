#!/usr/bin/python3
""""
Module helper"""

import json





class Utils:

    """Toolbox for parsing"""



    @staticmethod

    def split_action(line):

        """Converts a string into a tuple of arguments"""

        # action [class_name, id]

        arguments = []



        line = ' '.join(line)

        arguments.append(Utils.get_class(line))



        action, parameters = Utils.extract_parameters(line)

        id_obj = Utils.get_id(parameters)

        arguments.append(id_obj)



        dictionary = Utils.extract_dictionary(parameters)

        if dictionary:

            arguments.extend(dictionary)

            return action, tuple(arguments)



        if id_obj:

            start = line.find(id_obj) + len(id_obj)

            arg = Utils.extract_parameters2(line[start:])

            if arg:

                arguments.extend(arg)



        return action, tuple(arguments)



    @staticmethod

    def get_class(line):

        """Extracts the class_name in the string"""

        return line.split('.')[0]



    @staticmethod

    def get_id(line):

        """Get the id in the string"""

        if not line:

            return None

        tmp = line.split(',')

        return tmp[0].strip('",\'')



    @staticmethod

    def extract_parameters(line):

        """Extracts parameters in a string"""

        # User.action()

        start_action = line.find('.') + 1

        start = line.find('(')

        end = (line[start:].find(')')) + start



        action = line[start_action:start]

        if (start + 1) == end:

            return action, None



        return action, line[start + 1: end]



    @staticmethod

    def extract_parameters2(line):

        """Extracts extra parameters"""

        arg = []

        if not line:

            return None



        line = line.strip('", )')

        parameters = line.split(' ')

        for p in parameters:

            arg.append(p.strip(' ",'))



        return arg



    @staticmethod

    def extract_dictionary(line):

        """Extract a string dictionary from a string"""

        if not line:

            return None



        idx_start = line.find('{')

        if idx_start == -1:

            return None



        idx_end = line[idx_start:].find('}') + idx_start + 1



        return Utils.dictionary2list(line[idx_start: idx_end])



    def dictionary2list(dictionary):

        """Converts a dictionary into a list"""

        params = []



        dictionary = eval(dictionary)

        for k, v in dictionary.items():

            params.append(str(k))

            params.append(str(v))



        return params
