# CP1404 Assignment 2 - Movies2See 2.0 by MA YONGJIN

A Python project with GUI and Console programs that (re)use classes to manage a list of movies.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you?

Estimate:
I estimated that the project would take around 20 hours to complete, considering the need to learn aspects of Kivy for the GUI, integrate classes, and write tests.

Actual:
The project actually took me about 25 hours to complete. The additional time primarily came from debugging the GUI interactions and ensuring data integrity when loading and saving movies.

...

## 2. What are you most satisfied with?

I'm most satisfied with how the GUI turned out. Using Kivy to create a user-friendly interface that dynamically updates the movie list based on user interactions was particularly rewarding. It was gratifying to see the theoretical knowledge of GUI programming being effectively applied to a real-world application.

## 3. What are you least satisfied with?

I am least satisfied with the error handling in the initial stages of development. I found that my first approach to managing exceptions wasn't robust enough, which led to some crashes when unexpected inputs were tested. I had to go back and refine this aspect several times to ensure stability.

## 4. What worked well in your development process?

I am least satisfied with the error handling in the initial stages of development. I found that my first approach to managing exceptions wasn't robust enough, which led to some crashes when unexpected inputs were tested. I had to go back and refine this aspect several times to ensure stability.

## 5. What about your process could be improved the next time you do a project like this?

In future projects, I plan to spend more time on the planning and design phase, particularly in designing the data structures and GUI layout before diving into coding. I realized that some time was wasted reworking parts of the GUI and data handling that could have been optimized with better initial planning.

## 6. Describe what learning resources you used and how you used them.

I heavily relied on the Kivy documentation to understand the specifics of implementing various GUI components like buttons, spinners, and dynamic updates. Online forums and stack overflow were also helpful in solving specific issues related to Python classes and Kivy interactions. Additionally, I reviewed several tutorials to better understand Python's class mechanics.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

One of the main challenges was ensuring that the GUI correctly interacted with the back-end data structures. Initially, updates in the GUI did not reflect immediately in the data. I overcame this by implementing observer patterns and ensuring that changes to the data triggered updates in the GUI.

## 8. Briefly describe your experience using classes and if/how they improved your code.

Using classes significantly improved the organization and maintainability of the code. By encapsulating movie data and operations within a Movie and MovieCollection class, I was able to keep the GUI code clean and focused solely on presentation logic. This separation of concerns made the code easier to manage and extend.
