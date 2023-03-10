# International Standard Book Numbers - Validating ISBN Codes

The International Standard Book Number (ISBN) is a unique identifying number given to each published book. 
ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.

## Description

This program has a function that takes a string of numbers (possibly with an X at the end) and...

1. Return "Invalid" if it is not a valid ISBN-10 or ISBN-13.
2. Return "Valid" if it is a valid ISBN-13.
3. If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.

The program also converts a valid ISBN-10 to ISBN-13 by tacking 978 to the start, then changing the last digit (the check digit)
so that the resulting number passes the ISBN-13 check.

__Examples__

- isbn13("9780316066525") ➞ "Valid"
- isbn13("0330301824") ➞ "Invalid"
- isbn13("0316066524") ➞ "9780316066525"

## Table of Content
1.  Implementing the program in a virtual environment.
    - 1.1   Dependencies
    - 1.2   Copying Files
    - 1.3   Run Program
             
2.  Implementing the program in a Docker environment.
    - 2.1   Creating a Docker Hub account
    - 2.2   Prepare the Docker Environment
    - 2.3   Copying Files and Pushing the Program to Docker Hub
    - 2.4   Run Program
  
3.  Authors

### 1.  Implementing the program in a virtual environment.

##### 1.1   Dependencies

The virtual environment requires the installation of python & pip.

##### 1.2   Copying Files

Go to the directory or folder where you want to install the project and enter the following command in the command line or terminal:
```
>git clone https://github.com/riaandeventer/HyperionDev_CR_THT
```
If you are asked for a login then it should be because you might have made a typing error with the link.

##### 1.3   Run Program

If your files copied successfully, there should be a folder Section_C when you enter the >dir command or Windows or >ls -l for Unix or MacOS.
Go to this directory with below command.
```
>cd HyperionDev_CR_THT
>cd section_3
```

or for Unix or MacOS use
```
>cd ~/HyperionDev_CR_THT
>cd ~/Section_3
```
Now we can run the program with below command:
```
>python isbn.py
```

### 2.  Implementing the program in a Docker environment.

##### 2.1   Creating a Docker Hub Account

Go to [https://hub.docker.com/](https://hub.docker.com/) and create a docker account.

##### 2.2   Prepare the Docker Environment

To publish to Docker Hub, we have 2 options. Firstly we can install Docker Desktop if your machine meet the system requirements or we can 
use Docker Playground that gives us an online virtual space where we can test Docker Containers.

**For installing Docker Desktop**, go to [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

Open a command prompt and enter the following command to test if Docker Desktop was installed successfully:
```
>docker run hello-world
```
It will do some downloads and, finally, you’ll see output starting with “Hello from Docker!”.

**For using the Docker Playground**, go to [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/) and log in with your 
https://hub.docker.com/ docker account that you created in step 2.1 .

After logging in with Docker Playground, click “Start”. The playground has a 4-hour time limit, 
after which everything you did there will be deleted.

After clicking “Start” you’ll be able to create an instance.

##### 2.3   Copying Files and Pushing the Project to Docker Hub

Regardless if you are now in the desktop command prompt or the docker playground instance, run the following commands:

Copy the required files.
```
>git clone https://github.com/riaandeventer/HyperionDev_CR_THT
```
If you are asked for a login then it should be because you might have made a typing error with the link.

First we have to go into the folder that was created from the clone.
```
>cd HyperionDev_CR_THT
>cd Section_3           -- You can change this folder name to isbn
```
or for Unix or MacOS use
```
>cd ~/HyperionDev_CR_THT
>cd ~/Section_3
```
Now we have to build the project with following commands:
```
>docker build -t isbn ./
```
Now we need to connect the build name with the docker hub repository that we want to create.
We will do this with the below command.
```
>docker tag isbn [docker hub username without square brackets]/isbn
```
Now we need to copy our build to our docker hub. We need to use the push command from the command prompt
or the playground prompt (Which ever one you are using).
To be able to push to docker hub, we need access to docker hub from the command line. Let's use the following commands:
```
>docker login
```
You will be asked for your docker hub username and password. Enter these and lookout for the login succeeded message.
If the login was successful, let's push our build to docker hub with the following command:
```
>docker push [docker hub username without square brackets]/isbn
```
We have now created our project on docker hub. Go to Docker Hub and confirm that there is now a isbn repository
indicating that a push took place.

If you have been working with Docker Desktop, we are no done with Docker Desktop and will complete the rest with Docker Playground.

##### 2.4   Run Program

Just a reminder **if you have been working with Docker Desktop**, go to [https://labs.play-with-docker.com/](https://labs.play-with-docker.com/)
to test the site. Login with your Docker Hub account if you are not already logged in. Then click “Start”, and on the next screen
click “add new instance”.

**If you have used Docker Playground for Copying Files and Publishing the site to Docker Hub** then you can just continue with the following commands:

```
>docker run [docker hub username without square brackets]/isbn
```
Docker on the VM will download your image from Docker Hub and do all the relevant preparations and installation to make your app work.

The program should run in the terminal.

### 3.  Authors

Riaan Deventer  - [LinkedIn: @riaandeventer](https://www.linkedin.com/in/riaandeventer/)
