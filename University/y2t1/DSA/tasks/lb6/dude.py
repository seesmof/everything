# Importing the module
from urllib import response
import g4f

# Our input prompt, can be taken as input
input_data = (
    "Like with Neanderthals, Homo Sapiens also interbred with their... True or False?"
)

# Forming a message object in the following required format:
"""
"role": "user", 
"content": ...our message goes here
"""
message_object = {"role": "user", "content": input_data}

# A list of available providers in the g4f library
providers = [
    g4f.Provider.AItianhu,
    g4f.Provider.AItianhuSpace,
    g4f.Provider.AiAsk,
    g4f.Provider.Aichat,
    g4f.Provider.ChatBase,
    g4f.Provider.ChatForAi,
    g4f.Provider.ChatgptAi,
    g4f.Provider.ChatgptX,
    g4f.Provider.FakeGpt,
    g4f.Provider.FreeGpt,
    g4f.Provider.GPTalk,
    g4f.Provider.GptForLove,
    g4f.Provider.GptGo,
    g4f.Provider.Hashnode,
    g4f.Provider.MyShell,
    g4f.Provider.NoowAi,
    g4f.Provider.OpenaiChat,
    g4f.Provider.Theb,
    g4f.Provider.Vercel,
    g4f.Provider.You,
    g4f.Provider.Yqcloud,
    g4f.Provider.Acytoo,
    g4f.Provider.Aibn,
    g4f.Provider.Ails,
    g4f.Provider.Chatgpt4Online,
    g4f.Provider.ChatgptDemo,
    g4f.Provider.ChatgptDuo,
    g4f.Provider.ChatgptFree,
    g4f.Provider.ChatgptLogin,
    g4f.Provider.Cromicle,
    g4f.Provider.GptGod,
    g4f.Provider.Opchatgpts,
    g4f.Provider.Ylokh,
]


for provider in providers:
    # Generating the response
    # The model can be changed to whichever one available in the g4f library
    # The messages needs to be a list
    try:
        output_data = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo, messages=[message_object], provider=provider
        )
    except:
        output_data = (
            f"Whoops... The provider {provider} seems to be offline. Fixing it now 🫡"
        )
        providers.remove(provider)
        continue

    print(f"{output_data}\n")
