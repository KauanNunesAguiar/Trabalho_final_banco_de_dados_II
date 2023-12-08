CREATE FUNCTION ContPag (@tipo VARCHAR)
RETURNS INT
AS
BEGIN
    DECLARE @numero INT;
    SELECT @numero = COUNT(Metodo_Pagamento) FROM Pagamento WHERE Metodo_Pagamento = @tipo;
    RETURN @numero;
END;


create proc NameFis (@Pes varchar, @Enc varchar output) as
begin
	select @Enc = Nome from Fisioterapeuta
	where Nome = @Pes
	select @Enc
end


declare @Pes varchar, @Enc varchar

exec testSaida 'Ana Pereira', @Enc output

select @Enc

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
update Usuario set nome = 'burro' where nome like 'pedro%'
rollback