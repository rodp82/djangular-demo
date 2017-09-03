# Example Django Angular App
A basic application for learning django and angularjs through Pluralsight video tutorials.


## Instructions
1. Start up Vagrant VM
```sh
$ vagrant up
```

2. SSH into VM
```sh
$ vagrant ssh
```
3. Create Python VirtualEnv
```sh
$ cd ~
$ virtualenv django-env
```

4. Activate VirtualEnv
```sh
$ cd ~/django-env
$ . bin/activate
```

5. Install Django
```sh
$ pip install django
```

6. Run Migrations
```sh
$ python manage.py migrate
```

7. Start dev server
```sh
$ cd /vagrant/mysite
$ python manage.py runserver 0.0.0.0:8000
```

## Django Admin
1. Need to create a superuser
```sh
$ python manage.py createsuperuser
```