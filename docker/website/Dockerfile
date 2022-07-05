# choose starter image
FROM nginx

#label add info about the creator of this image - optional
LABEL MAINTAINER=dpark@spartaglobal.com


#copy website/dependence to usr/share/nginx/html folder in container
COPY website/ /usr/share/nginx/html/

#automate port mapping
EXPOSE 80

#run the command to launch the server/container - create container at launch time
CMD ["nginx", "-g", "daemon off;"]

#docker run command
