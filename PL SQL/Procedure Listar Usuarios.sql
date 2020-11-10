CREATE OR REPLACE PROCEDURE SP_LISTAR_USUARIOS (usuarios out SYS_RECURSOR)
IS

BEGIN

    OPEN usuarios FOR SELECT username, first_name || ' ' || last_name as " Nombre", is_active
                      FROM usuarios_usuarios;

END;