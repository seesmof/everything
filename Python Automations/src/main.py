from os import path, startfile


currentDir = path.dirname(path.abspath(__file__))
taskSchedulingFile = path.join(currentDir, "modules", "scheduling.py")
startfile(taskSchedulingFile)
