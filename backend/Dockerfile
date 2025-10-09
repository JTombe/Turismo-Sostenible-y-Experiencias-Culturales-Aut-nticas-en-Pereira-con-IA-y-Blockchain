version: '3.8'
services:
  maria-db:
    image: mariadb:10.11  # Versión estable de MariaDB
    container_name: maria-turismo
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass  # Cambia esto
      MYSQL_DATABASE: turismo_db     # DB por defecto para tu proyecto
      MYSQL_USER: turismo_user       # Usuario no-root
      MYSQL_PASSWORD: turismopass    # Password para el usuario
    ports:
      - "3306:3306"                  # Puerto local:contenedor
    volumes:
      - maria-data:/var/lib/mysql   # Persiste datos en un volumen

volumes:
  maria-data:  # Volumen para no perder datos al apagar
