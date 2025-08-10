from visql.models.queryable import Queryable

class Mark(Queryable):
    """
    A class that represents a Mark in a visualization.
    Extends the Queryable class to provide functionality for querying the mark.

    Args:
        Queryable (_type_): _description_
    """
    def __init__(self, source_table, encoding, layout):
        """Initializes the Mark with a source table, encoding, and layout.
        Args:
            source_table (str): The name of the source table for the mark.
            encoding (dict): A dictionary representing the encoding of the mark.
            layout (dict): A dictionary representing the layout of the mark.
        """
        self.source_table = source_table
        self.encoding = encoding
        self.layout = layout
        super().__init__()

    def build_query(self):
        """Builds a query based on the mark's properties.
        """
        return super().build_query()