[link to index](/readme.md)  

# Host a website on docker
- download the nginx image
- `docker run -d -p 80:80 nginx`
- navigate to your website folder on localhost
- `docker cp website/. <<CONTAINER ID>>:usr/share/nginx/html`
- `exit`
- `docker commit 363302a31233 davparcode/profile-page`
- `docker push davparcode/profile-page`