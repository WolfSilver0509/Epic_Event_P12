# Développez une architecture back-end sécurisée en utilisant Django ORM


Projet n°12 de la formation développeur d'Application Python.

:lock: ## Introduction : 

Vous travaillez chez Epic Events, une entreprise de conseil et de gestion dans l'événementiel qui répond aux besoins des start-up voulant organiser des « fêtes épiques ».

En tant que développeur de logiciels dans le département informatique, vous avez principalement travaillé sur le site Internet de l'entreprise destiné à la clientèle et vous vous êtes bâti une réputation de « responsable sécurité » dans votre équipe.

L'entreprise est très appréciée pour les fêtes et les événements hors du commun qu'elle organise pour ses clients de renom. En interne, l'essentiel de votre travail consiste à gérer le logiciel obsolète de gestion de la relation client (CRM) de l'entreprise, qui effectue le suivi de tous les clients et événements.

Cahier des charges:

* Utiliser Python 3.
* Empêcher une injection SQL.
* Veiller à gérer les entrées des utilisateurs pour prévenir une injection SQL en :
        ** utilisant Django ORM ;
        ** évitant d'utiliser les requêtes SQL brutes à moins que cela ne soit absolument nécessaire.
* Garantir l'authentification.
* Activer et utiliser le framework d'authentification Django dans les paramètres (django-admin startproject).
* Mettre en œuvre et faire appliquer le principe du moindre privilège lors de l'attribution de l'accès aux données. 
* Veiller à ce que les utilisateurs n'aient accès qu'aux données dont ils ont besoin.
* Supprimer les erreurs d'autorisation ou les droits de contrôle d'accès incorrectement configurés qui permettent un accès non autorisé.
* Mauvaises configurations de sécurité. S'assurer que toutes les vues disposent de décorateurs et/ou de contrôles de logique pour les configurations de sécurité :
        ** Les autorisations d'utilisateur sont appropriées
        ** Les méthodes HTTP utilisées dans la requête sont autorisées.
        ** Effectuer le logging et la surveillance. Toutes les applications doivent consigner les exceptions et les erreurs produites.


:pushpin: ## Utilisation : Voici la liste des outils utilisées pour ce projet :

#### Outils : 

* Django Rest Framwork 
* JWT Token
* Postman
* PostgreSQL

### Librairies Python :

asgiref==3.7.2
black==23.3.0
click==8.1.3
colorama==0.4.6
Django==4.2.2
djangorestframework==3.14.0
djangorestframework-jwt==1.11.0
djangorestframework-simplejwt==5.2.2
mypy-extensions==1.0.0
packaging==23.1
pathspec==0.11.1
platformdirs==3.5.3
psycopg2==2.9.6
PyJWT==1.7.1
pytz==2023.3
sqlparse==0.4.4
tomli==2.0.1
typing_extensions==4.6.3
tzdata==2023.3



:pushpin: ## Installation du projet : 


:floppy_disk: ### PostgreSQL
Vous devez avoir PostgreSQL, version 14 minimum, installé sur votre ordinateur (si ce n'est pas le cas vous pouvez le télécharger [ici - PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

:mag: Suite a ça je vous laisse installer ce logiciel sur votre ordinateur. Si vous avez des diffuculter vous pouvez suivre ce [tuto](https://www.postgresql.r2schools.com/how-to-install-postgresql-11-and-pgadmin-on-windows-11/) sur l'installation complete.

:point_right: Pour la suite je vous laisse crée une base de donnée que nous allons nommée epicevent_db par exemple : 

```
CREATE DATABASE epicevent_db;
```
:point_right: Ensuite nous allons crée un user pour cette base de donner , par exemple  user = lyoko avec un mots de passe = password":

```
CREATE USER lyoko WITH ENCRYPTED PASSWORD 'password';
```
:point_right: Ensuite nous accordons tous les privilèges de cette base de données spécifique à notre utilisateur spécifié.

```
GRANT ALL PRIVILEGES ON DATABASE epicevent_db TO lyoko;
```

Une fois cela fait vous pouvez vous rendre sur l'application pgAdmin 4 et voir votre base de donnée vide mais présente ! 

:computer: ### Python
Vous devez avoir Python, version 3.9 minimum, installé sur votre ordinateur (si ce n'est pas le cas vous pouvez le télécharger [ici - Python](https://www.python.org/downloads/))


:mag: Ensuite téléchargez le repo version zip sur github  :


:point_right: Créez un nouveau dossier sur votre bureau avec le nom que vous souhaitez par exemple le nom du projet : EpicEvent_P12



:point_right: Dé-zippez le contenu du dossier zip dans ce nouveau dossier : EpicEvent_P12



Une fois cela fait ouvrez le terminal de commande (Invite de commande) :



:point_right: Une fois le terminal ouvert nous allons rejoindre notre bureau dans un premier temps
```
cd desktop
```
:point_right: Ensuite nous allons rejoindre notre nouveau dossier sur le bureau
```
cd EpicEvent_P12
```
:point_right: Une fois là nous allons créer notre environnement virtuel ( exemple : envVirtuel ) sur python avec cette commande
```
python -m venv envVirtuel
```
:point_right: Une fois l'environnement créé nous allons nous rendre dans le dossier de l'environnement virtuel afin de l'activer:


Pour cela il nous faut récupérer le chemin du dossier:


* Rendez-vous sur votre bureau
* Allez dans le dossier "SoftDesk_P10"
* Maj + Clic Droit sur le dossier "envVirtuel"
* Faire : "Copier en tant que chemin d'accès"



:point_right: Une fois cela fait, retournez sur le terminal copiez votre chemin d'accès en rajoutant "\Scripts\activate" à la fin :
```
C:\Users\wolf\Desktop\EpicEvent_P12\envVirtuel\Scripts\activate
```
:point_right: Si tout va bien vous devez voir apparaître un (env) à côté de votre chemin d'accès, comme ceci
```
(env) C:\Users\wolf\Desktop\EpicEvent_P12>
```
:point_right: Déplacez-vous dans le dossier source du projet qui se nomme EpicEvent, comme ceci
```
(env) C:\Users\wolf\Desktop\EpicEvent_P12> cd EpicEvent
```
:point_right: Maintenant nous allons télécharger les librairies associés au projet nécessaire, pour cela tapez
```
pip install -r requirements.txt
```
:point_right: Par la suite avant de lancer votre serveur veillez à ouvrire un ide pour ouvrire votre projet.Dans setting.py du projet vous allez mettre à jour les informations de votre base de donnée dans la partie databases comme ci joint pour la connecter au projet : 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'epicevent_db',
        'USER': 'lyoko',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
:point_right: Une fois cela fait , vous vous rendez dans votre terminal afin de faire une migration ce qui va permettre de crées les tables du projet dans votre base de donnée. 
```
python manage.py migrate
```
:point_right: derniére étapes, vous allez crée un super_user qui va avoir les droits de crée vos différentes équipes ( VENTE , SUPPORT , GESTION ) :
```
python manage.py createsuperuser
```
:point_right: Suite à ça vous pouvez entrer les informations de votre super_user, comme fin vous aurez ce message :
```
Username (leave blank to use 'admin'): hopper
Email address: hopper@gmail.com
Password: ********
Password (again): ********
Superuser created successfully.
```
:computer: ### Tout est fin prêt, pour lancer votre projet Django  DRF sur un navigateur !


:point_right: Pour lancer le serveur tapez la commande suivante :
```
python manage.py runserver
``` 

:mag: Afin de tester les différentes endpoints du projets voici une documentation complete du projet  :  [ici - Documentation Postman](https://documenter.getpostman.com/view/17892890/2s93sZ7uPu#intro)


:mag: Il ne vous reste plus qu'à parcourir la documentation de Epic Event afin d'essayer toutes ces points de terminaison d'API.




<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a> <a href="https://postman.com" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" alt="postman" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>






