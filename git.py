import os
import uuid
class Git(object) :
    '''
        A class is defined for Git functions
    '''

    def __init__(self):
        '''
            Initialisation for specifying the message to the user that the user can access it now.
        '''
        print "Git functionality is now in process"

        self.functionalities = {
                                    0:"Select any one and pass the parameters separated by space",
                                    1:"Input 1 and a project name to create a directory (optional) for initialising git repo."
                                }
        self.functionValues = {1:self.initialisation}

        while(True):
            input = raw_input().strip().split(" ")
            if(int(input[0]) >= 1  and int(input[0]) <= len(self.functionValues)):
                print self.functionValues[int(input[0])](input[1] if(len(input)==2) else uuid.uuid1())
            else:
                break


    def initialisation(self,directory):
        print os.getcwd()
        return directory


git = Git()
