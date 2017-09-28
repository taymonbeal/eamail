# EA Boston Mailing List & Site

[Vagrant](https://www.vagrantup.com/) is the officially supported method of setting up a development environment for this project.

Once Vagrant is installed, from the main (eamail) directory, use the `vagrant up` command to start the VM and the `vagrant ssh` command to enter it, then navigate to the project directory from within the Vagrant VM and use the `runserver` command to run the website (and email-sending) systems. Note that `vagrant up` is used both to create the VM the first time you run it, and to start the VM after it has been created.

The site will be viewable at <http://0.0.0.0:8000/> or <http://localhost:8000/>.

Some content should be added through the admin interface (at <http://0.0.0.0:8000/admin/> or <http://localhost:8000/admin/>, username and password 'admin'). This content consists of the interests "Major events", "Harvard College Effective Altruism", "Harvard University Effective Altruism", "MIT Effective Altruism", "Tufts Effective Altruism", and "Somerville meetup group", and placeholder events. Placeholder events must have a title, an image with a 3x2 aspect ratio, a start time (and optional end time), description text, and interests assigned. Events should have one of the interests that is not "Major events" assigned, and may also have the "Major events" interest assigned.

Subscribers should not be added through the admin interface, but rather by signing them up on the main page. This will automatically assign them tokens. Emails can be sent to subscribers with the `django-admin sendnewsletter` command. These emails will then be sent not to the actual email addresses but rather to MailCatcher, and can be viewed at <http://localhost:1080/>. Subscribers are **not** users, and do not have passwords.

Zurb Foundation for Emails instructions for drafting email templates are in `zurb/README.md`.
