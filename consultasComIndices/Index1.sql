--create index idx_Data_Nascimento on Paciente (Data_Nascimento) include (ID_Paciente, Nome, Endereco, Telefone, Email)


select ID_Paciente, Nome, Data_Nascimento, Email from Paciente where Data_Nascimento between '01-01-1985' and ' 01-01-2000' order by ID_Paciente

--drop index idx_Data_Nascimento on Paciente