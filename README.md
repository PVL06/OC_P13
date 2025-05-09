## :one: Introduction

Ce projet s'inscrit dans le cadre du parcours "Développeur d'application Python" sur OpenClassrooms et a un but uniquement pédagogique.  

Le projet concerne la startup Orange Country Lettings, spécialisée dans la location de biens immobiliers.  
Le site web est construit avec le framework Django 3.2 et une base de donnée SQLite.  
La base du projet est disponible sur ce dépôt GitHub : https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.  

:link: [Documentation disponible sur Read the Docs](https://orange-project-13.readthedocs.io/en/latest/index.html)

## :two: Développement en local

#### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- Docker CLI (si contenairisation)
- Compte Sentry avec un projet configuré et une clé sentry DSN

#### Installation
Cloner le repository
```
git clone https://github.com/PVL06/OC_P13
```

Environnement virtuel
```
cd OC_P13
python -m venv .venv

# Activation sur linux/macOS
source .venv/bin/activate

# Activation sur windows
.venv/script/activate
```

Dépendances
```
pip install -r requirements.txt
```

#### Variables d'environnement

Ajoutez un fichier .env à la racine du projet.  
Ce fichier contiendra les variables d'environnement nécessaires pour le lancement en local.  

Voici un exemple de contenu pour le fichier .env:
```
# Django Settings
SECRET_KEY=<your secret key>
DEBUG=True

# Sentry Settings
SENTRY_DSN=<your sentry dsn>
```
#### Lancement du serveur en local

```
python manage.py runserver
```
Le site est disponible sur votre navigateur à l'adresse `127.0.0.1:8000` ou `localhost:8000`
L'interface d'administration est displonible à l'URL `http://localhost:8000/admin`
Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Image Docker en local
Construction d'une image
```
docker build -t <image-name>:<tag> .
```
Lancement d'un containeur
```
docker run --rm -d -p 8000:8000 --env-file .env <image-name>:<tag>
```
Le site et l'interface d'administration est disponible sur votre navigateur pareil au lancement via python manage.py runserver.

## :three: Pipeline CI/CD

Le pipeline CI/CD est implémenté pour être utilisé avec GitHub Actions. Le fichier de configuration se trouve dans .github/workflows/main.yml.  

Le pipeline contient 3 étapes:
- **test**: tests unitaire et d'intégration, test de couverture (valide si supérieur à 80%), test de linting
- **build-and-push**: Création d'une image Docker pour l'application et envoi sur le Docker Hub.
- **deploy**: L'application est déployée sur Render (optionnel).

#### Prérequis

- Compte sur Render
- Compte Github

#### Configuration pour Github Actions

Pour envoyer l'image Docker construite sur Docker Hub, vous devez renseigner votre nom d'utilisateur et votre mot de passe de manière sécurisée en utilisant les secrets GitHub.  
Vous pouvez choisir entre un déploiement automatique ou manuel en configurant la variable d'environnement AUTO_DEPLOY.  

Sur Github, un fois dans le projet allez dans Settings -> Environments -> Secrets and variable et definir les variables:
- **DOCKER_USERNAME**: `Nom d'utilisateur Docker`
- **DOCKER_PASSWORD**: `Mot de passe Docker`
- **AUTO_DEPLOY**: `True` pour deploiement automatique sinon `False`
- **RENDER_DEPLOY_HOOK**: `URL privé Deploy Hook`

#### Configuration pour Render
Créer un nouveau service :
- Source Code : Sélectionnez Existing image.
- Image URL : Entrez l'URL de votre image sur Docker Hub.
- Cliquez sur Connect.

Configurer les paramètres du service :
- Name : Choisissez un nom pour le service. Ce nom sera utilisé pour générer l'adresse de votre service, par exemple <nom_du_service>.onrender.com.
- Type d'instance : Sélectionnez le type d'instance souhaité (la version gratuite est disponible).

Configurer le Deploy Hook :
- Copiez l'URL privée du Deploy Hook fournie par Render.
- Ajoutez cette URL dans les secrets GitHub de votre projet.

Configurer les variables d'environnement :
- **DEBUG** : `False`
- **HOST** : `nom_du_service.onrender.com`
- **SECRET_KEY** : `clé secrète pour Django`
- **SENTRY_DSN** : `URL Sentry DSN`

#### Lancement du pipeline

Une fois les configurations faites, le pipeline se déclenche lors d'un push ou d'une pull request sur le repository.  
- Branche **master**: Toute les étapes du pipeline 
- Branche **dev**: Seulement la première étape (Test)
