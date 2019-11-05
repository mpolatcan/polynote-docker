# polynote-docker

Docker image of **Polynote** which its developed by **Netflix**

## Usage

```yaml
version: "3.6"
services:
  polynote:
    image: mpolatcan/polynote:0.2.11-java8
    container_name: polynote
    ports:
      - 8888:8192
    volumes:
      - ./notebooks:/polynote/notebooks
```

To run **Polynote**, run this command:
    
    sudo docker-compose up -d
    
After that open url **http://localhost:8888**