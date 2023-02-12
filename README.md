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