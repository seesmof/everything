from os import path, startfile


currentDir = path.dirname(path.abspath(__file__))
taskSchedulingFile = path.join(currentDir, "scheduling.py")
startfile(taskSchedulingFile)

intro = """
So the idea is to add GUI to Python Automations and make it public. Then I'd also have to come up with an adequate descriptive name for it

For now let's define the set of features we wanna have. So I'm thinking something like this:

- ability to add classes that will be opened every time they were selected and the links to them will be opened 
    - for this we will do a section where the user will be able to add each class and to specify if its once per week or once per two weeks, and also to specify the time and the day of course
    - in that input we should also have an optional meeting code field that will copy meeting code to user's clipboard as its opening

And so those are the main features. Pretty much a classes automation tool so that students don't have to open them all manually. We can also add feature that would allow us to open classes 5 minutes before it or something like that. That would probably go in the settings. In the settings section we can also have options to change color theme and something else. Maybe also an option to enable TTS every time a class starts. 

And also we might wanna have some kind of visualization for the app, maybe some kind of a calendar that shows the upcoming classes. And of course we wanna have the main page that would show our today's classes, as well as allow all sorts of interactions with the user.

So, to recap, here's the general structure of the app:

- Home Page
    - Upcoming Classes Section
- All Classes Page
    - All Classes
    - Class Details for Each One
    - Add Class Button
- Settings
    - Color Theme Selection
    - Enable/Disable TTS
    - Enable/Disable Notifications
    
Possible future features:

- Todo list for the tasks that have to be done
- Export classes
"""
