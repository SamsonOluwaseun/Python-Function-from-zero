
# Python-Function-from-zero
Learning Python function from start

[![Python function test with GitHub Actions](https://github.com/SamsonOluwaseun/Python-Function-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/SamsonOluwaseun/Python-Function-from-zero/actions/workflows/main.yml)

### To call Microservice
Sometging like this

```bash
curl -X 'POST' \
  'https://humble-waffle-pg5x7wr695x36jj5-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft"
}'
```

### Build Container
`docker build .` to build
`docker image ls` to know the image location
IMAGE ID       CREATED              SIZE
51344b1fcf69   About a minute ago   712MB

`docker run -p 127.0.0.1:8080:8080 137865ad2b96` To run the docker

### To kill existing process
ps -ef | grep python
kill -9 process id eg 19659
history for previous commands

### Invoke POST request
run `bash invoke.sh`