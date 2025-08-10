from visql.models.table import Table
from visql.models.mark import Mark

class VisQL:
    """
    A class that represents a VisQL object, which can contain tables and marks.
    Provides methods to add tables and marks, and to build queries based on them.
    """
    
    def __init__(self):
        """Initializes the VisQL object with empty lists for tables and marks."""
        self.marks = []

    def add_mark(self, mark: Mark):
        """Adds a mark to the VisQL object.

        Args:
            mark (Mark.Mark): The mark to be added.
        """
        self.marks.append(mark)

    def render(self):
        """Renders the VisQL object by returning its marks.

        Returns:
            list: A list of marks contained in the VisQL object.
        """
        return self.marks

