# 📚 Citation API

Une API RESTful pour gérer des citations, construite avec **FastAPI**, **SQLAlchemy** et **PostgreSQL**.

---

## 🚀 Fonctionnalités

- ➕ Ajouter une citation
- 📋 Lister toutes les citations
- 🔍 Récupérer une citation par ID
- ✏️ Mettre à jour une citation
- 🗑️ Supprimer une citation

---

## 🗂️ Structure du projet

```
main.py
app/
  core/
    database.py
  db/
    models/
      citation.py
      citation_controllers.py
  util/
    init_db.py
```

---

## ⚙️ Installation

1. **Cloner le dépôt**
   ```sh
   git clone <url-du-repo>
   cd citation
   ```

2. **Créer un environnement virtuel**
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```sh
   pip install fastapi uvicorn sqlmodel sqlalchemy psycopg2
   ```

4. **Configurer la base de données**

   Modifie la variable `SQLALCHEMY_DATABASE_URL` dans [`app/core/database.py`](app/core/database.py) selon tes paramètres PostgreSQL.

5. **Lancer l’application**
   ```sh
   uvicorn main:app --reload
   ```

---

## 🛠️ Utilisation

- Accède à la documentation interactive : [http://localhost:8000/docs](http://localhost:8000/docs)
- **Endpoints principaux :**
  - `POST /citation/` : Ajouter une citation
  - `GET /citation/` : Lister toutes les citations
  - `GET /citation/{citation_id}` : Obtenir une citation spécifique
  - `PUT /citation/{citation_id}` : Modifier une citation
  - `DELETE /citation/{citation_id}` : Supprimer une citation

---

## 👤 Auteur

- kpara gedeon

---

## 📄 Licence

Ce projet est