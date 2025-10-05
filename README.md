# About
This project is a prototype built in a hackathon in one and 6 hours:
The project is an interactive map allowing military/medical access to civilian resources and expertise/assistance in times of emergencies, such as natural disasters or wars.
Markers are created by individuals and organisations who volunteer their skills and help in cases of emergency. The condition and availability of resources and skillsets are
modifiable by their respective creators.

features: 
filter out out-of-range resources by clicking on your position and entering a radius to see availability
MGRS coordinates provided on top of longitude and latitude
search for resources needed by using the provided search bar
AI searches resources and generates markers & summaries [not implemented]

🧩 Requirements
* Python 3
* pip3
* Django

⚙️First, install Django using pip:
```console
$ pip3 install django
```
🚀 Next, clone the repository and navigate into the project folder:

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

🗺️ Pages to visit
/           # end user goes here
/login      # user logs in
/add        # user can add resources
/dashboard  # user can manage resources
/map        # authorities' view, they can see available resources, locations and contact information

# Preview
<img width="1920" height="1080" alt="Screenshot_20251005_162841" src="https://github.com/user-attachments/assets/448752c4-4625-46dc-8747-f0fb4ad2134c" />

<img width="1920" height="1080" alt="Screenshot_20251005_163022" src="https://github.com/user-attachments/assets/696a3fa0-45f3-45b9-a9f0-9e0d71a5d6f0" />

<img width="1224" height="456" alt="Screenshot_20251005_163102" src="https://github.com/user-attachments/assets/5648fe77-46ea-421a-a98b-6153bc103f7c" />

<img width="928" height="754" alt="Screenshot_20251005_163206" src="https://github.com/user-attachments/assets/51daf719-375e-4d74-9ea4-c52898bd7c5f" />


