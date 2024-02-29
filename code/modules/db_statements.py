TABLE_A = "A"
TABLE_B = "B"

CREATE_TABLE_STATEMENT = f"""
Create TABLE if not exists {TABLE_A} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    date BLOB,
);

Create TABLE if not exists {TABLE_B} (
    id INTEGER,
    new_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date BLOB,
    text TEXT,
    FOREIGN KEY (new_id) REFERENCES {TABLE_A} (id)
);
"""
