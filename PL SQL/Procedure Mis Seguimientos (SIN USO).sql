CREATE OR REPLACE PROCEDURE SP_MIS_SEGUIMIENTOS (segui OUT SYS_REFCURSOR)
IS

BEGIN

    OPEN segui FOR SELECT p.tipo, s.est_seguimiento 
                   FROM pedido p INNER JOIN seguimiento s
                   ON p.id_ped = s.pedido_id_ped;

END;