##############
Pipeline CI/CD
##############

Introduction
============

.. attention::
    Avant de pousser des modifications sur le repository et enclencher le pipeline
        * Configurer les variable d'environnement sur Github      
        * Avoir un compte sur Render et configurer l'environement 

Le pipeline CI/CD est implémenté pour etre utilisé avec Github Actions, le ficher de configuration se trouve dans .github/workflows/main.yml
Le pipeline se déclenche lors d'un push ou d'une pull request sur le repository, sur la branche **master** le pipeline effectue toute les étapes et sur la branche **dev** seul les tests sont effectué.

Il contient plusieurs étapes:
    1. Tests
    2. Contenairisation avec Docker
    3. Déploiement automatique (optionel)

Tests
-----
Les tests du pipeline contiennent :
    * les test unitaire et d'intégration contenu dans les fichier tests de chaque application
    * s'assure d'une couverture des tests supérieur a 80%
    * test si erreur sur le linting

Contenairisation
----------------
Création d'une image Docker grâce au Dockerfile présent dans le projet, basé sur l'image python:3.11-slim et une fois contenairisé lance l'application sur un serveur Gunicorn.
Envoie l'image une fois construite sur le Docker Hub.

Déploiement
-----------
L'application est deployer sur Render (https://render.com/).
Le deploiement peut etre automatique ou manuel suivant la variable d'environnement AUTO_DEPLOY sur Github Secret.

Configuration pour Github Actions
=================================

Pour envoyer l'image construite sur le Docker Hub il faut renseigner son username et password de manière sécurisé avec Github Sercet.
Choisir le deploiement automatique ou non grâce a la variable AUTO_DEPLOY  

Sur Github, un fois dans le projet allez dans Settings -> Environments -> Secrets and variable.
    * **DOCKER_USERNAME**: <Nom d'utilisateur Docker>
    * **DOCKER_PASSWORD**: <Mot de passe Docker>
    * **AUTO_DEPLOY**: <True> pour deploiement automatique sinon <False>
    * **DEPLOY_HOOK**: <URL privé Deploy Hook>

Configuration pour Render
=========================
Une fois inscrit sur Render, créer un nouveau service puis configurer:
    * Source Code: Existing image
    * Image URL: l'url de votre image sur le Docker Hub
    * Cliquer sur Connect
    * Name: Le nom du service qui sera votre futur addresse du type <nom_du_service>.onrender.com.
    * Le type d'instance (version gratuite possible)
    * Copier votre URL privé Deploy Hook et la mettre dans Github Secret

Configurer les variables d'environnement de votre nouveau service:
    * **DEBUG:** False
    * **HOST**: <nom_du_service>.onrender.com
    * **SECRET_KEY**: <clé secrete pour Django>
    * **SENTRY_DSN**: <url sentry dsn>
