class Join:
    def __init__(self, left: Queryable, right: Queryable, on: List[Column], mark: Optional[Mark] = None):
        self.left = left
        self.right = right
        self.on = on
        self.mark = mark

    def __repr__(self):
        return f"Join(left={self.left}, right={self.right}, on={self.on}, mark={self.mark})"