from enum import Enum

class ConstraintType(Enum):
    """
    Enum representing different types of constraints.
    """
    PRIMARY_KEY = 0
    FOREIGN_KEY = 1
    UNIQUE = 2

class Constraint:
    """
    Base class for constraints.
    """
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Constraint(name={self.name})"

    def is_valid(self, *args, **kwargs) -> bool:
        """
        Check if the constraint is valid.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")