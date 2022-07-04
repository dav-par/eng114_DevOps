[link to index](/readme.md)  
# Docker
Docker is an open source platform for building, deploying, and managing containerized applications.

![Docker](/Documentation/resources/docker/Docker_architecture.jpg)  

## Benefits
- Portability
    - Once you have tested your containerized application you can deploy it to any other system where Docker is running and you can be sure that your application will perform exactly as it did when you tested it.
- Performance
    - Although virtual machines are an alternative to containers, the fact that containers do not contain an operating system (whereas virtual machines do) means that containers have much smaller footprints than virtual machines, are faster to create, and quicker to start.
 - Agility
    - The portability and performance benefits offered by containers can help you make your development process more agile and responsive. Enhancing your continuous integration and continuous delivery processes to take advantage of containers and technology such as Enterprise Developer Build Tools for Windows makes it easier for you to deliver the right software at the right time. Enterprise Developer Build Tools for Windows is a component of Enterprise Developer which provides all of the functionality of Enterprise Developer to enable you to compile, build, and test COBOL code but without the overhead of an IDE.
- Isolation
    - A Docker container that contains one of your applications also includes the relevant versions of any supporting software that your application requires. If other Docker containers contain applications that require different versions of the same supporting software, that isn't a problem because the different Docker containers are totally independent of one other.
    - This also means that as you move through the various stages of your development lifecycle, you can have total confidence that an image you create during development will perform exactly the same as it moves through testing and potentially to your users.
- Scalability
    - You can quickly create new containers if demand for your applications requires them. When using multiple containers you can take advantage of a range of container management options. See the Docker documentation for more information on these options.

## Note
 - Although there are a number of advantages to using Docker, not all applications are suitable for running in containers. In particular, it is generally accepted that applications with a graphical user interface are not suitable for using with Docker. Micro Focus recommends that when evaluating potential use of Docker you bear in mind the types of application that you will need to run.

## containers vs virtualisation
-  Virtualization enables you to run multiple operating systems on the hardware of a single physical server, while containerization enables you to deploy multiple applications using the same operating system on a single virtual machine or server. 
- Virtual machines are great for supporting applications that require an operating system’s full functionality when you want to deploy multiple applications on a server, or when you have a wide variety of operating systems to manage. Containers are a better choice when your biggest priority is to minimize the number of servers you’re using for multiple applications.

## docker commands
- `docker run -d -p 80:80 nginx`
    - downloads and runs nginx on port 80
- `docker ps`
    - see containers that are running
    - `-a` - see all
- `docker rm <<CONTAINTER ID>>`
    - stops container running
    - `-f` to force it
- `docker exec -it <<CONTAINER ID>> bash`
    - runs bash on the container


## notes
- use `alias docker="winpty docker"` if `docker` command isn't working
