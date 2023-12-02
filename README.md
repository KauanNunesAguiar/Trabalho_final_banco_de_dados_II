## Projeto Sistema de Atendimento fisioterapia

### Grupo E

### Integrantes:
Kauan Nunes Aguiar - @KauanNunesAguiar<br>
Michel Almeida da Rosa - @L3mitch<br>
Elias Enns - @EliasEnns<br>
Yuri Mazzuchello Candiotto - @Yuri-Candiotto<br>
Suyane Bonfanti dos Santos - @suyane924<br>



### Modelo Físico
Responsável: @Yuri-Candiotto<br>
Utilizamos a ferramenta de modelagem de dados [dbdiagram.io](https://dbdiagram.io/) para criação do modelo físico do banco de dados, para posterior exportação dos scripts DDL das tabelas e relacionamentos.<br>
Arquivo fonte: [Modelo Fisico](https://dbdiagram.io/d/6561325e3be1495787b1c71a).<br>

![image](https://github.com/jlsilva01/projeto_final_bd2_satc_2023/assets/484662/1fefa9fd-868c-4209-8cc5-d32cd73fa46d)

### Dicionário de Dados
Responsável: @suyane924<br>
As informações sobre as tabelas e índices foram documentados na planilha [template1.xlsx](dicionario_dados/template1.xlsx).

### Scripts SQL
Para este projeto foi utilizado o banco de dados [SQL Server 2022](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads) <br>
Este é o procedimento para criação do banco de dados [SQL Server usando o SQL Server Management Studio ou o Transact-SQL](https://learn.microsoft.com/pt-br/sql/relational-databases/databases/create-a-database?view=sql-server-ver16) <br>

Abaixo, segue os scripts SQL separados por tipo:
+ DDL [ddl.sql](scripts_sql/ddl.sql)<br>
- Responsável: @Yuri-Candiotto<br>
+ Índices [indices.sql](scripts_sql/indices.sql)<br>
- Responsável: TBD<br>
+ DML [dml.sql](scripts_sql/dml.sql)<br>
- Responsável: @EliasEnns<br>
+ Triggers [triggers.sql](scripts_sql/triggers.sql)<br>
- Responsável: @L3mitch<br>
+ Stored Procedures [stored_procedures.sql](scripts_sql/stored_procedures.sql)<br>
- Responsável: @L3mitch<br>
+ Functions [functions.sql](scripts_sql/functions.sql)<br>
- Responsável: @L3mitch<br>


### Scripts DDL Criação do Database:
Responsável: @Yuri-Candiotto<br>
Banco de dados utilizado SQL Server versão 2022 - Azure<br>
<code>1 arquivo SQL por objeto</code>

### Scripts Popula tabelas:
Responsável: @EliasEnns<br>
<code>1 arquivo SQL por objeto</code>

### Objetos de BD (stored procedure, triggers e functions):
Responsável: @L3mitch<br>
<code>1 arquivo SQL por objeto</code>

### Código Fonte do CRUD
- Linguagem de Programação C# .NET.<br>
- Framework .NET 4.6
- Projeto Windows Forms
- Biblioteca Entity Framework para SQL Server (nativo)

[Codigo Fonte](fonte/)

### Relatório Final
O relatório final está disponível no arquivo [template1.docx](relatorio/template1.docx).

### Código do sistema:
Responsável: @KauanNunesAguiar<br>
Linguagem de Programação Python<br>
Biblioteca: SQLAlchemy<br>
<code>código fonte da aplicação</code>
