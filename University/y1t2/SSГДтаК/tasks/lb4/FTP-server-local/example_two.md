# Markdown Guide for Web Development

Markdown is a lightweight markup language that allows you to write formatted text using a [[plain]] text editor. Here is a guide to some of the more advanced features of Markdown that you can use in web development.

## Tables

Tables in Markdown can be a bit challenging, so it's recommended to use [[HTML]] markup instead for more complex layouts. However, for simple two-column tables, you can use lists with strong text instead of Markdown tables. Here's an example of a table:

```
| Default aligned | Left aligned | Center aligned  | Right aligned  |
|-----------------|:-------------|:---------------:|---------------:|
| First body part | Second cell  | Third cell      | fourth cell    |
| Second line     | foo          | **strong**      | baz            |
| Third line      | quux         | baz             | bar            |
```

## Links

When creating links in Markdown, it's important to use meaningful link text that describes the content of the link. Here's an example of how to create a link:

```
[Link text](https://www.example.com)
```

## Collapsible Content

You can use a collapsed content section to hide information until a user clicks on the summary text. Here's how to create a collapsible content section:

```
<details>
  <summary>This is the summary text, click me to expand</summary>
  This is the detailed text.
</details>
```

## Front Matter

Front matter is metadata that goes at the beginning of a Markdown document, preceding the content. It's used by static site generators like Jekyll, Hugo, and many other applications. To use front matter in GitLab, it must be between delimiters and at the very top of the document. Here's an example of how to use front matter:

```
---
title: Example Title
---
```

## Task Lists

In GitLab issues, merge requests, and comments, you can create task lists that users can check off as they complete tasks. Here's an example of how to create a task list:

```
- [x] Completed task
- [~] Inapplicable task
- [ ] Incomplete task
```

## Diagrams

In GitLab wikis, you can use the diagrams.net editor to create diagrams. You can also edit diagrams created with the diagrams.net editor. A Markdown image reference to the diagram is inserted in the wiki content.

## Advanced Markdown Features

For more advanced Markdown features, such as syntax highlighting, footnotes, tables, and more, see the [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
