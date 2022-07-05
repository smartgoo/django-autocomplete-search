# Django Autocomplete Search
This is a small project that serves as a demo implementation of a simple Django autocomplete search solution.

Please refer to the [associated blog post here](https://www.chuckvallone.com/blog/a-simple-django-autocomplete-search-solution-for-low-complexity-search-requirements) for more information.


# This Autocomplete Solution
The autocomplete search solution used here is simple and meant for low-complexity search requirements. Why go through the hassle of implementing and managing a dedicated search service or library if it really isn't necessary.


# A Few Notes
- The data searched against in this project is a small listing of stocks. The listing comes from a csv that is part of this project. In a real world app, your data will likely come from your database or an external API.
- The front end implementation using HTMX is intentionally left bare bones and feature incomplete. The core functionality of making the Ajax request and rendering results is there. This is meant to focus on the Django implementation, not the front end rendering and UX. 


# Getting Started
If you want to run the project locally, clone it and then go through the following steps:

1) Create a virtual env and activate it:
```
python -m venv env
source env/bin/activate
```

2) Install the required Python packages:
```
pip install -r requirements.txt
```

3) Fire up Django
```
python manage.py runserver
```
