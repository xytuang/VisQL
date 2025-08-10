

from abc import abstractmethod


class Queryable:
    """
    A class that represents a queryable object with dependencies.
    This class is designed to be extended by other classes that require
    queryable functionality.

    Attributes:
        dependencies (list): A list of dependencies for this queryable object.
    """
    def __init__(self):
        """Creates a Queryable object
        """
        self.dependencies = []
        pass

    def add_dependency(self, dependency):
        """Adds a dependency to this queryable object
        """
        if dependency not in self.dependencies:
            self.dependencies.append(dependency)

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def build_query(self):
        """Builds a query based on the dependencies and properties of this object.
        
        Returns:
            str: The SQL query string.
        """
        raise NotImplementedError("Subclasses must implement this method.")


