CREATE OR replace PROCEDURE SP_LISTAR_PRODUCTOS (productos OUT SYS_REFCURSOR)
IS

BEGIN

    OPEN productos FOR SELECT p.nom_prod, p.precio_prod, p.stock_prod, u.username
                       FROM productos p INNER JOIN usuarios_usuarios u 
                       ON p.usuarios_usuarios_id_user = u.id_user;

END;