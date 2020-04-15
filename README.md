This is a small and complete project, I developed for training a group of
graduates in using Python-Flask. I am making it available on github with the
hope that it will be useful to somebody.

The project requirements are given in ERMS.pdf. For structuring the
application I followed the Flask Mega-Tutorial
(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

Before running the application, database has to be initialised.
Run the following commands in the root directory:

    flask db init

    flask db migrate

    flask db upgrade

To run the application, again from the root directory run the following:

    export FLASK_APP=main.py

    flask run
