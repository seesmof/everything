chrome.commands.onCommand.addListener((command) => {
  const commandsMap = {
    "open-chat-gpt": "https://chat.openai.com/",
    "open-bing-chat": "https://copilot.microsoft.com/",
    "open-phind": "https://phind.com/",
  };

  if (commandsMap[command]) {
    chrome.tabs.create({ url: commandsMap[command] });
  }
});
