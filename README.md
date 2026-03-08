# Сеть продажи электроники

REST API для управления иерархической сетью поставок электроники: заводы → оптовые → розничные сети.

Реализовано с использованием:
- Django + Django REST Framework
- Docker + PostgreSQL + Nginx
- Админка с action "Очистить задолженность"
- Фильтрация по стране, городу
- Swagger UI документация

---

## 🛠 Технологии

- **Django** — бэкенд и ORM
- **DRF** — REST API
- **PostgreSQL** — база данных
- **Docker & Docker Compose** — контейнеризация
- **Nginx** — раздача статики и проксирование
- **drf-spectacular** — автоматическая документация

---

## 🚀 Запуск проекта

### 1. Клонируйте репозиторий
bash git clone https://github.com/ваш-репозиторий/electronics-sales-network.git cd electronics-sales-network


### 2. Создайте `.env` файл
bash cp .env.example .env

Или создайте вручную:
DEBUG=1 SECRET_KEY=your-secret-key-here 
DB_NAME=electronics_network DB_USER=myuser 
DB_PASSWORD=mypass123 
DB_HOST=db DB_PORT=5432
DJANGO_SUPERUSER_USERNAME=admin 
DJANGO_SUPERUSER_EMAIL=admin@example.com 
DJANGO_SUPERUSER_PASSWORD=admin


> ⚠️ Не коммитьте `.env` в Git!

### 3. Запустите через Docker
bash docker-compose build --no-cache docker-compose up

---

## 🔗 Доступные адреса

| Сервис           | Адрес                                                                      |
|------------------|----------------------------------------------------------------------------|
| Админка          | [http://127.0.0.1/admin](http://127.0.0.1/admin)                           |
| API (Browsable)  | [http://127.0.0.1:8000/api/networks/](http://127.0.0.1:8000/api/networks/) |
| Swagger UI       | [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)         |

> Логин: `admin`, пароль: `admin` (из `.env`)

---

## 📦 Структура проекта
electronics-network/ 
├── network/ # Приложение 
├── core/ # Настройки Django 
├── staticfiles/ # Собранная статика (авто) 
├── mediafiles/ # Медиа (авто) 
├── nginx/ # Конфиг Nginx 
├── .env # Переменные окружения 
├── .gitignore 
├── README.md 
├── requirements.txt 
├── docker-compose.yml 
└── Dockerfile


---

## 🧪 Особенности

- **Только активные сотрудники** могут использовать API (`is_staff=True`)
- **Задолженность нельзя изменить через API**
- **Уровень определяется автоматически**
- В админке: **action "Очистить задолженность"**

---

## 📄 Автор
@MariyaM1982 — 2026

