
TP-Final-Name-******
Presentacion de Producto ✅

Fase 0: Preparar el entorno

- [ ] Crear subcarpeta /api en el repo o repo nuevo.
- [ ] Crear entorno virtual:

python'''python -m venv .venv'''
bash'''source .venv/bin/activate   # Windows: .venv\Scripts\activate'''


 Instalar dependencias:

'''pip install Flask Flask-SQLAlchemy Flask-RESTful python-dotenv'''

- [ ] Crear archivo .env para variables sensibles (DB URL, API keys).

Fase 1: Modelos de datos

- [ ] Crear archivo models.py.

 Definir tablas:

- [ ]Shop (carnicería, token, premium/free, ubicación, contacto).

- [ ]Cut (nombre, alias).

- [ ]Price (shop_id, cut_id, precio, stock, fecha).

- [ ]Offer (promociones, vigencia).

Optional: User (clientes y carnicerías) para login/autenticación.

- [ ] Configurar SQLAlchemy y crear la DB (sqlite para MVP).

Fase 2: Endpoints básicos

- [ ] /cuts → listar cortes disponibles.

- [ ] /shops → listar carnicerías, info básica, ubicación.

- [ ] /shops/<id> → detalle de carnicería (productos, promociones, horarios, contacto).

- [ ] /shops/<id>/prices → POST para agregar precio (solo carnicería con token).

- [ ] /prices → GET precios filtrados por corte, ubicación, rango de distancia.

- [ ] /offers → GET promociones activas.

- [ ] /suggestion → unir clima + precios → “¿me conviene hacer asado?” (dummy al inicio).

Fase 3: Autenticación y seguridad

- [ ] Generar tokens para carnicerías (API keys).

- [ ] Middleware para validar token en endpoints de modificación (POST/PUT/DELETE).

- [ ] Limitar consultas por tipo de licencia (freemium / premium).

Fase 4: Integración con clima

- [ ] Crear endpoint /weather?location=LAT,LON&date=YYYY-MM-DD

- [ ] Integrar con OpenWeatherMap (o mock para MVP).

- [ ] Retornar pronóstico simple: lluvia, temperatura, viento, iconos.

Fase 5: Testing y documentación

- [ ] Crear tests básicos (pytest o unittest) para endpoints.

- [ ] Documentar endpoints en README.md y usar Swagger o Postman para pruebas.

Fase 6: Deploy

- [ ] Preparar requirements.txt.

- [ ] Configurar WSGI (Flask) o ASGI si usás FastAPI en otra versión.

 Desplegar en Vercel, Railway, Render o Heroku (para MVP rápido).

 Probar endpoints con frontend conectado (mapa, perfil carnicerías, clima).
