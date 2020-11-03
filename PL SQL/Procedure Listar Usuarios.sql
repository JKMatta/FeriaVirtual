CREATE OR REPLACE PROCEDURE SP_LISTAR_USUARIOS (usuarios out SYS_RECURSOR)
IS

BEGIN

    OPEN usuarios FOR SELECT first_name, last_name, username, email, tipo_usuario FROM usuarios_usuarios;

END;