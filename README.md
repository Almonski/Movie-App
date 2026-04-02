Movie Collection - Fullstack CRUD App
En webbapplikation för att hantera en filmsamling, byggd med FastAPI på backenden och React på frontenden. Projektet demonstrerar ett komplett dataflöde från UI till en SQLite-databas via ett REST API.

Teknikstack
Backend: Python 3.10+, FastAPI, SQLAlchemy (ORM), Pydantic (Validering).

Frontend: React, Axios för API-anrop.

Databas: SQLite (lokal fil: movies.db).

Struktur
Projektet följer en modulär struktur för att separera ansvar:

models.py - Definierar databastabeller (SQLAlchemy).

schemas.py - Pydantic-modeller för datavalidering och JSON-struktur.

database.py - Konfiguration av databasanslutning och sessioner.

App.jsx - Hanterar state, API-anrop (Async/Await) och rendering.

Installation & Uppstart
1. Backend (FastAPI)
Gå till backend-mappen och skapa en virtuell miljö:

Bash
python -m venv .venv
source .venv/bin/scripts/activate  # Windows: .venv\Scripts\activate
pip install fastapi uvicorn sqlalchemy
Starta servern:

Bash
uvicorn main:app --reload
Backenden körs nu på http://127.0.0.1:8000. Dokumentation hittas på /docs.

2. Frontend (React)
Gå till frontend-mappen och installera beroenden:

Bash
npm install
npm install axios
Starta utvecklingsservern:

Bash
npm run dev
Frontenden körs vanligtvis på http://localhost:5173.

API Endpoints
Applikationen implementerar följande CRUD-flöde:

GET /movies - Hämtar alla filmer.

POST /movies - Skapar en ny film (valideras via Pydantic).

PUT /movies/{id} - Uppdaterar titel/regissör för en specifik film.

DELETE /movies/{id} - Raderar en film baserat på ID.

Arkitektur & Logik
CORS: Backend är konfigurerad med CORSMiddleware för att tillåta anrop från React-klienten.

Async/Await: Alla API-anrop i frontend hanteras asynkront för att förhindra att UI:t låser sig vid väntetid.

State Management: Använder React useState och useEffect för att synkronisera UI:t med databasens innehåll efter varje ändring.