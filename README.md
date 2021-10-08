# classik

## About the App
Classik is a web-based application where we can store, organize and manage our study notes in a very efficient manner. Thus, application makes a huge difference in storing and managing the notes such that the notes never get lost anywhere. The application will be built with **HTML, CSS, Javascript, Jquery, Bootstrap Framework** for Front-end and a popular Python framework called **Django** as a Backend it also uses **sqlite3** as Database to store the files.

## Installation

### Create Virtualenv with Python3

#### Installing Virtualenv with pip
```bash
pip install virtualenv
```
#### Creating a virtual environment named myenv to the project
```bash
virtualenv myenv
```

### Installing the Python Packages
#### Install dependencies into the virtual environment
```bash
pip install -r requirements.txt
```
### Creating the Admin account and making changes to the database
#### Create Superuser
```bash
python manage.py createsuperuser
```
#### Makemigrations of Project
```bash
python manage.py makemigrations
```
#### Migrate Project or Single App
```bash
python manage.py migrate
```
### Run Locally
#### Start the server

```bash
  python manage.py runserver
```

## Screenshots

### Before Login
![HomeScreen](screenshots/homescreen.png?raw=true "HomeScreen")

### User Signup
![user_signup](screenshots/user_signup.png?raw=true "user_signup")

### User Signin
![user_signin](screenshots/user_signin.png?raw=true "user_signin")

### After Signin
![after_signin](screenshots/after_signin.png?raw=true "after_signin")

### Creating a new classroom
![creating_new_classroom](screenshots/creating_new_classroom.png?raw=true "creating_new_classroom")

### join a existing classroom
![join_a_existing_classroom](screenshots/join_new_classroom.png?raw=true "join_a_existing_classroom")

### Inside the classroom
![Inside_classroom](screenshots/Inside_classroom.png?raw=true "Inside_classroom")

### Adding a new Announcement to the classroom
![adding_new_announcement](screenshots/adding_new_announcement.png?raw=true "adding_new_announcement")

### Announcement
![announcement](screenshots/announcement.png?raw=true "announcement")

### Classroom Peers
![all_peers](screenshots/all_peers.png?raw=true "all_peers")


## Author

- [@Rakeshgombi](https://www.github.com/Rakeshgombi)
