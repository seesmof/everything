def bTreeTaskSearchForSub(data):
    # Helper function to retrieve subscriber data based on phone number
    def retrieveSubscribersData(phoneNumber):
        for sub in employeesTaskElementsList:
            if sub["phone"] == phoneNumber:
                return sub
        return None

    # Check if the data is found in the employeesTaskElements tree
    isFound = employeesTaskElements.search(data)

    # Retrieve the subscriber data based on the data (phone number)
    subscriberData = retrieveSubscribersData(data)

    # If data is found in the tree, display the subscriber's name and type in an alert popup
    # Otherwise, display a message that data was not found in the database
    if isFound:
        AlertPopup(
            f"+{data} was found in the database\nName - {subscriberData['name']}, Type - {subscriberData['type']}"
        )
    else:
        AlertPopup(f"+{data} was NOT found in the database")
