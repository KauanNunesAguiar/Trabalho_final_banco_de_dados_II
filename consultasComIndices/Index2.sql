--create index idx_Data_Hora on Agendamento (Data_Hora) include (ID_Agendamento, Duracao, ID_Paciente, ID_Fisioterapeuta)

select ID_Agendamento, ID_Fisioterapeuta, ID_Paciente, Duracao, Data_Hora from Agendamento where Data_Hora between '01-05-2023' and ' 31-05-2023' order by Data_Hora

--drop index idx_Data_Hora on Agendamento