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

  if (translation == "NIV") {
    var data;
    if (_message) {
      data = _message;
    } else {
      data = await fetch(
        "https://beta.ourmanna.com/api/v1/get/?format=json&order=random"
      );
      data = await data.json();
    }
    lastMessage = data;

    var verse = data.verse.details.text;
    var reference = data.verse.details.reference;
  } else if (translation == "KJV") {
    var query = "https://bible-api.com/?random=verse&translation=KJV";
    var response = await fetch(query);
    var data = await response.json();
    lastMessage = data;

    var verse = data.text;
    var reference = data.reference;
  } else {
    var query = "https://bible-api.com/?random=verse&translation=BBE";
    var response = await fetch(query);
    var data = await response.json();
    lastMessage = data;

    var verse = data.text;
    var reference = data.reference;
  }

  vscode.window
    .showInformationMessage(
      verse,
      {
        modal: false,
      },
      "Copy",
      reference
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
