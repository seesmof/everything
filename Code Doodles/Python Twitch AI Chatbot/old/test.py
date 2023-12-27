import g4f

while True:
    input_prompt = input(": ")
    if input_prompt == "q":
        break
    input_prompt = [{"role": "user", "content": input_prompt}]
    
    output_response = g4f.ChatCompletion.create(
        model=g4f.models.default, 
        messages=input_prompt,
    )
    print(output_response)