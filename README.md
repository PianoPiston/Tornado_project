🧩 Requirements
* Python 3
* pip3

⚙️ Installation
First, install Django using pip:
```console
$ pip3 install django
```
🚀 Usage
Clone the repository and navigate into the project folder:

```console
$ git clone <repository_url>
$ cd <repository_folder>
```

Run database migrations:
```console
$ python3 manage.py makemigrations resource_map
$ python3 manage.py migrate
```

(Optional) Populate the database with sample data:
```console
$ python3 manage.py populate_data
```

Start the development server:
```console
$ python3 manage.py runserver
```

Open your browser and visit:
👉 http://127.0.0.1:8000

🗺️ Page Layout
Page	            URL Path	  Description
Introduction	    /	          Homepage or overview
Login	            /login	    User login page
Volunteer Form	  /add	      Add new volunteer data
Dashboard	        /dashboard	User dashboard
Supervisory Map	  /map	      Map view of resources

