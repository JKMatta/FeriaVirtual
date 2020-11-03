CREATE OR REPLACE PROCEDURE SP_LISTAR_PEDIDOS (pedido OUT SYS_REFCURSOR)
IS

BEGIN

    OPEN pedido FOR SELECT p.tipo, p.fecha, p.descrip, u.username 
                    FROM pedido p INNER JOIN usuarios_usuarios u 
                    ON p.usuarios_usuarios_id_user = u.id_user;

END;
