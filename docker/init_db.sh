mysql -u root -p$MYSQL_ROOT_PASSWORD <<_EOF
USE $MYSQL_DATABASE;
CREATE TABLE partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(255),
    equipo_visitante VARCHAR(255),
    goles_local INT,
    goles_visitante INT
);
_EOF