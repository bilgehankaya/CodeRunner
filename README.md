# Compiler

## Installing using Docker

Build the image using the following command:

```
docker image build . -t compilerapi
```

Run container using:

```
docker run -d --name compilerService -p 8111:8111 compilerapi
```

For the swagger page:
http://localhost:8111/docs

![Alt text](./compiler.png?raw=true "Compiler")