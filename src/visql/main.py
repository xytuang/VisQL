from visql.db.connector import Connector

if __name__ == "__main__":
    print("We are alive!")
    conn = Connector()
    conn.execute(
        """
    CREATE TABLE users (
        id INTEGER,
        name VARCHAR,
        date_created INT,
        age INTEGER,
        PRIMARY KEY(name, date_created)
    )
    """
    )
    conn.execute(
        """
    INSERT INTO users VALUES
    (1, 'Alice', 1, 30),
    (2, 'Bob', 2, 25),
    (3, 'Charlie', 3, 35)
    """
    )
    columns = conn.describe_table("users")
    for column in columns:
        print(repr(column))
    print("Finish!")
