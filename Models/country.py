# coding: utf-8

class Country():
    """
        Model for country table on database
    """

    def __init__(self, id, name):
        """
            Constructor
        """

        # native properties
        self.id = id
        self.name = name
