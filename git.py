import os
import uuid
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
                                    1:"Input 1 and a project name to create a directory (optional) for initialising git repo."
                                }
        self.functionValues = {1:self.initialisation}



    def following_process(self):
        '''
            Function to carry out the functionality.
        '''

        while(True):
            input = raw_input().strip().split(" ")
            if((input[0].isdigit()) and (int(input[0]) >= 1  and int(input[0]) <= len(self.functionValues))):
                print self.functionValues[int(input[0])](input[1] if(len(input)==2) else str(uuid.uuid1()))
            else:
                break


    def initialisation(self,directory):
        try:
            # print os.listdir(self.path)
            os.mkdir(self.path+directory)
            return "done"
        except OSError:
            return "failed"

git = Git("/media/aman/E:/Test-git-script/")
git.following_process()
