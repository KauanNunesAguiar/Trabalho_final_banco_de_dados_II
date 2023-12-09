-- Quais pacientes possuem uma idade maior que 50 anos?

WITH Idades AS (
    SELECT ID_Paciente, Nome, Data_Nascimento, FLOOR(DATEDIFF(DAY, Data_Nascimento, GETDATE()) / 365.25) AS idade 
    FROM Paciente
)
SELECT * FROM Idades WHERE idade > 50;

-- Qual o método de pagamento mais utilizado pelos pacientes?
SELECT 
    CASE Metodo_Pagamento
        WHEN 'C' THEN 'Crédito'
        WHEN 'D' THEN 'Débito'
        WHEN 'E' THEN 'Extrato'
        WHEN 'P' THEN 'Pix'
        ELSE 'Desconhecido'
    END AS Metodo_Pagamento_Nome,
    COUNT(*) AS Quantidade
FROM Pagamento
GROUP BY Metodo_Pagamento
ORDER BY Quantidade DESC;

-- Quais pacientes possuem uma idade maior que 50 anos?

WITH Idades AS (
    SELECT ID_Paciente, Nome, Data_Nascimento, FLOOR(DATEDIFF(DAY, Data_Nascimento, GETDATE()) / 365.25) AS idade 
    FROM Paciente
)
SELECT * FROM Idades WHERE idade > 50;

-- Qual o método de pagamento mais utilizado pelos pacientes?
SELECT 
    CASE Metodo_Pagamento
        WHEN 'C' THEN 'Crédito'
        WHEN 'D' THEN 'Débito'
        WHEN 'E' THEN 'Extrato'
        WHEN 'P' THEN 'Pix'
        ELSE 'Desconhecido'
    END AS Metodo_Pagamento_Nome,
    COUNT(*) AS Quantidade
FROM Pagamento
GROUP BY Metodo_Pagamento
ORDER BY Quantidade DESC;

--Quantos pacientes não possuem um procedimento de tratamento?
select count(ID_Tratamento) 
from Tratamento 
where Procedimentos IS NULL
