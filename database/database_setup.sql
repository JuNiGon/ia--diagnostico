CREATE TABLE Doencas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    relevancia INTEGER
);

CREATE TABLE Sintomas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

CREATE TABLE Doenca_Sintoma (
    doenca_id INTEGER,
    sintoma_id INTEGER,
    peso INTEGER,
    FOREIGN KEY (doenca_id) REFERENCES Doencas(id),
    FOREIGN KEY (sintoma_id) REFERENCES Sintomas(id)
);
