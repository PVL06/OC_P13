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

Pour commencer, assurez-vous de remplir les conditions suivantes :
   * **Cloner le projet** : Assurez-vous d'avoir cloné le dépôt du projet sur votre machine locale.
   * **Compte Sentry** : Inscrivez-vous sur Sentry et obtenez votre DSN (Data Source Name).

**Configuration du fichier .env**

Ajoutez un fichier .env à la racine du projet.
Ce fichier contiendra les variables d'environnement nécessaires pour le lancement en local.
Ajouter un fichier .env a la racine du projet qui contiendra les variables d'environnement pour le lancement en local.

Voici un exemple de contenu pour le fichier .env :

.. code-block::

   # Django Settings
   SECRET_KEY=<your secret key>
   DEBUG=True

   # Sentry Settings
   SENTRY_DSN=<your sentry dsn>

Lancement du serveur en local
=============================

.. code-block:: bash

   python manage.py runserver

Lancement du serveur depuis l'image du Docker Hub
=================================================

Avant de commencer, assurez-vous de remplir les conditions suivantes :

   * **Fichier .env configuré** : Assurez-vous d'avoir configuré le fichier .env à la racine du projet avec les variables d'environnement nécessaires.
   * **Docker installé** : Assurez-vous d'avoir Docker installé sur votre machine.


.. code-block:: bash

   docker pull pvldocker/lettings:latest
   docker run --rm -d -p 8000:8000 --env-file .env pvldocker/lettings:latest

Lancement du site
=================

Dans votre navigateur, entrez l'une des adresses suivantes :
   * 127.0.0.1:8000
   * localhost:8000

