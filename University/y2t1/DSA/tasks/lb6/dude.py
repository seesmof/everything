# Importing the module
import g4f

# Our input prompt, can be taken as input
input_data = "Hello World!"

# Forming a message object in the following required format:
"""
"role": "user", 
"content": ...our message goes here
"""
message_object = {"role": "user", "content": input_data}

# Generating the response
# The model can be changed to whichever one available in the g4f library
# The messages needs to be a list
output_data = g4f.ChatCompletion.create(
    model=g4f.models.gpt_35_turbo, messages=[message_object]
)

# Output response
print(f"{output_data}\n")


# Or, we could put it all into an infinite loop and chat with it, like a real chat-bot
while True:
    input_data = input(": ")
    message_object = {"role": "user", "content": input_data}
    output_data = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo, messages=[message_object]
    )
    print(f"{output_data}\n")
