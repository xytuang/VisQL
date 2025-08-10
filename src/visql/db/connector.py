from typing import List, Optional

import duckdb

from visql.models.column import Column


class Connector:
    def __init__(self):
        """Creates a new connection to in-memory DuckDB"""
        self.conn = duckdb.connect()

    def execute(self, sql: str) -> list:
        """Executes a SQL query

        Args:
            sql (str): The query to execute

        Returns:
            list: Results of the executed query
        """
        return self.conn.execute(sql).fetchall()

    def describe_table(self, table: str) -> List[Column]:
        """_summary_

        Args:
            table (str): The name of the table to describe

        Returns:
            List[Column]: A list of Columns for the table
        """
        sql = f"DESCRIBE {table};"
        rows = self.execute(sql)
        columns = []
        for row in rows:
            column_name = row[0]
            column_type = row[1]
            key = row[3]
            columns.append(
                Column(column_name=column_name, column_type=column_type, key=key)
            )
        return columns

    def shutdown(self):
        """Closes the connection to DuckDB"""
        self.conn.close()
