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
```
# choose starter image
FROM node

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
```