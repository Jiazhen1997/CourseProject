




from gradesourcesession import GradesourceSession
from getpass import getpass






def downloadEmail(login, courseID):
    
    
    gradesource = GradesourceSession(login, getpass('Password: '), courseID)
    gradesource.downloadEmail()

def downloadiClicker(login, courseID):
    gradesource = GradesourceSession(login, getpass('Password: '), courseID)
    gradesource.downloadiClicker()



def updateScoresByEmail(login, courseID, assignmentID, CSVFile, overwrite):
    gradesource = GradesourceSession(login, getpass('Password: '), courseID)
    gradesource.updateEmailScore(assignmentID, CSVFile, overwrite)

def updateScoresByPID(login,courseID, assignmentID, CSVFile, overwrite):
    gradesource = GradesourceSession(login, getpass('Password: '), courseID)
    gradesource.updatePIDScore(assignmentID, CSVFile, overwrite)


def downloadEmailGUI(login, courseID, password):
    
    
    gradesource = GradesourceSession(login, password, courseID)
    gradesource.downloadEmail()

def downloadiClickerGUI(login, courseID, password):
    gradesource = GradesourceSession(login, password, courseID)
    gradesource.downloadiClicker()



def updateScoresByEmailGUI(login, courseID, assignmentID, CSVFile, password, overwrite):
    gradesource = GradesourceSession(login, password, courseID)
    gradesource.updateEmailScore(assignmentID, CSVFile, overwrite)

def updateScoresByPIDGUI(login,courseID, assignmentID, CSVFile, password, overwrite):
    gradesource = GradesourceSession(login, password, courseID)
    gradesource.updatePIDScore(assignmentID, CSVFile, overwrite)
