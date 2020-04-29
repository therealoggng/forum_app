# Test App
i am running project is name Forum . I create project with commands: >django-admin startproject forum 
But before creating a project you must make sure that you have installed Django, if not, here's a link to you:https://docs.djangoproject.com/en/3.0/topics/install/. Then i created app , with commands: "django-admin startapp app" and immediately set up in the settings , first plugged in INSTALLED_APPS is our app also connected his database in postgres , you can read here about connecting the postgres/mysql/etc databases:https://docs.djangoproject.com/en/3.0/ref/databases/.
Basic model
~Question
fields: question_text
        pub_date
~Choice
fields: question
        choice_text
        votes
Also i connected templates index.html and detail.html, set up in urls.py there i attached patterns, and in view i added exception 404 if the answer or question is not found
