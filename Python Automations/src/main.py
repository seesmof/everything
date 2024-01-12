from os import path, startfile


currentDir = path.dirname(path.abspath(__file__))
taskSchedulingFile = path.join(currentDir, "scheduling.py")
startfile(taskSchedulingFile)
