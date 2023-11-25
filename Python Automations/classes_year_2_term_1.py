from library import *

disciplineNames = {
    "DSA": "Data Structures and Algorithms",
    "WEB": "Web technology and Web design",
    "OPI": "Fundementals of Programming Engineering",
    "SP": "Competitive Programming",
    "TY": "Theory of Probability",
    "IY": "History of Ukraine",
    "VM": "Calculus",
}

currentSchedule = {
    "Чисельник": {
        "Monday": {
            classTimes["3"]: "DSA Lecture",
            classTimes["4"]: "TY Practice",
            classTimes["5"]: "SP Lecture",
        },
        "Tuesday": {
            classTimes["1"]: "WEB Practice",
            classTimes["2"]: "DSA Practice",
            classTimes["5"]: "OPI Practice",
        },
        "Wednesday": {
            classTimes["1"]: "TY Lecture",
            classTimes["2"]: "WEB Lecture",
        },
        "Thursday": {
            classTimes["5"]: "IY Practice",
        },
        "Friday": {
            classTimes["2"]: "VM Lecture",
            classTimes["3"]: "VM Practice",
        },
    },
    "Знаменник": {
        "Monday": {
            classTimes["3"]: "DSA Lecture",
            classTimes["4"]: "SP Practice",
        },
        "Tuesday": {
            classTimes["1"]: "WEB Practice",
            classTimes["2"]: "DSA Practice",
            classTimes["4"]: "OPI Practice",
            classTimes["5"]: "OPI Practice",
        },
        "Wednesday": {
            classTimes["2"]: "WEB Lecture",
        },
        "Thursday": {
            classTimes["2"]: "OPI Lecture",
            classTimes["5"]: "IY Lecture",
        },
    },
}


def DSA_lecture():
    speak(f"Opening {disciplineNames['DSA']} Lecture.")
    webbrowser.open_new_tab(
        "https://us04web.zoom.us/j/79660602873?pwd=Dd2sGFxKZNePIGtiA32VhpzlmrfyKx.1"
    )
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%90%D0%A1%D0%94%20-%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%B8%20%D1%82%D0%B0%20%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%20%D0%94%D0%B0%D0%BD%D0%B8%D1%85%2Fdata"
    )


def DSA_practice():
    speak(f"Opening {disciplineNames['DSA']} Practice.")
    webbrowser.open_new_tab("https://meet.google.com/kwk-xiup-fvf")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%90%D0%A1%D0%94%20-%20%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC%D0%B8%20%D1%82%D0%B0%20%D0%A1%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B8%20%D0%94%D0%B0%D0%BD%D0%B8%D1%85%2Fdata"
    )


def TY_lecture():
    speak(f"Opening {disciplineNames['TY']} Lecture.")
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A2%D0%99%20-%20%D0%A2%D0%B5%D0%BE%D1%80%D1%96%D1%8F%20%D0%99%D0%BC%D0%BE%D0%B2%D1%96%D1%80%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9%2Fdata"
    )


def TY_practice():
    speak(f"Opening {disciplineNames['TY']} Practice.")
    webbrowser.open_new_tab("https://meet.google.com/arg-syjc-vcz")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A2%D0%99%20-%20%D0%A2%D0%B5%D0%BE%D1%80%D1%96%D1%8F%20%D0%99%D0%BC%D0%BE%D0%B2%D1%96%D1%80%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9%2Fdata"
    )


def SP_lecture():
    speak(f"Opening {disciplineNames['SP']} Lecture.")
    webbrowser.open_new_tab("https://meet.google.com/dxa-pjjr-byx")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A1%D0%9F%20-%20%D0%A1%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D0%B2%D0%BD%D0%B5%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%2Fdata"
    )


def SP_practice():
    speak(f"Opening {disciplineNames['SP']} Practice.")
    webbrowser.open_new_tab("https://meet.google.com/dxa-pjjr-byx")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A1%D0%9F%20-%20%D0%A1%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D0%B2%D0%BD%D0%B5%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D1%83%D0%B2%D0%B0%D0%BD%D0%BD%D1%8F%2Fdata"
    )


def WEB_lecture():
    speak(f"Opening {disciplineNames['WEB']} Lecture.")
    webbrowser.open_new_tab("https://meet.google.com/igt-rmni-ftk")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%92%D0%95%D0%91%20-%20%D0%92%D0%B5%D0%B1%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D0%B9%20%D1%82%D0%B0%20%D0%92%D0%B5%D0%B1%20%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%2Fdata"
    )


def WEB_practice():
    speak(f"Opening {disciplineNames['WEB']} Practice.")
    webbrowser.open_new_tab("https://meet.google.com/igt-rmni-ftk")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%92%D0%95%D0%91%20-%20%D0%92%D0%B5%D0%B1%20%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D0%B9%20%D1%82%D0%B0%20%D0%92%D0%B5%D0%B1%20%D0%B4%D0%B8%D0%B7%D0%B0%D0%B9%D0%BD%2Fdata"
    )


def OPI_practice():
    speak(f"Opening {disciplineNames['OPI']} Practice.")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/5151534723")
    pyperclip.copy("152334")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%9E%D0%9F%D0%86%20-%20%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%B8%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%BE%D1%97%20%D0%86%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D1%96%D1%97%2Fdata"
    )


def OPI_lecture():
    speak(f"Opening {disciplineNames['OPI']} Lecture.")
    webbrowser.open_new_tab("https://us02web.zoom.us/j/71772651691")
    pyperclip.copy("2023")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%9E%D0%9F%D0%86%20-%20%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%B8%20%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BD%D0%BE%D1%97%20%D0%86%D0%BD%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D1%96%D1%97%2Fdata"
    )


def IY_practice():
    speak(f"Opening {disciplineNames['IY']} Practice.")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/82941381946?pwd=fWODT5tAqYogAMAfDpkTQf6aWp1IRF.1"
    )
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%86%D0%A3%20-%20%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%2C%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B0%20%D1%82%D0%B0%20%D1%96%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%87%D0%BD%D1%96%D1%81%D1%82%D1%8C%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8%2Fdata"
    )


def IY_lecture():
    speak(f"Opening {disciplineNames['IY']} Lecture.")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/82941381946?pwd=fWODT5tAqYogAMAfDpkTQf6aWp1IRF.1"
    )
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%86%D0%A3%20-%20%D0%86%D1%81%D1%82%D0%BE%D1%80%D1%96%D1%8F%2C%20%D0%BA%D1%83%D0%BB%D1%8C%D1%82%D1%83%D1%80%D0%B0%20%D1%82%D0%B0%20%D1%96%D0%B4%D0%B5%D0%BD%D1%82%D0%B8%D1%87%D0%BD%D1%96%D1%81%D1%82%D1%8C%20%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D0%B8%2Fdata"
    )


def VM_lecture():
    speak(f"Opening {disciplineNames['VM']} Lecture.")
    webbrowser.open_new_tab(
        "https://us05web.zoom.us/j/4344130497?pwd=Z05oUnB4RDJGTGRWeEFaNlRsVDlBZz09"
    )
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A1%D0%A0%D0%92%D0%9C%20-%20%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%A0%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D0%B8%20%D0%92%D0%B8%D1%89%D0%BE%D1%97%20%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8%2Fdata"
    )


def VM_practice():
    speak(f"Opening {disciplineNames['VM']} Practice.")
    webbrowser.open_new_tab("https://meet.google.com/neu-xwef-ivi")
    webbrowser.open_new_tab(
        "obsidian://open?vault=everything&file=University%2FYear%202%20Term%201%2F%D0%A1%D0%A0%D0%92%D0%9C%20-%20%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D1%96%20%D0%A0%D0%BE%D0%B7%D0%B4%D1%96%D0%BB%D0%B8%20%D0%92%D0%B8%D1%89%D0%BE%D1%97%20%D0%9C%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B8%2Fdata"
    )


# tasks examples

# Task(
#     is_completed=False,
#     content='ЛК. Спеціальні Розділи Вищої Математики',
#     description='',
#     due=Due(date='2023-09-15', string='every other fri at 10:05'),
#     priority=1
# )

# Task(
#     is_completed=False,
#     content='test priority 1',
#     description='',
#     due=Due(date='2023-09-15', string='15 Sep'),
#     priority=4
# )

# full format. above is just the properties we really need

# Task(assignee_id=None, assigner_id=None, comment_count=0, is_completed=False, content='ПР. Спеціальні Розділи Вищої Математики', created_at='2023-09-03T18:16:36.019003Z', creator_id='45513878', description='', due=Due(date='2023-09-15', is_recurring=True, string='every other fri at 11:55', datetime='2023-09-15T08:55:00Z', timezone='Europe/Kiev'), id='7194004149', labels=['GCal'], order=11, parent_id=None, priority=1, project_id='2318959463', section_id=None, url='https://todoist.com/showTask?id=7194004149', sync_id=None)
