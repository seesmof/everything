var svg = document.querySelector(".artwork__94141");
// replace the svg with white background
var bg = document.createElementNS("http://www.w3.org/2000/svg", "rect");
bg.setAttribute("width", svg.getAttribute("width"));
bg.setAttribute("height", svg.getAttribute("height"));
bg.setAttribute("fill", "white");
svg.parentNode.replaceChild(bg, svg);
