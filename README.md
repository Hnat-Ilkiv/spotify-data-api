# Spotify Data API – Lab 2

## Опис
Проєкт для генерації тестових даних, збереження їх у базу даних та роботи з предметною областю Spotify.

## Стек технологій
- Python 3
- SQLAlchemy (ORM)
- SQLite (база даних)
- pytest (тестування)

## Архітектура
- **Data Access Layer (DAL)** – доступ до бази даних через інтерфейси.
- **Business Logic Layer (BLL)** – логіка роботи з CSV і базою.
- **Presentation Layer (CLI)** – взаємодія через командний рядок.

## Запуск проєкту
```bash
nix-shell
python src/main.py gen_csv

