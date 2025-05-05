######################
Architecture du projet
######################

Le projet est divisé en trois applications:
   * **oc_lettings_site** : Point d'entrée du projet, contenant les paramètres (settings), la configuration des URLs de base, ainsi que la vue pour la page d'accueil.
   * **lettings** : Contient la partie dédiée à la gestion des locations de biens.
   * **profiles** : Contient la partie dédiée à la gestion des utilisateurs.

Les applications **lettings** et **profiles** possèdent chacune leurs propres modèles, URLs, templates, tests et configurations d'administration. Cette organisation facilite les modifications ou les améliorations spécifiques à chaque application.

À la racine du projet, vous trouverez également les dossiers suivants :
   * **static** : Contient les fichiers statiques pour l'ensemble du site.
   * **templates** : Contient les fichiers HTML de base du site, y compris la page d'accueil et les pages d'erreur (404 et 500)
   * **doc** : Contient la présente documentation.

****************************
Application oc_lettings_site
****************************

Views
=====

.. automodule:: oc_lettings_site.views
   :members:
   :undoc-members:
   :show-inheritance:

********************
Application Lettings
********************

Views
=====

.. automodule:: lettings.views
   :members:
   :undoc-members:
   :show-inheritance:


Models
======

.. automodule:: lettings.models
    :members:
    :undoc-members:
    :show-inheritance:


********************
Application Profiles
********************

Views
=====

.. automodule:: profiles.views
   :members:
   :undoc-members:
   :show-inheritance:


Models
======

.. automodule:: profiles.models
    :members:
    :undoc-members:
    :show-inheritance: