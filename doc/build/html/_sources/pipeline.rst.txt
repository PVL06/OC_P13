##############
Pipeline CI/CD
##############

Introduction
============

.. attention::
    Avant de pousser des modifications sur le repository et d'enclencher le pipeline. 
    Assurez-vous de suivre ces étapes :

    * **Configurer les variables d'environnement sur GitHub** : Assurez-vous que toutes les variables d'environnement nécessaires sont configurées dans les paramètres de votre repository GitHub.
    * **Avoir un compte sur Render et configurer l'environnement** : Créez un compte sur Render et configurez l'environnement pour le déploiement de votre application.

Le pipeline CI/CD est implémenté pour être utilisé avec GitHub Actions. Le fichier de configuration se trouve dans .github/workflows/main.yml.

Le pipeline se déclenche lors d'un push ou d'une pull request sur le repository. Voici les actions spécifiques pour chaque branche :

    * **Branche master** : Le pipeline exécute toutes les étapes.
    * **Branche dev** : Seuls les tests sont exécutés.

Le pipeline contient plusieurs étapes :

    * **Tests** : Exécution des tests automatisés pour vérifier la qualité du code.
    * **Conteneurisation avec Docker** : Création d'une image Docker pour l'application.
    * **Déploiement automatique** (optionnel) : Déploiement de l'application sur l'environnement de production.


Tests
-----
Les tests du pipeline incluent les éléments suivants :
    * **Tests unitaires et d'intégration** : Exécution des tests unitaires et d'intégration contenus dans les fichiers de tests de chaque application.
    * **Couverture des tests** : Vérification que la couverture des tests est supérieure à 80 %.
    * **Linting** : Vérification des erreurs de linting pour s'assurer que le code respecte les normes de style.


Contenairisation
----------------
| Une image Docker est créée à l'aide du fichier Dockerfile présent dans le projet.
| Cette image est basée sur l'image python:3.11-slim. Une fois l'application conteneurisée, elle est lancée sur un serveur Gunicorn.
| L'image Docker, une fois construite, est envoyée sur Docker Hub avec un tag correspondant à l'identifiant du commit. De plus, l'image avec le tag latest sera remplacée par la nouvelle image.

Déploiement
-----------
L'application est déployée sur Render (https://render.com/).
Le déploiement peut être automatique ou manuel, en fonction de la variable d'environnement AUTO_DEPLOY configurée dans les secrets GitHub.

Configuration pour Github Actions
=================================

Pour envoyer l'image Docker construite sur Docker Hub, vous devez renseigner votre nom d'utilisateur et votre mot de passe de manière sécurisée en utilisant les secrets GitHub.
Vous pouvez choisir entre un déploiement automatique ou manuel en configurant la variable d'environnement AUTO_DEPLOY.

Sur Github, un fois dans le projet allez dans Settings -> Environments -> Secrets and variable.
    * **DOCKER_USERNAME**: <Nom d'utilisateur Docker>
    * **DOCKER_PASSWORD**: <Mot de passe Docker>
    * **AUTO_DEPLOY**: <True> pour deploiement automatique sinon <False>
    * **RENDER_DEPLOY_HOOK**: <URL privé Deploy Hook>

Configuration pour Render
=========================
    Créer un nouveau service :
        * Source Code : Sélectionnez Existing image.
        * Image URL : Entrez l'URL de votre image sur Docker Hub.
        * Cliquez sur Connect.

    Configurer les paramètres du service :
        * Name : Choisissez un nom pour le service. Ce nom sera utilisé pour générer l'adresse de votre service, par exemple <nom_du_service>.onrender.com.
        * Type d'instance : Sélectionnez le type d'instance souhaité (la version gratuite est disponible).

    Configurer le Deploy Hook :
        * Copiez l'URL privée du Deploy Hook fournie par Render.
        * Ajoutez cette URL dans les secrets GitHub de votre projet.

    Configurer les variables d'environnement :
        * DEBUG : False
        * HOST : <nom_du_service>.onrender.com
        * SECRET_KEY : <clé secrète pour Django>
        * SENTRY_DSN : <URL Sentry DSN>

