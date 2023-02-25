# ultra-ctrl-f

`ultra-ctrl-f` is a personal side project that arised from my own struggle to find pictures of myself inside a website with pictures from a sporting event. I thought "Wouldn't it be great if I could look up pictures using face similarity?". This project is my attempt to do that, using a chrome extension that communicates with a facial landmark detector neural network backend.

Link to frontend of chrome extension: https://github.com/guerchen/ultra-ctrl-f-front

# ultra-ctrl-f-back

This is where the magic behind `ultra-ctrl-f` happens! Images are collected through websites, stored in a database, preprocessed and clustered with the final goal of giving the user the most similar faces in a website to the reference picture. 

## How to run:

It's easy to run this API locally. Using Docker, just:
1. Build the Docker image:
```
docker build -t myimage .
```
2. Start container:
```
docker run -d --name mycontainer -p 80:80 myimage
```