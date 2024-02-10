# Hack-4-Good-Smart-Event

## Introduction

This documentation is part of our ground-up initiative aimed at developing a platform for tracking user data efficiently.

## Guide

Upon accessing the home URL, users will find a concise description of our web application. Users can choose to either log in or sign up as a participant or an admin. For admins, authentication requires both a username and password, while participants only need to enter their username.

### For Admins:

- Upon authentication, admins will be directed to the admin events page.
- Here, they can generate events to populate the table or manually create events by providing a name, description.
- During an event's duration, participants can view the event details.
- Admins have the authority to end events at their discretion.
- Clicking on an event redirects the admin to the event's dashboard page, where they can access survey and participant details.
- Admins can create surveys in JSON format for participant feedback.
- After participants complete the survey, admins can extract data, including average time spent by all participants and an AI summary of the survey feedback.

### For Participants:

- Participants, upon logging in or signing up, will be directed to the participant events page.
- Here, they can access events and view associated surveys after generating events.
- To mark their attendance, participants must first check in, specifying the time of entry.
- They can then proceed to answer the survey questions, which include multiple-choice and open-ended formats.
- Once they have completed the survey, participants can check out, returning them to the homepage.

## Tech Stack

The Smart-Events application utilizes Angular for the frontend and Django for the backend, coupled with a temporary SQLite database. Django, renowned for its comprehensive authentication libraries and middleware, offers a wide array of user authentication methods. Angular, developed by Google, integrates with Django's Model-View-Controller (MVC) architecture, facilitating clear and structured component-based development. This synergy enhances the usability of Angular, as all methods are distinctly defined within separate components, creating efficient development practices.

## Problems

Regrettably, due to scheduling conflicts and inconvenient timing, collaborative efforts were hindered, rendering it impractical to execute the project as a team. Consequently, significant functionality was compromised. Additionally, encountered challenges arose in the frontend validation method, contributing to further setbacks in the development process.

## Future Ideas

- Enhancing the front-end design to improve user experience and aesthetics.
- Implementing real-time database analysis to provide immediate insights into event dynamics.
- Expanding the capabilities of AI to analyze a broader range of patterns and behaviors.
- Incorporating demographic information on the participant side to enrich data analysis.
- Implementing functionality to export data in various file formats for further analysis.
- Utilizing Python machine learning models to identify trends over time, enabling predictive analytics and informed decision-making.
