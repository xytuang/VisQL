from typing import List, Optional

from visql.models.column import Column
from visql.models.mark import Mark
from visql.models.queryable import Queryable


class Table(Queryable):
    """
    A class that represents a table in a database.
    Extends the Queryable class to provide functionality for querying the table.

    Args:
        Queryable (_type_): _description_
    """
    def __init__(self, table_name: str, columns: List[Column]):
        """Creates a Table object

        Args:
            table_name (str): The logical name of this table. Assume this is the name of the table in the database,and is unique.
            columns (List[Column]): The columns of this table
        """
        pass

    def get_table_name(self) -> str:
        pass

    def get_column(self, column_name: str) -> Optional[Column]:
        pass

    def build_query(self):
        """Builds a query based on the table's columns and properties.
        """
        return super().build_query()

    def rect(self, encodings, layout_algorithm) -> Mark:
        """Returns a Rectangle mark
        
        Returns:
            tuple: A tuple representing the rectangle (x, y, width, height).
        """
        return (0, 0, 0, 0)