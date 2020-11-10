CREATE OR replace PROCEDURE SP_AGREGAR_PRODUCTOS(
    v_nombre VARCHAR2,
    v_precio NUMBER,
    v_desc VARCHAR2,
    v_stock NUMBER,
    v_user_id NUMBER,
    v_salida OUT NUMBER
)
IS 

BEGIN

    INSERT INTO productos (nom_prod, precio_prod, desc_prod, stock_prod, usuarios_usuarios_id_user)
    VALUES (v_nombre, v_precio, v_desc, v_stock, v_user_id);
    COMMIT;

    v_salida := 1;

    EXCEPTION
    WHEN OTHERS THEN
        v_salida := 0;

END;