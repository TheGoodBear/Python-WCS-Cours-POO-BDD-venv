# coding: utf-8

import Variables as var


class Type():
    """
        Model for type table in database
    """

    def __init__(self,
        id, name, id_parent):
        """
            Constructor  
        """

        # native properties
        self.id = id
        self.name = name
        self.id_parent = id_parent
        
        # calculated properties

        # self.parent = [
        #     my_type.name
        #     for my_type
        #     in var.types
        #     if my_type.id == self.id_parent][0]