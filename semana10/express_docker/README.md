# Docker

## Comandos

### Docker build

```bash
# docker build -t {nombre_imagen} .
# -t: tag
docker build -t express_docker .
```

### Docker run

```bash
# docker run -p {puerto_contenedor}:{puerto_host} -d {nombre_imagen}
# -p: mapear puerto
# -d: ejecutar en segundo plano
docker run -p 5000:3000 express_docker
```

### Show Executing Containers

```bash
docker ps
```

### Show All Containers

```bash
docker ps -a
```

### Stop Container

```bash
docker stop {id_contenedor}
```

### Remove Container

```bash
docker rm {id_contenedor}
```

### Remove All Containers

```bash
docker rm -f $(docker ps -a -q)
```

### Show Images

```bash
docker images
```

### Remove Images

```bash
docker rmi {id_imagen}
```

### Remove All Images

```bash
docker rmi -f $(docker images -q)
```

### Show Container Logs

```bash
docker logs {id_contenedor}
```