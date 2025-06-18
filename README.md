# PharmaAI Crew

## À propos du projet

PharmaAI Crew est un système d'agents IA conçu pour assister les pharmaciens d'officine, en particulier les débutants, dans leurs tâches quotidiennes. Le projet s'appuie sur le framework [crewAI](https://crewai.com) pour orchestrer une équipe d'agents spécialisés qui collaborent pour rechercher des informations, analyser des documents et fournir des réponses précises à des questions pharmaceutiques complexes.

L'objectif est de fournir un outil fiable et efficace pour aider à la prise de décision et alléger la charge de travail en automatisant les tâches de recherche d'informations.

## Démarrage rapide

Suivez ces étapes pour installer et lancer le projet sur votre machine.

### Prérequis

Assurez-vous d'avoir Python (version >= 3.10 et < 3.13) installé sur votre système. Ce projet utilise [UV](https://docs.astral.sh/uv/) pour la gestion des dépendances.

### Installation

1.  **Installer UV** (si ce n'est pas déjà fait) :
    ```bash
    pip install uv
    ```

2.  **Installer les dépendances du projet** :
    Depuis la racine du projet, exécutez la commande suivante pour créer un environnement virtuel et installer les paquets nécessaires :
    ```bash
    crewai install
    ```

### Configuration

Avant de lancer le projet, vous devez configurer votre clé d'API OpenAI.

1.  Ouvrez le fichier `.env` et ajoutez votre clé d'API :
    ```
    OPENAI_API_KEY="votre_clé_api_ici"
    ```

## Utilisation

Pour lancer la mission de votre équipe d'agents, exécutez la commande suivante depuis le dossier racine de votre projet :

```bash
crewai run
```

Cette commande initialise l'équipe PharmaAI, assemble les agents et leur assigne les tâches définies dans vos fichiers de configuration. Par défaut, l'exemple initial effectuera une recherche sur les LLM et créera un fichier `report.md` à la racine du projet avec les résultats.

## Personnalisation

Vous pouvez adapter le comportement de votre équipe en modifiant les fichiers de configuration :

-   `src/pharmaai/config/agents.yaml` : Définissez les rôles, objectifs et outils de vos agents.
-   `src/pharmaai/config/tasks.yaml` : Décrivez les tâches que les agents doivent accomplir.
-   `src/pharmaai/crew.py` : Ajoutez votre propre logique, des outils personnalisés ou des arguments spécifiques.
-   `src/pharmaai/main.py` : Modifiez les entrées (inputs) pour vos agents et vos tâches.

## Support

Pour toute question ou suggestion concernant PharmaAI Crew ou le framework `crewAI` :

-   Consultez la [documentation officielle](https://docs.crewai.com)
-   Visitez le [dépôt GitHub de crewAI](https://github.com/joaomdmoura/crewai)
-   Rejoignez la communauté sur [Discord](https://discord.com/invite/X4JWnZnxPb)

---
Créons des merveilles ensemble avec la puissance et la simplicité de crewAI.