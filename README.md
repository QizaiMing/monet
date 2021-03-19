# Monet API

## Setting up locally

To set the site up locally, you'll need to have Docker and Docker Compose installed.

1. Clone the repository

```bash
git clone https://github.com/QizaiMing/monet.git
```

2. Run the docker-compose file

```bash
docker-compose up
```

4. Open a new terminal and execute a terminal inside the django_server_monet_api image

```bash
docker exec -t -i django_server_monet_api bash
```

5. Apply migrations to the database

```bash
python manage.py migrate
```

6. Create you superuser

```bash
python manage.py createsuperuser
```

7. Run the django command that reads the file and saves it to the database

```bash
python manage.py extract_data
```

8. You can run tests

```bash
python manage.py test
```

9. You can view/edit file information on the admin using your superuser credentials

```bash
http://localhost:8000/admin
```

10. The API endpoint for checking a file

```bash
http://localhost:8000/api/file/<int:id>
```

&nbsp;&nbsp; Go to http://localhost:8000/ to view the site.
