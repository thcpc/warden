sql = """
LOCK TABLES `eclinical_edc_database_owner` WRITE;
/*!40000 ALTER TABLE `eclinical_edc_database_owner` DISABLE KEYS */;
INSERT INTO `eclinical_edc_database_owner` VALUES (2,24,58);
/*!40000 ALTER TABLE `eclinical_edc_database_owner` ENABLE KEYS */;
UNLOCK TABLES;
"""
procedure_sql="""
CREATE PROCEDURE GET_DDL(IN name varchar(200))
BEGIN

  SET @stmt=CONCAT('SHOW CREATE TABLE ', name);
  PREPARE STMT FROM @stmt;
    execute STMT;
  DEALLOCATE PREPARE STMT;

END
"""

commit_sqls = [sql]