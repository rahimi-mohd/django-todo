# Yet Another Django-Todo App.

This app use Django as backend and Html with Bootstrap5 on the frontend. Note that I choose to use Function Based View (FBV) instead of Class Based View (CBV) because I wanted to understand better how to do things in Django. 

### How To:

To use this Todo App, there are several steps that you need to do:

1. Clone this repo
```
$ git clone {repo url}
```

2. Activate environment [OPTIONAL BUT RECOMMENDED]
```
$ python -m venv venv
$ source venv/bin/activate
```

> For Windows user, please see your OS documentation for permission's stuff. This answer from StackOverflow seem to be working fine with me [Here](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows).

3. Install all the requirements
```
$ pip install -r requirements.txt 
```

4. Database migration
```
$ ./manage makemigrations
$ ./manage migrate

# You can also create super user to be use in admin page
$ ./manage createsuperuser # and follow the instruction
```

5. Activate server
```
$ ./manage runserver # there will be link provided or you can go to http://localhost:8000 on your browser.
```

### What's working
1. User registration, Login and Logout.
2. Add Todos, Change Todos Status from In Progress to Done, Delete Todos.

### Testing is currently work in progress
Functional testing will be write using Playwright.

There're also several step that needed to be done before we can start functional testing. Playwright should already be install if you follow step 3: Install all the requirements. Next step:

1. Install playwright's requirement [here](https://playwright.dev/python/docs/intro), or follow this instruction:

```
$ playwright install
```

2. Run pytest, there will be no browser open by default, so you can add `--headed` to invoke browser. You also can make it slower by using `--slowmo={n}`. Here's the command I use to run playwright with browser and slower time:

```
$ pytest --headed --slowmo=1000
```

