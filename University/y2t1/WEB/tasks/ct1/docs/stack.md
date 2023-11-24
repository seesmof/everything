- JavaScript
- React
- Next.JS
- TailwindCSS
- TMDb API

---

I have this Flickster movies browser/catalog built using NextJS and TailwindCSS and a TMDb API. It has 4 pages - about, genres, movies, home. at home it has sections with popular and trending movies and a search bar. at movies it has a catalog of all the movies with filtering and sorting options as well as pagination. at genres it has a grid of available genres and each one leads to movies with appropriate genre selected. at about it has a brief description of the app, my motivation behind it, some history, and a contact form. The app is deployed on Vercel. it also has a navbar with links to the other pages and a search bar, but on larger screens only. on smaller screens it moves to the bottom and contains only the links. everything seems to be relatively neatly organized into components, pages, separate files, etc. and i can drop you whatever code you need. oh, and also it has a page for each movie, its dynamic so it uses just a template and fills in the data via an API by given id. and so this project is my last project for the discipline called "Web development and design" this semester so i would like you to help me with the report which is massive honestly. are you ready? please just confirm before we continue.

---

# Description of the Decisions Made

The design and implementation decisions made for the Flickster application were primarily aimed at enhancing user experience and usability across different screen sizes.

## Navbar Design

The navbar was designed to be responsive, adapting to different screen sizes. On smaller screens, the navbar is positioned at the bottom of the screen, providing four section buttons for navigation. This design decision was made to ensure that the navbar remains functional and easily accessible on smaller devices.

On larger screens, the navbar is positioned at the top of the screen, incorporating a project logo as a link to the home page and a search bar for movie search. This design decision was made to provide a more visually appealing and user-friendly interface on larger screens, while still maintaining functionality.

The navbar is also designed to be sticky, meaning it maintains a fixed position on the screen. This decision was made to improve usability and user experience by ensuring that the navbar is always accessible, regardless of the user's scroll position on the page.

## Catalog Page Design

On the catalog page, a filtering and sorting section is incorporated beside the movies grid. This section is designed to be sticky for the entire section height on larger screens, meaning it follows the user downwards as they scroll. On smaller screens, it remains at the top.

This design decision was made to improve user experience and make it easier for the user to sort and filter the movies catalog. By keeping the sorting and filtering options visible as the user scrolls, we aim to provide a more seamless and efficient browsing experience.

## "Go Back to Top" Button

At the bottom of the search results on the movies search page, there is a "Go back to top" button. This button is designed to improve user experience by providing a quick and easy way for users to navigate back to the top of the page, especially when dealing with a large number of search results.

The button is designed with an upwards-facing chevron icon, which is universally recognized as a symbol for upward movement or navigation. This design decision was made to ensure that the button is easily recognizable and intuitive to use.

In conclusion, the design decisions made for the Flickster application were guided by the principles of usability, user experience, and responsiveness. By considering the needs and preferences of different user groups, we were able to create a web application that is not only functional but also visually appealing and easy to navigate.
