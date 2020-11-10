CREATE OR replace PROCEDURE SP_SOLI_PEDIDOS(
    v_tipo varchar2,
    v_fecha DATE,
    v_desc VARCHAR2,
    v_user_id NUMBER,
    v_salida OUT NUMBER
)
IS 

BEGIN

    INSERT INTO pedido (tipo, fecha, descrip, usuarios_usuarios_id_user)
    VALUES (v_tipo, v_fecha, v_desc, v_user_id);
    COMMIT;

    v_salida := 1;

    EXCEPTION
    WHEN OTHERS THEN
        v_salida := 0;

END;