[link to index](/readme.md)  

## Host a website on docker
- download the nginx image
- `docker run -d -p 80:80 nginx`
- navigate to your website folder on localhost
- `docker cp website/. <<CONTAINER ID>>:usr/share/nginx/html`
- `exit`
- `docker commit 363302a31233 davparcode/profile-page`
- `docker push davparcode/profile-page`

## Bundle app in node image
- Dockerfile to add app to image
```
# choose starter image
FROM node

#label add info about the creator of this image - optional
LABEL MAINTAINER=dpark@spartaglobal.com


# copy app to container
WORKDIR /usr/src/app
COPY app/ /usr/src/

#navigate to app folder and install npm
RUN npm install -g npm@latest
RUN npm install express

#open port app
EXPOSE 3000

#launch the app
CMD ["node", "app.js"]

```
- `docker build -t davparcode/eng114_app .`
    - builds the image
- `docker run -d -p 3000:3000 davparcode/eng114_app`
    - runs the image in a container with port 3000 connected
- `docker push davparcode/eng114_app:v1`
    - `v1` is a tag for version control

## Production-ready image
- the below Dockerfile makes a slimmed-down image with only the essential dependences
```
# choose starter image
FROM node AS app

#label add info about the creator of this image - optional
LABEL MAINTAINER=dpark@spartaglobal.com


#copy app to container
WORKDIR /usr/src/app
COPY app/ /usr/src/

#navigate to app folder and install npm
RUN npm install -g npm@latest
RUN npm install express

#open port app
EXPOSE 3000

#launch the app
CMD ["node", "app.js"]


#multi-build##########

FROM node:alpine 

LABEL MAINTAINER=dpark@spartaglobal.com


#copy app to container
WORKDIR /usr/src/app
COPY app/ /usr/src/

#navigate to app folder and install npm
RUN npm install -g npm@latest
RUN npm install express
COPY --from=app /usr/src/app /usr/src/app

EXPOSE 3000

CMD ["node", "app.js"]
```
- `docker build -t davparcode/eng114_app:v3 .`
    - builds the image
- `docker run -d -p 3000:3000 davparcode/eng114_app:v3`
    - runs the image in a container with port 3000 connected
- `docker push davparcode/eng114_app:v3`
    - `v3` is a tag for version control
    

## docker-compose file in yml
- create a file called `docker-compose.yml`
- fill it with the below
```
 version: "2.6.1"

 services:
   db:
     image: mongo
     ports:
       - 27017:27017

   app:
    image: davparcode/eng114_app:v3
    ports:
       - 3000:3000
    environment:
      - DB_HOST=mongodb://db:27017/posts
    depends_on:
      - db
```
- `docker-compose up -d`
    - this builds the file runs the containers
    - `-d` runs it in the background
- `docker exec -it <<APP-CONTAINER-ID>> sh`
    - connects to the app machine
    - `node seeds/seed.js`
        - seeds the database
- go to http://localhost:3000/posts to see the app running

## notes
- if you make changes to the compose file then run `docker-compose build`