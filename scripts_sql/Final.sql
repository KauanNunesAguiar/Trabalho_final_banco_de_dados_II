CREATE FUNCTION ContPag (@tipo VARCHAR(1))
RETURNS INT
AS
BEGIN
    DECLARE @numero INT;
    SELECT @numero = COUNT(Metodo_Pagamento) FROM Pagamento WHERE Metodo_Pagamento = @tipo;
    RETURN @numero;
END;

DECLARE @contagem INT;
EXEC @contagem = ContPag 'p';
SELECT @contagem;

--DROP FUNCTION ContPag;

CREATE PROC eptChk AS
BEGIN
	update Tratamento set Procedimentos = 'Fisioterapeuta não escreveu nenhum procedimento, em caso de dúvidas envie um E-mail para: doloris.fisioterapia@gmail.com'
	where Procedimentos IS NULL
END

--DROP PROCEDURE eptChk;

CREATE PROCEDURE NameFis 
    @Pes VARCHAR(255), 
    @Enc VARCHAR(255) OUTPUT
AS
BEGIN
    SELECT @Enc = Nome FROM Fisioterapeuta
    WHERE Nome = @Pes;
END;

DECLARE @Pes VARCHAR(255), @Enc VARCHAR(255);

EXEC NameFis 'Ana Pereira', @Enc OUTPUT;

SELECT @Enc;


--DROP PROCEDURE NameFis;

create trigger upd_seg on usuario for update
as
declare @count int

begin
	select @count = count(*) from inserted
	if (@count > 1)
	begin
		raiserror(N'OPERAÇÃO NÃO PERMITIDA', 16, 0, @count)
		rollback tran
	end
end

select * from usuario

begin tran
update Usuario set nome = 'NomeErrado' where nome like '%'
rollback

--DROP TRIGGER upd_seg ON usuario;
