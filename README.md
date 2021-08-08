# ActionsDemo
Repositorio para realizar pruebas unitarias con pytest. Desarrollo web profesional, 81. 

# Correr nuestro Dockerfile
docker build -t webapp:v1 .

# Crear el contenedor 
docker run -it -p 8080:8080 -v /workspace/ActionsDemo/docker:/docker --name webapp -h webapp webapp:v1