--create index idx_Historico on HistoricoMedico (DataConsulta) include (ID_HistoricoMedico, ID_Paciente)

select ID_HistoricoMedico, ID_Paciente, DataConsulta, Diagnostico, TratamentoAnterior from HistoricoMedico where DataConsulta between '01-05-2023' and ' 31-05-2023' order by DataConsulta

--drop index idx_Historico on HistoricoMedico