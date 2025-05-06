############
Installation
############

Installation du projet
======================

Cloner le projet:

.. code-block:: bash

   git clone https://github.com/PVL06/OC_P13.git

Création et activation de l'environnement virtuel:

.. code-block:: bash

   cd OC_P13
   python -m venv .venv
    
   # windows
   .venv\Scripts\activate
   # linux
   source .venv/bin/activate

Installation des dépendances:

.. code-block:: bash

   pip install -r requirements.txt

Variables d'environnement
=========================

Prérequis:
    * Avoir cloné le projet
    * Etre inscrit sur sentry et avoir son DSN

Ajouter un fichier .env a la racine du projet qui contiendra les variables d'environnement pour le lancement en local.

Template pour le fichier .env

.. code-block::

   SENTRY_DSN=<your sentry dsn>
   SECRET_KEY=<your secret key>
   DEBUG=True

Lancement du serveur en local
=============================

.. code-block:: bash

   python manage.py runserver

Lancement du serveur depuis l'image du Docker Hub
=================================================

prérequis:
    * avoir le ficher .env configuré
    * Avoir Docker installé sur sa machine

.. code-block:: bash

   docker pull pvldocker/lettings:latest
   docker run --rm -d -p 8000:8000 --env-file .env pvldocker/lettings:latest

Lancement du site
=================

Dans votre navigateur entrez l'adresse:
    | 127.0.0.1:8000
    | ou 
    | localhost:8000

