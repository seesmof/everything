const vscode = require("vscode");
const fetch = require("node-fetch");

/**
 * @param {vscode.ExtensionContext} context
 */
let interval = false;
let lastMessage = {};

function activate(context) {
  if (
    vscode.workspace.getConfiguration("bibletext").get("show-on-startup", true)
  ) {
    message();
  }

  interval = setInterval(async () => {
    if (vscode.window.state.focused) {
      message();
    }
  }, parseInt(vscode.workspace.getConfiguration("bibletext").get("duration") || "1") * 60 * 1000);

  let disposable = vscode.commands.registerCommand(
    "bible-text.previous",
    () => {
      message(lastMessage);
    }
  );

  context.subscriptions.push(disposable);
  let disposable2 = vscode.commands.registerCommand("bible-text.bless", () => {
    message();
  });
  context.subscriptions.push(disposable2);

  let disposable3 = vscode.commands.registerCommand(
    "bible-text.restart",
    () => {
      if (interval) {
        clearInterval(interval);
      }
      interval = setInterval(async () => {
        if (vscode.window.state.focused) {
          message();
        }
      }, parseInt(vscode.workspace.getConfiguration("bibletext").get("duration") || "1") * 60 * 1000);
    }
  );

  context.subscriptions.push(disposable3);
}

async function message(_message) {
  let translation = vscode.workspace
    .getConfiguration("bibletext")
    .get("translation");

  let baseUrl = "https://bible-api.com/";
  const query = `${baseUrl}?random=verse&translation=${translation}`;

  const response = await fetch(query);
  const data = await response.json();
  lastMessage = data;

  const verse = data.text;
  const reference = data.reference;

  vscode.window
    .showInformationMessage(
      verse,
      {
        modal: false,
      },
      "Copy",
      translation
    )
    .then((e) => {
      if (e == "Copy") {
        vscode.env.clipboard.writeText(`${verse} - ${reference}`);
      }
      if (e == reference) {
        let url = `https://www.biblegateway.com/passage/?search=${encodeURIComponent(
          reference
        )}&version=NASB;UKR`;
        vscode.env.openExternal(vscode.Uri.parse(url));
      }
    });
}

function deactivate() {
  if (interval) {
    clearInterval(interval);
  }
}

module.exports = {
  activate,
  deactivate,
};
