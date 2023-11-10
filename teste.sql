-- Implemente um gatilho no banco de dados que dispara toda vez que um Tripulante ´e cadastrado ou quando o atributo “funcao” tem seu valor modificado. O gatilho deve garantir que somente um dos tripulantes tenha a fun¸c˜ao “Capit˜ao”.
CREATE OR REPLACE TRIGGER check_capitao
BEFORE INSERT OR UPDATE OF funcao ON Tripulante
FOR EACH ROW
DECLARE
  existing_capitao INTEGER;
BEGIN
  IF :NEW.funcao = 'Capitão' THEN
    SELECT COUNT(*) INTO existing_capitao FROM Tripulante WHERE funcao = 'Capitão';
    IF existing_capitao > 0 THEN
      RAISE_APPLICATION_ERROR(-20001, 'There can only be one Capitão');
    END IF;
  END IF;
END;