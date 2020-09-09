# coding: utf-8

class Zone():
    """
        Model for zone table on database
    """

    def __init__(self, id, name):
        """
            Constructor
        """

        # native properties
        self.id = id
        self.name = name
        