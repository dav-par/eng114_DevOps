# choose starter image
FROM mongo

#label add info about the creator of this image - optional
LABEL MAINTAINER=dpark@spartaglobal.com


#copy app to container
WORKDIR /usr/src/db/
COPY ./mongodb.conf /etc/


#open port app
EXPOSE 27017

#launch the app
CMD ["mongod"]