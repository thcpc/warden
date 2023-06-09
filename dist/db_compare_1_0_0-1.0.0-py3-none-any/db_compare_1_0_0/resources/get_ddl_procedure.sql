DROP PROCEDURE IF EXISTS GET_DDL;
DELIMITER $$
SET FOREIGN_KEY_CHECKS = 0;
CREATE PROCEDURE GET_DDL(IN name varchar(200))
BEGIN

  SET @stmt=CONCAT('SHOW CREATE TABLE ', name);
  PREPARE STMT FROM @stmt;
    execute STMT;
  DEALLOCATE PREPARE STMT;

END $$
DELIMITER ;