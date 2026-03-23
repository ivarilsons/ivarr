# 🎓 FSDM Student Portal — S5 MI-GI

Projet complet en 2 étapes:

## Structure du projet
```
project/
├── scraper.py        ← scrape les notes du site FSDM
├── index.html        ← le portail web (frontend)
├── students_data.json ← généré par le scraper
└── requirements.txt
```

## Étape 1 — Scraper les notes

### Installation
```bash
pip install requests beautifulsoup4 tqdm --break-system-packages
```

### Lancer le scraper
```bash
python3 scraper.py
```
→ Génère `students_data.json` avec toutes les notes

## Étape 2 — Lancer le site

### Option A: Simple (Python)
```bash
python3 -m http.server 8080
```
→ Ouvrir http://localhost:8080

### Option B: avec Live Server (VS Code)
Clic droit sur index.html → Open with Live Server

## Features du portail
- 🔍 Search bar par nom/CNE
- 📸 Photo de chaque étudiant (depuis FSDM)
- 📊 Click sur étudiant → tableau des notes complet
- ✅ Badges colorés: Validé / Rattrapage
- ⊞ Vue grille + ☰ Vue liste

## Notes importantes
- Le scraper respecte un délai de 1s entre chaque requête
- Les étudiants étrangers (USMBA...) sans CIN marocain sont ignorés
- Si photo inexistante → initiales affichées à la place
