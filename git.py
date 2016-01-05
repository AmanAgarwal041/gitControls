import os
import uuid
import subprocess
class Git(object) :
    '''
        A class is defined for Git functions
    '''

    def __init__(self,path):
        '''
            Initialisation for specifying the message to the user that the user can access it now.
        '''
        print "Git functionality is now in process"

        '''
            Global variables of a class for storing information related to handling processes.
        '''

        self.path = path if(path != "") else os.getcwd()
        self.functionalities = {
                                    0:"Select any one and pass the parameters separated by space",
                                    1:"Input 1 and a project name to create a directory (optional) for initialising git repo.",
                                    2:"Input 2 to pull the data from the git repo.",
                                    3:"Input 3 to push the data to the git repo.",
                                    4:"Input 4 to commit the changes to the git repo.",
                                    5:"Input 5 to add the remote origin to the git repo.",
                                    6:"Input 6 to add the new created files to the stack for committing the changes",
                                    7:"Input 7 to change the directory"
                                }
        self.functionValues = {
                                1:self.initialisation,
                                2:self.pull_changes,
                                3:self.push_changes,
                                4:self.commit_changes,
                                5:self.remote_origin,
                                6:self.add_files,
                                7:self.change_directory
                                }



    def following_process(self):
        '''
            Function to carry out the functionality.
        '''

        while(True):
            for i in range(len(self.functionalities)):
                if(i==0):
                    print "*******************\n"+self.functionalities[i]
                else:
                    print str(i)+") "+self.functionalities[i]
            print "*******************\n"
            input = raw_input().strip().split(" ")
            if((input[0].isdigit()) and (int(input[0]) >= 1  and int(input[0]) <= len(self.functionValues))):
                print self.functionValues[int(input[0])](" ".join(input[1:len(input)]) if(len(input)>1) else "")
            else:
                break


    def initialisation(self,inputValues):
        '''
            Initialisation of git project folder.
        '''
        if(inputValues==""):
            inputValues = [str(uuid.uuid1())]
        else:
            inputValues = inputValues.split(" ")

        try:
            os.mkdir(self.path+inputValues[0])
            os.chdir(self.path+inputValues[0])
            return subprocess.check_output("git init" , shell=True)
        except OSError:
            return "failed"


    def pull_changes(self,inputValues):
        '''
            Pull the data of the git project folder.
        '''
        try:
            if(inputValues!=""):
                inputValues = inputValues.split(" ")
                os.chdir(self.path+inputValues[0])
            return subprocess.check_output("git pull -v --progress" , shell=True)
        except OSError:
            return "failed"

    def push_changes(self,inputValues):
        '''
            Push the data to the git project folder.
        '''
        try:
            if(inputValues!=""):
                inputValues = inputValues.split(" ")
                os.chdir(self.path+inputValues[0])
            return subprocess.check_output("git push -v --progress origin master" , shell=True)
        except OSError:
            return "failed"

    def commit_changes(self,inputValues):
        '''
            Commit the changes to the git project folder.
        '''
        try:
            if(inputValues==""):
                '''
                    Default Message added to the Commit changes
                '''
                inputValues = "Added changes to the repository"
            return subprocess.check_output("git commit -am \""+inputValues+"\"" , shell=True)
        except OSError:
            return "failed"

    def remote_origin(self,inputValues):
        '''
            Remote Adding Origin repository link to the .git configuration file
        '''
        try:
            if(inputValues!=""):
                return subprocess.check_output("git remote add origin "+inputValues , shell=True)
            else:
                return "Changes cannot be done as the url is not provided"
        except OSError:
            return "failed"


    def add_files(self,inputValues):
        '''
            Adding files to the stack for commiting the changes
        '''
        try:
            if(inputValues==""):
                return subprocess.check_output("git add *" , shell=True)
        except OSError:
            return "failed"


    def change_directory(self,inputValues):
        '''
            Changing directory to follow git commands
        '''
        try:
            if(inputValues!=""):
                os.chdir(self.path+inputValues)
            else:
                return "Enter the directory"
        except OSError:
            return "failed"

git = Git("/media/aman/E:/GIT/")
git.following_process()
