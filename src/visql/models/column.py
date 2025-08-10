from typing import Any, Type

from visql.db.coerce_type import coerce_type


class Column:
    def __init__(self, column_name: str, column_type: Type[Any], key: str):
        """_summary_

        Args:
            column_name (str): The name of this column
            column_type (Type[Any]): The type of this column
            key (_type_): Indicates if this column is a key
        """
        self.column_name = column_name
        self.column_type = coerce_type(column_type)
        self.key = False if key is None else True

    def get_column_name(self) -> str:
        """Returns the name of this column

        Returns:
            str: The name of this column
        """
        return self.column_name

    def is_key(self) -> bool:
        """Returns whether this column is a primary key

        Returns:
            bool: True if this column is a primary key, False otherwise
        """
        return self.key

    def __repr__(self) -> str:
        """Returns the string representation of this Column

        Returns:
            str: _description_
        """
        return f"column_name: {self.column_name} column_type: {self.column_type} key: {self.key}"

    def __eq__(self, other: object) -> bool:
        """Checks if two Column objects are equal

        Args:
            other (object): The other object to compare with

        Returns:
            bool: True if both objects are equal, False otherwise
        """
        if not isinstance(other, Column):
            return False
        return (
            self.column_name == other.column_name
            and self.column_type == other.column_type
            and self.key == other.key
        )