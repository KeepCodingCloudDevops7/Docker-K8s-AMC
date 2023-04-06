mysql -u root -p$MYSQL_ROOT_PASSWORD <<_EOF
CREATE DATABASE IF NOT EXISTS partidos_futbol;
USE partidos_futbol;
CREATE TABLE IF NOT EXISTS partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipo_local VARCHAR(255),
    equipo_visitante VARCHAR(255),
    goles_local INT,
    goles_visitante INT
);
_EOF