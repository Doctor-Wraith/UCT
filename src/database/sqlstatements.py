
CREATE_TABLE = {
    "atom": """
        CREATE TABLE IF NOT EXISTS atom (
        atom_id     TEXT    NOT NULL    PRIMARY KEY,
        atom_name   TEXT    NOT NULL    UNIQUE
        )
        """,
    "tuning": """
        CREATE TABLE IF NOT EXISTS tuning (
        tuning_id      TEXT         NOT NULL    PRIMARY KEY,
        name            TEXT        NOT NULL,
        surface_id      TEXT,
        adsorbate_1_id  TEXT,
        adsorbate_2_id  TEXT,
        adsorbate_3_id  TEXT,
        energy          REAL        NOT NULL,
        outcar_path     TEXT        NOT NULL,
        training         BOOLEAN     NOT NULL,
        FOREIGN KEY(surface_id)     REFERENCES atom(atom_id),
        FOREIGN KEY(adsorbate_1_id) REFERENCES atom(atom_id),
        FOREIGN KEY(adsorbate_2_id) REFERENCES atom(atom_id),
        FOREIGN KEY(adsorbate_3_id) REFERENCES atom(atom_id)
        )
        """,
    "position": """
        CREATE TABLE IF NOT EXISTS position (
        position_id     TEXT    NOT NULL    PRIMARY KEY,
        atom_id         TEXT    NOT NULL,
        tuning_id      TEXT     NOT NULL,
        x               REAL    NOT NULL,
        y               REAL    NOT NULL,
        z               REAL    NOT NULL,
        position_type   TEXT    NOT NULL,
        FOREIGN KEY(atom_id)    REFERENCES atom(atom_id),
        FOREIGN KEY(tuning_id)  REFERENCES tuning(tuning_id)
        )
        """,
    "force": """
        CREATE TABLE IF NOT EXISTS force (
        force_id        TEXT    NOT NULL    PRIMARY KEY,
        atom_id         TEXT    NOT NULL,
        tuning_id      TEXT    NOT NULL,
        x               REAL    NOT NULL,
        y               REAL    NOT NULL,
        z               REAL    NOT NULL,
        FOREIGN KEY(atom_id)    REFERENCES atom(atom_id),
        FOREIGN KEY(tuning_id)  REFERENCES tuning(tuning_id)
        )
        """
}

ADD_ITEMS = {
    "atom": """
        INSERT INTO atom VALUES (?,?)
    """,
    "tune": """
        INSERT INTO tuning VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    "position": """
        INSERT INTO position VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    "force": """
        INSERT INTO force VALUES  (?, ?, ?, ?, ?, ?)
    """
}

SEARCH_IDS = {
    "atom": """
        SELECT atom_id FROM atom where atom_name = ?
    """
}

SEARCH_OUTCAR_PATH = """SELECT tuning_id FROM tuning WHERE outcar_path = ?"""

SEARCH_OUTCAR_TRAIN_PATH = """
        SELECT outcar_path from tuning WHERE training = ?
"""

SEARCH_OUTCAR_ENERGY = """
        SELECT energy, outcar_path from tuning WHERE training = ?
"""
