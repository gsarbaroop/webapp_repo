Process & Functionality:
1. A webapp using Flask was created which routes a GET api and returns a message if "/home" path is hit. 
2. A Dockerfile is created using this py file and a requirements file.
3. The docker image is created by building this file. The image is based on python and runs pip command to install flask. Then runs the command of python to run the file. Later, exposes port 80

4. To create the image simply run "docker build -t {image_name}:{version} ."
5. To run the image type "docker run -p 80:80 {image_id}".


