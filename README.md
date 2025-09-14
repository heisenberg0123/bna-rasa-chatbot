# BNA Rasa Chatbot

Ce projet implémente un chatbot basé sur Rasa pour répondre aux requêtes des utilisateurs de la banque BNA, comme "Combien d'employés ?" ou "Statut de ma transaction", avec des réponses adaptées aux rôles.

## Fonctionnalités
- Réponses basées sur les rôles (Admin, Financiere, OperationsManager, Clerk).
- Requêtes dynamiques via des appels au backend Spring Boot.
- Gestion des intents comme les demandes de statistiques ou d'informations personnelles.
- Intégration avec l'interface Angular pour une expérience utilisateur fluide.

## Prérequis
- Python 3.8+ (vérifiez avec `python --version`)
- Backend Spring Boot en cours d'exécution sur `http://localhost:8091`.

## Installation après clonage
1. Clonez le dépôt :
   
   git clone https://github.com/heisenberg0123/bna-rasa-chatbot.git
   cd bna-rasa-chatbot
   python -m venv venv
   pip install -r requirements.txt
   rasa train
   rasa run actions
   rasa run --enable-api --cors "*"
