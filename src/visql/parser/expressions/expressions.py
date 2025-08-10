class Expr:
    def __init__(self, name):
        pass


class RowProxy:
    def __init__(self):
        """
        Initializes a new RowProxy object.
        Each RowProxy object stores the columns accessed per row.
        The RowProxy is meant to be passed to functions that take in a row as the only parameter.
        """
        self.accesses = []

    def __getattr__(self, name: str):
        """Returns an Expr when called with a Lambda

        Args:
            name (str): The name of the attribute being accessed
        """
        self.accesses.append(name)
        return Expr(name)
