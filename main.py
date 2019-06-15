import sys
from os import walk

logPath = sys.argv[1]

myUsernames = ['', '']
herUsernames = ['', '']

myUsernameCount = 0
herUsernameCount = 0

(_, _, logFileNames) = next(walk(logPath))

for i, logFileName in enumerate(logFileNames):
    with open(logPath+logFileName, 'r') as logFile:
        log = logFile.read()
        for myUsername in myUsernames:
            myUsernameCount += log.count(myUsername)
        for herUsername in herUsernames:
            herUsernameCount += log.count(herUsername)
    print(i)

print('myUsernameCount: {}, herUsernameCount: {}'.format(myUsernameCount, herUsernameCount))
