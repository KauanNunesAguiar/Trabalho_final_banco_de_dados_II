## Projeto Sistema de Atendimento fisioterapia

### Grupo E

### Integrantes
Kauan Nunes Aguiar - @KauanNunesAguiar<br>
Michel Almeida da Rosa - @L3mitch<br>
Elias Enns - @EliasEnns<br>
Yuri Mazzuchello Candiotto - @Yuri-Candiotto<br>
Suyane Bonfanti dos Santos - @suyane924<br>

### Modelo Físico
Responsável: @Yuri-Candiotto<br>
Utilizamos a ferramenta de modelagem de dados [dbdiagram.io](https://dbdiagram.io/) para criação do modelo físico do banco de dados, para posterior exportação dos scripts DDL das tabelas e relacionamentos.<br>
Arquivo fonte: [Modelo Fisico](https://dbdiagram.io/d/656e62bf56d8064ca0604658).<br>

![ModeloFisico-PDF](https://github.com/KauanNunesAguiar/Trabalho_final_banco_de_dados_II/assets/141968186/cc277aae-dc14-4e84-b2be-ad883ffb099f)


### Dicionário de Dados
Responsável: @suyane924<br>
As informações sobre as tabelas e índices foram documentados na planilha [Dicionario-de-Dados.xlsx](dicionario_dados/Dicionario-de-Dados.xlsx).

### Scripts SQL
Para este projeto foi utilizado o banco de dados [SQL Server 2022](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads) <br>
Este é o procedimento para criação do banco de dados [SQL Server usando o SQL Server Management Studio ou o Transact-SQL](https://learn.microsoft.com/pt-br/sql/relational-databases/databases/create-a-database?view=sql-server-ver16) <br>

Abaixo, segue os scripts SQL separados por tipo:
#### DDL 
+ Link: [ddl.sql](scripts_sql/scripts_ddl.sql)
+ Responsável: @Yuri-Candiotto
#### DML 
+ Link: [dml.sql](scripts_sql/scripts_dml.sql)
+ Responsável: @EliasEnns
#### Índices 
+ Link: [indices.sql](consultasComIndices)
+ Responsável: @L3mitch
#### Triggers 
+ Link: [triggers.sql](scripts_sql/Final.sql)
- Responsável: @L3mitch
#### Stored Procedures
+ Link: [stored_procedures.sql](scripts_sql/Final.sql)
+ Responsável: @L3mitch
#### Functions 
+ Link: [functions.sql](scripts_sql/Final.sql)
+ Responsável: @L3mitch

### Código Fonte do CRUD
- Linguagem de Programação: Phyton
- Biblioteca: SQLAlchemy
- Link: [Codigo Fonte](codigo_CRUD/main.py)
- Responsável: @KauanNunesAguiar

### Relatório Final
O relatório final está disponível no arquivo [template1.docx](relatorio/template1.docx).
