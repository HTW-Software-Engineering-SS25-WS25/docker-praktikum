# Praktikum Docker

## This is a repository for the Docker practical course at the University of Applied Sciences

Start by forking this repository to your own GitHub account. Then, clone it to your local machine to work on the tasks.

### Table of Contents

- [Basics](#basics)
- [Examples](#examples)
- [Tasks](#tasks)

## Basics

Check the Basics folder for a PDF containing the basics of Docker and theoretical knowledge about how Docker works and commands.

## Examples

Check the Examples folder for two application examples that are built with Docker. The first one is a simple Python Flask application, the second one is a more complex Vue.js application.

## Tasks

Check the Tasks folder for the tasks that you need to complete during the practical course. Each task has its own folder with a README.md file that contains the instructions and requirements for the task.

## Cheatsheet

Heres a cheatsheet with the most important Docker commands and options you need to know for the practical course. This is not an exhaustive list, but it covers the most commonly used commands and options.

### Dockerfile Commands

### `FROM <image>[:<tag>]`
Specifies the base image to start building from. Usually the first instruction in a Dockerfile.
```
FROM ubuntu:20.04
FROM node:14-alpine
```

### `RUN <command>`
Executes commands in a new layer on top of the current image.
```
RUN apt-get update && apt-get install -y curl
RUN npm install
```

### `COPY <src> <dest>`
Copies files or directories from the build context into the image.
```
COPY . /app
COPY package.json /app/
```

### `ADD <src> <dest>`
Similar to COPY but with additional features (can extract tar files and download from URLs).
```
ADD https://example.com/file.tar.gz /tmp/
```

### `WORKDIR <path>`
Sets the working directory for subsequent instructions.
```
WORKDIR /app
```

### `ENV <key>=<value>`
Sets environment variables inside the container.
```
ENV NODE_ENV=production
ENV PATH="/usr/local/bin:${PATH}"
```

### `EXPOSE <port>`
Documents which ports the container will listen on at runtime (doesn't actually publish them).
```
EXPOSE 80
EXPOSE 80/tcp 443/tcp
```

### `CMD ["executable", "param1", "param2"]`
Provides defaults for an executing container. Only the last CMD will take effect.
```
CMD ["node", "app.js"]
CMD ["nginx", "-g", "daemon off;"]
```

### `ENTRYPOINT ["executable", "param1", "param2"]`
Configures the container to run as an executable. CMD values will be appended as arguments.
```
ENTRYPOINT ["npm", "start"]
```

### `VOLUME ["/data"]`
Creates a mount point for external volumes.
```
VOLUME ["/var/log", "/data"]
```

### `USER <username or UID>`
Sets the user that will run subsequent RUN, CMD, or ENTRYPOINT instructions.
```
USER node
```

### `ARG <name>[=<default value>]`
Defines build-time variables that can be passed at build time.
```
ARG VERSION=latest
ARG BUILD_DATE
```

### `HEALTHCHECK`
Tells Docker how to test if the container is still working correctly.
```
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
```

### Example of a complete Dockerfile:
```dockerfile
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Copy dependency files
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy application code
COPY . .

# Set environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose port
EXPOSE 3000

# Create volume for persistent data
VOLUME ["/app/data"]

# Set user
USER node

# Start the application
CMD ["node", "server.js"]
```

### Basic Docker Commands

### `docker --version`

Shows the Docker version information.

### `docker info`

Displays system-wide information about Docker.

### `docker help`

Shows help information and lists all available commands.

## Container Management

### `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`

Creates and starts a new container from an image.

**Important Options:**

- `-d, --detach`: Run container in background

  ```
  docker run -d nginx
  ```

- `-p, --publish list`: Publish container's port(s) to the host

  ```
  docker run -p 8080:80 nginx  # Map port 80 in container to 8080 on host
  docker run -p 80:80 -p 443:443 nginx  # Map multiple ports
  ```

- `-v, --volume list`: Bind mount a volume

  ```
  docker run -v /host/path:/container/path nginx  # Bind mount
  docker run -v my_volume:/container/path nginx  # Named volume
  ```

- `--name string`: Assign a name to the container

  ```
  docker run --name my_container nginx
  ```

- `-e, --env list`: Set environment variables

  ```
  docker run -e MYSQL_ROOT_PASSWORD=secret mysql
  docker run -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=mydb mysql
  ```

- `--network string`: Connect container to a network

  ```
  docker run --network my_network nginx
  ```

- `--rm`: Automatically remove the container when it exits

  ```
  docker run --rm alpine echo "Hello World"
  ```

- `-it`: Interactive session with terminal

  ```
  docker run -it ubuntu bash
  ```

- `--restart string`: Restart policy (no, on-failure, always, unless-stopped)

  ```
  docker run --restart always nginx
  ```

- `--memory`: Memory limit

  ```
  docker run --memory 512m nginx
  ```

- `--cpus`: Limit CPU usage
  ```
  docker run --cpus 0.5 nginx  # Use up to 50% of one CPU
  ```

**Complete Example:**

```
docker run -d --name web_server -p 8080:80 -v ./website:/usr/share/nginx/html --restart always nginx
```

### `docker ps`

Lists running containers.

### `docker ps -a`

Lists all containers (running and stopped).

### `docker start CONTAINER`

Starts one or more stopped containers.

### `docker stop CONTAINER`

Stops one or more running containers gracefully.

### `docker restart CONTAINER`

Restarts one or more containers.

### `docker kill CONTAINER`

Forces a running container to stop by sending a SIGKILL signal.

### `docker rm CONTAINER`

Removes one or more containers.

```
docker rm $(docker ps -aq)  # Remove all containers
```

### `docker exec [OPTIONS] CONTAINER COMMAND`

Runs a command in a running container.

```
docker exec -it my_container bash
```

### `docker logs CONTAINER`

Fetches the logs of a container.

### `docker inspect CONTAINER|IMAGE`

Returns detailed information about a container or image.

## Image Management

### `docker images`

Lists all locally available images.

### `docker pull IMAGE[:TAG]`

Downloads an image from a registry.

```
docker pull nginx:latest
```

### `docker build [OPTIONS] PATH|URL`

Builds an image from a Dockerfile.

```
docker build -t my_image:1.0 .
```

### `docker rmi IMAGE`

Removes one or more images.

### `docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]`

Creates a tag TARGET_IMAGE that refers to SOURCE_IMAGE.

### `docker push IMAGE[:TAG]`

Pushes an image to a registry.

## Network Commands

### `docker network ls`

Lists all networks.

### `docker network create [OPTIONS] NETWORK`

Creates a new network.

```
docker network create my_network
```

### `docker network connect NETWORK CONTAINER`

Connects a container to a network.

### `docker network disconnect NETWORK CONTAINER`

Disconnects a container from a network.

## Volume Commands

### `docker volume ls`

Lists all volumes.

### `docker volume create [OPTIONS] [VOLUME]`

Creates a new volume.

### `docker volume inspect VOLUME`

Displays detailed information on one or more volumes.

### `docker volume rm VOLUME`

Removes one or more volumes.

## Docker Compose

### `docker compose up [OPTIONS]`

Creates and starts containers defined in a docker-compose.yml file.

```
docker compose up -d
```

### `docker compose down [OPTIONS]`

Stops and removes containers, networks, volumes, and images created by `up`.

### `docker compose logs [OPTIONS] [SERVICE...]`

Views output from containers.

### `docker compose ps [OPTIONS] [SERVICE...]`

Lists containers from the compose project.

## System Commands

### `docker system df`

Shows Docker disk usage.

### `docker system prune`

Removes all unused containers, networks, images, and volumes.

```
docker system prune -a --volumes  # Remove everything unused
```

### `docker stats [CONTAINER...]`

Displays a live stream of container resource usage statistics.

```
docker stats
```
