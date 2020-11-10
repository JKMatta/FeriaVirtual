create or replace PROCEDURE SP_LISTAR_PEDIDOS (pedido OUT SYS_REFCURSOR)
IS

BEGIN

    OPEN pedido FOR SELECT p.tipo, p.fecha, p.descrip, u.username, p.estado_admin
                    FROM pedido p INNER JOIN usuarios_usuarios u 
                    ON p.usuarios_usuarios_id_user = u.id_user;

END;