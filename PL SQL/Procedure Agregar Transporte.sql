CREATE OR replace PROCEDURE SP_AGREGAR_TRANSPORTE(
    v_tip_transporte VARCHAR2,
    v_tamano NUMBER,
    v_capacidad NUMBER,
    v_refrigeracion VARCHAR2,
    v_fecha DATE,
    v_user_id NUMBER,
    v_salida OUT NUMBER
)
IS 

BEGIN

    INSERT INTO transporte (tip_transporte, tamano_trans, capacidad_trans, refrigeracion_trans, fecha_trans, usuarios_usuarios_id_user)
    VALUES (v_tip_transporte, v_tamano, v_capacidad, v_refrigeracion, v_fecha, v_user_id);
    COMMIT;

    v_salida := 1;

    EXCEPTION
    WHEN OTHERS THEN
        v_salida := 0;

END;