CREATE TABLE Paciente (
 ID_Paciente INT PRIMARY KEY IDENTITY(1,1),
 Nome VARCHAR(50) NOT NULL,
 Data_Nascimento DATE NOT NULL,
 Endereco VARCHAR(50) NOT NULL,
 Telefone VARCHAR(13),
 Email VARCHAR(50) NOT NULL
);

CREATE TABLE Fisioterapeuta (
 ID_Fisioterapeuta INT PRIMARY KEY IDENTITY(1,1),
 Nome VARCHAR(50) NOT NULL,
 Especialidade VARCHAR(50) NOT NULL,
 Telefone VARCHAR(13),
 Email VARCHAR(50) NOT NULL
);

CREATE TABLE Usuario (
 ID_Usuario INT PRIMARY KEY IDENTITY(1,1),
 Nome VARCHAR(50) NOT NULL,
 Username VARCHAR(50) NOT NULL,
 Senha VARCHAR(50) NOT NULL,
 Nivel_Acesso CHAR(1) NOT NULL CONSTRAINT chk_nvl CHECK (Nivel_Acesso IN ('V', 'B', 'A'))
 );

CREATE TABLE Agendamento (
 ID_Agendamento INT PRIMARY KEY IDENTITY(1,1),
 ID_Paciente INT NOT NULL,
 ID_Fisioterapeuta INT NOT NULL,
 Data_Hora DATETIME NOT NULL,
 Duracao TIME NOT NULL,
 Observacoes TEXT,
 FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
 FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeuta(ID_Fisioterapeuta)
);

CREATE TABLE HistoricoMedico (
 ID_HistoricoMedico INT PRIMARY KEY IDENTITY(1,1),
 ID_Paciente INT NOT NULL,
 DataConsulta DATE NOT NULL,
 Diagnostico TEXT NOT NULL,
 TratamentoAnterior TEXT,
 FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Tratamento (
 ID_Tratamento INT PRIMARY KEY IDENTITY(1,1),
 ID_Paciente INT NOT NULL,
 ID_Fisioterapeuta INT NOT NULL,
 Data_Inicio DATE NOT NULL,
 Data_Fim DATE NOT NULL,
 Diagnostico TEXT NOT NULL,
 Procedimentos TEXT,
 FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente),
 FOREIGN KEY (ID_Fisioterapeuta) REFERENCES Fisioterapeuta(ID_Fisioterapeuta)
);

CREATE TABLE Pagamento (
 ID_Pagamento INT PRIMARY KEY IDENTITY(1,1),
 ID_Paciente INT NOT NULL,
 Valor DECIMAL(10,2) NOT NULL,
 Data_Pagamento DATE NOT NULL,
 Metodo_Pagamento CHAR(1) NOT NULL CONSTRAINT chk_pag CHECK (Metodo_Pagamento IN  ('C', 'D', 'E', 'P')),
 FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);

CREATE TABLE Relatorio (
 ID_Relatorio INT PRIMARY KEY IDENTITY(1,1),
 ID_Paciente INT NOT NULL,
 Conteudo TEXT NOT NULL,
 Data_Criacao DATE NOT NULL,
 FOREIGN KEY (ID_Paciente) REFERENCES Paciente(ID_Paciente)
);