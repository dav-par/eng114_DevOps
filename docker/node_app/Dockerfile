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


#multi-build############################

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
