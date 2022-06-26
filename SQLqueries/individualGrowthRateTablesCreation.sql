delimiter //

DROP PROCEDURE IF EXISTS for_loop;

CREATE procedure for_loop()
wholeblock:BEGIN
  DECLARE x INT;
  SET x = 1;
  loop_label: LOOP
    IF x = 24 THEN
      LEAVE loop_label;
    END IF;
    SET @tname = (SELECT CryptoName FROM cryptos WHERE SNo = x);
    SET @statement = CONCAT('Create table ', @tname, ' ( curdate DateTime, growthrate double, PRIMARY KEY (curdate));');
    prepare stmt from @statement;
    execute stmt;
    deallocate prepare stmt;
    -- create table [x]	 ( SNo int NOT NULL, CryptoName varchar(20) NOT NULL, AnnualGrowthRate double, PRIMARY KEY (CryptoName));
    SET x = x + 1;
    ITERATE loop_label;
  END LOOP;

END//

delimiter ;
call for_loop();