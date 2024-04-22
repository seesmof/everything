var left = document.querySelector("a.prev-chapter");
var right = document.querySelector("a.next-chapter");

document.addEventListener("keydown", function (event) {
  if (
    document.activeElement.tagName.toLowerCase() === "input" &&
    document.activeElement.type === "text"
  ) {
    return;
  }

  if (event.key === "ArrowLeft") {
    left.click();
  } else if (event.key === "ArrowRight") {
    right.click();
  }
});

var navbar = document.querySelector(".bbl-fontsize");
var fontsizeDropdown = navbar.querySelector(".fontsize-dropdown");
fontsizeDropdown.parentNode.removeChild(fontsizeDropdown);

var fontSizeArea = document.createElement("div");
navbar.appendChild(fontSizeArea);

fontSizeArea.style.display = "flex";
fontSizeArea.style.flexDirection = "row";
fontSizeArea.style.gap = "6px";

var decreaseBtn = document.createElement("button");
decreaseBtn.innerHTML = "-";
decreaseBtn.addEventListener("click", function () {
  textbox.value = (parseFloat(textbox.value) - 0.1).toFixed(1);
  textbox.dispatchEvent(new Event("input"));
});
fontSizeArea.appendChild(decreaseBtn);

decreaseBtn.style.backgroundColor = "#952004";
decreaseBtn.style.color = "white";
decreaseBtn.style.paddingTop = "4px";
decreaseBtn.style.paddingBottom = "4px";
decreaseBtn.style.paddingLeft = "12px";
decreaseBtn.style.paddingRight = "12px";
decreaseBtn.style.borderRadius = "3px";
decreaseBtn.style.border = "1px solid #952004";

var textbox = document.createElement("input");
textbox.type = "text";
textbox.className = "fontsizeChanger";
textbox.value = 1.4;
textbox.placeholder = "Bible text font size...";
fontSizeArea.appendChild(textbox);

textbox.style.border = "1px solid #b2b2b2";
textbox.style.paddingLeft = "6px";
textbox.style.width = "60px";

var increaseBtn = document.createElement("button");
increaseBtn.innerHTML = "+";
increaseBtn.addEventListener("click", function () {
  textbox.value = (parseFloat(textbox.value) + 0.1).toFixed(1);
  textbox.dispatchEvent(new Event("input"));
});
fontSizeArea.appendChild(increaseBtn);

increaseBtn.style.backgroundColor = "#952004";
increaseBtn.style.color = "white";
increaseBtn.style.paddingTop = "4px";
increaseBtn.style.paddingBottom = "4px";
increaseBtn.style.paddingLeft = "12px";
increaseBtn.style.paddingRight = "12px";
increaseBtn.style.borderRadius = "3px";
increaseBtn.style.border = "1px solid #952004";

textbox.addEventListener("input", function () {
  var fontSize = this.value + "em";

  var textElements = document.querySelectorAll(".text");
  textElements.forEach(function (element) {
    element.style.fontSize = fontSize;
    element.style.lineHeight = fontSize;
  });
});

new MutationObserver(() => {
  let elements = document.getElementsByClassName("woj");

  [...elements].forEach((el) => {
    el.style.color = document.body.classList.contains("s-woj")
      ? "#D20103"
      : "black";
  });
}).observe(document.body, { attributes: true });
