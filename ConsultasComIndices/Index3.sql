--create index idx_Relatorio on Relatorio (Data_Criacao) include (ID_Relatorio, ID_Paciente)

select ID_Relatorio, ID_Paciente, Data_Criacao, Conteudo from Relatorio where Data_Criacao between '01-05-2023' and ' 31-05-2023' order by Data_Criacao

--drop index idx_relatorio on relatorio