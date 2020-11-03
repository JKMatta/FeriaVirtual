CREATE OR REPLACE PROCEDURE SP_AGREGAR_USUARIOS (
    v_username varchar2,
    v_email varchar2,
    v_first_name varchar2,
    v_last_name varchar2,
    v_direccion varchar2,
    v_salida out number
)

IS

BEGIN

    INSERT INTO USUARIOS_USUARIOS(USERNAME, EMAIL, FIRST_NAME, LAST_NAME, DIRECCION)
    VALUES (v_username, v_email, v_first_name, v_last_name, v_direccion);
    
    COMMIT;
    v_salida := 1;
    
    EXCEPTION
    WHEN OTHERS THEN 
        v_salida := 0;
END;