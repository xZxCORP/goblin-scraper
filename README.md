# Goblin Scraper API

<img src="https://media.istockphoto.com/id/1329042362/fr/vectoriel/mignon-gobelin-mascotte-personnage-dessin-anim%C3%A9-ic%C3%B4ne-illustration-vectorielle.jpg?s=612x612&w=0&k=20&c=hCQcXZfom7E1llL_v0alNFgPzHZEjLCChFDahJGBbxE=" width=200>

## Résumé

Goblin API est un projet en Python utilisant FastAPI pour récupérer automatiquement des données depuis la plateforme publique [HistoVec](https://histovec.interieur.gouv.fr/). Cette API permet d'accéder à des informations historiques sur les véhicules en France, comme les changements de propriétaire et les éventuels sinistres.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/xZxCORP/goblin-scraper.git goblin-scraper
   cd goblin-scraper
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application :
   ```bash
   fastapi dev index.py
   ```

## Exemple de requête

```bash
curl -X GET "http://127.0.0.1:8000/status"
```
