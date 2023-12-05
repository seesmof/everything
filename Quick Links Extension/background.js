chrome.commands.onCommand.addListener((command) => {
  const commandsMap = {
    "open-chat-gpt": "https://chat.openai.com/",
    "open-bing-chat":
      "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx&wlexpsignin=1",
    "open-phind": "https://phind.com/",
    "open-monkeytype": "https://monkeytype.com/",
  };

  if (commandsMap[command]) {
    chrome.tabs.create({ url: commandsMap[command] });
  }
});
