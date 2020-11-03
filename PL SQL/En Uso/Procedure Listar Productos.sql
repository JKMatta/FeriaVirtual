create or replace PROCEDURE SP_LISTAR_PRODUCTOS (productos out SYS_REFCURSOR)
IS

BEGIN

    OPEN productos FOR SELECT p.nom_prod, p.precio_prod, p.stock_prod, u.username
                       FROM productos p INNER JOIN usuarios_usuarios u 
                       ON p.usuarios_usuarios_id_user = u.id_user;

END;