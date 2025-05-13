# Flask SQLi Demo - Mini site vulnérable à l'injection SQL

Ce projet est une mini application Flask volontairement vulnérable aux injections SQL.
Il permet de s'entraîner à exploiter des failles dans un contexte réaliste de formulaire de login.

---

## Installation

### 1.Cloner le repo
```bash
git clone https://github.com/AndyDCK/Simple-SQL-Injection.git
cd Simple-SQL-Injection
```
### 2.Installer les dépendances
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Lancer l'application
```bash
python app.py
```
L'application sera disponible sur http://127.0.0.1:5000
