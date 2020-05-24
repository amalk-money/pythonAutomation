# pythonAutomation
# Overview of the project
In the world of Devops, it is all about the automation and how to automate the task. 
According to the researches, most companies fail to successfully deliver ML based projects and are stuck in the process of tuning the model to work better. Then came the new technology called MLOps which integrates the ML with Devops to address such challenges.
One of the challenges is finding the better accuracy of the model by tweaking the model. So a small setup I created is demonstrated below.
For this project I used the Jenkins, Git and Docker Devops tools and CNN program.
## Project Setup 
In the Jenkins I used the following jobs:
## Job 1: Copy the github code
When the developer creates the code, it pushes the code to github via git and as soon as the code is pushed, Jenkins job automatically starts to run.
![copy files general]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/copy%20files%20general.png)
https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/copy%20pgm%20general.png
![copy files scm](https://github.com/amalk-money/drupal_with_docker/blob/master/ScreenShots/up.png)
![copy files build trigger](https://github.com/amalk-money/drupal_with_docker/blob/master/ScreenShots/up.png)
![copy files build](https://github.com/amalk-money/drupal_with_docker/blob/master/ScreenShots/up.png)
Copied files are copied to the `/py` folder.
## Job2: Creating the environment
This job will create the environment to run the program what the developer defined. Before creating the environment, it will check f the environment is present or not. If not it will create the environment.
![env gen]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20general.png)
![env scm]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20scm.png) 

![env build trigger]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20build%20trigger.png)

![env build]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20build.png)
Dockerfile for Python
![dockerfile]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/Dockerfile.png)
According to the `requirements.txt` file, the environment for the program will be created.
## Job3: Executing the program
Now the environment is ready for the programs to run on.
![env gen]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/pgm%20general.png)
![env scm]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20scm.png) 
![env build]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/env%20build.png)
`programFile.py` python code will run on the environment created and will provide the accuracy.
## Job 4: Tweaking the python code
For tweaking the code and to show how tuning works, I created another program which tweaks the existing code.
![tweak general]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/copy%20pgm%20general.png)
![tweak scm]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/copy%20pgm%20scm.png)
![build]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/copy%20pgm%20build.png)
This Job will the run the code `copyProgram.py`.
In the `programFile.py` I added a comment `#add` between the output layer and the layer before it to show what tweaking means. 
![before]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/code%20before.png)

In the file `addFile.txt` I added three layers code description.
![addfile]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/add.png)

So when this job runs, `addFile.txt’ file content is copied to the actual code where `#add` is found. And hence the actual code becomes as:
![addfile]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/code%20after.png)
## Job 5: Running the tweaked code
This job will be automatically executed when the tweaking of the code is done. 
![re general]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/re%20general.png)
![re build trgger]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/re%20build%20trigger.png)
![re build]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/re%20build.png)
This job will run the tweaked code on the same environment and provide the accuracy.
## Conclusion
For the purpose of showing the difference, I just used one epoch
Original code
![run pgm]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/first%20run%20pgm.png)
Here the accuracy is approximately 94%
Tweaked code
![re run]( https://github.com/amalk-money/pythonAutomation/blob/master/screenShots/first%20run%20re.png)
Here the accuracy is approximately 95%
Even though there is just a slight increase of the accuracy but even few percentage of accuracy makes difference.
So, that’s how we can use the ML with the DevOps to make the automation work easily.
## Future Improvements
Even thought this is just a demonstration, we can use this setup to build different ML applications where human interventions are required so much like finding the weights or coefficients and accuracy where the developers need to continuously monitor the process.
We can use the DevOps technology to automatically monitor the process too.
