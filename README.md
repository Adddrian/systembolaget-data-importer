# Systembolaget data importer



## Set MySql username / host / port / password


```bash
export DB_HOST="127.0.0.1"                                                                            
export DB_PORT="3306"                                                                                  
export DB_USER="user"                                                                                
export DB_PASSWORD="password"
```


## Create table


```sql
CREATE TABLE `artiklar` (
  `nr` varchar(255) DEFAULT NULL,
  `artikel_id` varchar(255) NOT NULL,
  `varnummer` varchar(255) DEFAULT NULL,
  `namn` varchar(255) DEFAULT NULL,
  `namn2` varchar(255) DEFAULT NULL,
  `prisinklmoms` varchar(255) DEFAULT NULL,
  `pant` varchar(45) DEFAULT NULL,
  `volymiml` varchar(255) DEFAULT NULL,
  `pris_per_liter` varchar(255) DEFAULT NULL,
  `saljstart` varchar(255) DEFAULT NULL,
  `utgatt` varchar(255) DEFAULT NULL,
  `varugrupp` varchar(255) DEFAULT NULL,
  `typ` varchar(255) DEFAULT NULL,
  `stil` varchar(255) DEFAULT NULL,
  `forpackning` varchar(255) DEFAULT NULL,
  `forslutning` varchar(255) DEFAULT NULL,
  `ursprung` varchar(255) DEFAULT NULL,
  `ursprunglandnamn` varchar(255) DEFAULT NULL,
  `producent` varchar(255) DEFAULT NULL,
  `leverantor` varchar(255) DEFAULT NULL,
  `argang` varchar(255) DEFAULT NULL,
  `provadargang` varchar(255) DEFAULT NULL,
  `alkoholhalt` varchar(255) DEFAULT NULL,
  `sortiment` varchar(255) DEFAULT NULL,
  `sortiment_text` varchar(255) DEFAULT NULL,
  `ekologisk` varchar(255) DEFAULT NULL,
  `etiskt` varchar(255) DEFAULT NULL,
  `etiskt_etikett` varchar(45) DEFAULT NULL,
  `koscher` varchar(255) DEFAULT NULL,
  `ravaror_beskrivning` varchar(255) DEFAULT NULL,
  `date` varchar(45) NOT NULL,
  PRIMARY KEY (`artikel_id`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```



## Run the script

```bash
./fetch.sh
```