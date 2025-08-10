import unittest
from visql.models.column import Column

class TestColumn(unittest.TestCase):
    def test_column_init(self):
        col = Column(column_name="id", column_type="int", key=None)
        self.assertEqual(col.column_name, "id")
        self.assertEqual(col.column_type, int)

    def test_column_repr(self):
        col = Column(column_name="age", column_type="float", key=None)
        self.assertIn("age", repr(col))
        self.assertIn("float", repr(col))

    def test_column_equality(self):
        col1 = Column(column_name="name", column_type="str", key=None)
        col2 = Column(column_name="name", column_type="str", key=None)
        self.assertEqual(col1, col2)

if __name__ == "__main__":
    unittest.main()