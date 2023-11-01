## How to connect jQuery to the project?

To connect jQuery to your project, you can either download the jQuery library from the official website or include it from a content delivery network (CDN). You should add a script tag in your HTML file with the source pointing to the jQuery library, like this:

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

## What are the advantages and disadvantages of using the jQuery library?

- Advantages:
  - Simplifies DOM manipulation and traversal.
  - Provides a wide range of built-in animations and effects.
  - Cross-browser compatibility.
- Disadvantages:
  - Overhead in terms of file size and loading time.
  - Some of its features may not be as efficient as using native JavaScript.
  - The need for an additional library in modern web development may be questioned.

## What is the difference between JavaScript and jQuery?

JavaScript is a programming language used for web development, while jQuery is a library built with JavaScript that simplifies tasks like DOM manipulation and event handling. jQuery is essentially a framework that makes JavaScript easier to work with.

## What is the main function when working with jQuery?

The main function in jQuery is `$()`, which is used to select elements from the DOM so that you can manipulate or perform actions on them.

## What does the "$" sign mean in jQuery?

In jQuery, the "$" sign is an alias for the `jQuery` object. It's a shorthand way of calling jQuery functions and methods. For example, `$(selector)`is the same as`jQuery(selector)`.

## Describe the differences between working with the DOM in classic JavaScript and jQuery?

jQuery simplifies DOM manipulation by providing an easier and more concise syntax. It abstracts away some of the complexities of handling cross-browser issues, making it more user-friendly for developers compared to classic JavaScript.

## How to access the DOM element / elements in jQuery?

You can access DOM elements in jQuery by selecting them using the `$()` function. For example:

- To select an element with the ID "myElement": `$("#myElement")`
- To select all paragraphs: `$("p")`

## Give examples of complex jQuery selectors.

Complex jQuery selectors allow you to filter elements based on various conditions. For example:

- Select all anchor tags with an "href" attribute starting with "https": `$("a[href^='https']")`
- Select all input elements of type checkbox inside a form with the ID "myForm": `$("#myForm input[type='checkbox']")`

## How to ensure that the code is executed only after the page is fully loaded? Why is it necessary to do this?

You can ensure code is executed after the page is fully loaded by wrapping it in a `$(document).ready()` function. This is necessary to ensure that your code doesn't run before the DOM is fully loaded, preventing any potential issues.

## What are the .addClass(), .removeClass(), .toggleClass(), and .hasClass() methods used for in jQuery?

- `.addClass(className)`: Adds one or more class names to the selected element(s).
- `.removeClass(className)`: Removes one or more class names from the selected element(s).
- `.toggleClass(className)`: Toggles between adding and removing a class name on the selected element(s).
- `.hasClass(className)`: Checks if the selected element(s) have a specific class, returning `true` or `false`.

## What is the purpose of the event.preventDefault() function?

    `event.preventDefault()` is used to prevent the default behavior of an event. For example, in the context of a form submission, it prevents the form from submitting and the page from refreshing.

## What is a chain of commands in jQuery?

    A chain of commands in jQuery is a sequence of actions or methods that can be applied one after the other to a selected element or elements. This allows for concise and efficient code by stringing together multiple operations.

## How is the .delay() method used in jQuery? Does it have an analogue in classic JavaScript?

    The `.delay()` method in jQuery adds a delay before executing the next item in the animation queue. It's typically used for animations and effects. In classic JavaScript, you can achieve similar results using `setTimeout()` to introduce delays in your code.

## What is a jQuery plugin?

    A jQuery plugin is a piece of code that extends the functionality of jQuery. It allows you to add new methods, functions, or features to jQuery, making it more versatile and customizable for specific tasks or needs.

---

1. How to connect jQuery to the project?
2. What are the advantages and disadvantages of using the jQuery library?
3. What is the difference between JavaScript and jQuery?
4. What is the main function when working with jQuery?
5. What does the "$" sign mean in jQuery?
6. Describe the differences between working with the DOM in classic JavaScript and jQuery?
7. How to access the DOM element / elements in jQuery?
8. Give examples of complex jQuery selectors.
9. How to ensure that the code is executed only after the page is fully loaded? Why is it necessary to do this?
10. What are the .addClass(),.removeClass(),.toggleClass() and .hasClass() methods used for in jQuery?
11. What is the purpose of the event.preventdefault() function?
12. What is a chain of commands in jQuery?
13. How is the .delay() method used in jQuery? Does it have an analogue in classic JavaScript?
14. What is a jQuery plugin?
