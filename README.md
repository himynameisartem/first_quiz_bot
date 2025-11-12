# Quiz Bot / Telegram bot «Викторина»

---

Table of Contents
-----------------
- [English Version](#english-version)
  - [Overview](#overview)
  - [Features](#features)
  - [Commands & Keyboards](#commands--keyboards)
  - [Installation](#installation)
  - [Project Structure](#project-structure)
  - [Contact / Bot username](#contact--bot-username)
  - [Author](#author)
- [Русская версия](#русская-версия)
  - [Описание](#описание)
  - [Функционал](#функционал)
  - [Команды](#команды)
  - [Установка](#установка)
  - [Структура проекта](#структура-проекта)
  - [Контакт / Имя бота](#контакт--имя-бота)
  - [Автор](#автор)

## English Version

### Overview
Simple Telegram quiz bot built with aiogram and aiosqlite. Presents multiple-choice questions, saves the user's last result and basic statistics (number of games, best score). Reply keyboard allows starting, restarting and viewing stats.

### Features
- Start quiz and answer multiple-choice questions.
- Save last result, total games and best score.
- Reply keyboard with:
  - "Start game" / "Start over" / "Try again"
  - "View statistics"
- Ability to interrupt and restart the quiz at any time.

### Commands & Keyboards
- /start — initialize DB if needed and show start keyboard
- /quiz — start the quiz
- /stats — show user statistics

### Installation
1. Clone the repository from GitHub (replace <REPO_URL> with your repo link):
   ```bash
   git clone https://github.com/himynameisartem/first_quiz_bot.git
   cd first_quiz_bot
   ```

2. Create and activate virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If no requirements file:
   ```bash
   pip install aiogram aiosqlite
   ```

### Project Structure
- main.py — app entry, handlers registration
- handlers/
  - quiz.py — quiz flow (start, send questions)
  - callbacks.py — answer processing and result saving
  - stats.py — stats command
  - start.py — /start command
- database/
  - db_handler.py — DB operations (aiosqlite)
- keyboards/
  - builders.py — Reply/Inline keyboards
- data/
  - quiz_data.py — questions and options
- config.py — token and DB name (local)
- README.md — this file

### Contact / Bot username
Replace with real bot username so your reviewer can find it:
- Bot username: @firstStudyQuizBot

### Author

**Artem Kudryavtsev**
This project demonstrates practical skills in the following areas:

- Developing Telegram bots using aiogram
- Asynchronous programming in Python (async/await, state management)
- Working with local databases (aiosqlite, schemas, user statistics storage)
- UX design for chat interfaces (Inline/Reply keyboards, callback handling)
- User state and session management (question indexes, progress reset)
- Basic user analytics (saving last results, best/total metrics)

---

## Русская версия

### Описание
Простейший Telegram-бот для викторин на aiogram + aiosqlite. Задаёт вопросы с вариантами, сохраняет последний результат пользователя и базовую статистику (число игр, лучший результат). Reply-клавиатура позволяет запускать, перезапускать игру и смотреть статистику.

### Функционал
- Прохождение квиза с вариантами ответов.
- Сохранение результатов.
- ReplyKeyboard:
  - "Начать игру" / "Начать заново" / "Попробовать ещё раз"
  - "Посмотреть статистику"
- Возможность прервать и перезапустить квиз.

### Команды
- /start — инициализация (создание таблицы БД) и показ стартовой клавиатуры
- /quiz — запустить квиз
- /stats — показать статистику

### Установка
1. Клонируйте репозиторий с GitHub (замените <REPO_URL> на ссылку вашего репо):
   ```bash
   git clone https://github.com/himynameisartem/first_quiz_bot.git
   cd first_quiz_bot
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   Если requirements.txt нет:
   ```bash
   pip install aiogram aiosqlite
   ```

### Структура проекта
- main.py — вход в приложение, регистрация хендлеров
- handlers/
  - quiz.py — логика квиза
  - callbacks.py — обработка ответов, сохранение результатов
  - stats.py — команда статистики
  - start.py — /start команда
- database/
  - db_handler.py — операции с БД
- keyboards/
  - builders.py — клавиатуры
- data/
  - quiz_data.py — вопросы и варианты
- config.py — токен и имя БД (локально)
- README.md — этот файл

### Контакт / Имя бота
Замените на реальное имя бота, чтобы проверяющий мог найти:
- Имя бота: @firstStudyQuizBot

### Автор

**Артем Кудрявцев**
Этот проект демонстрирует практические навыки в следующих областях:

- Разработка Telegram‑ботов на aiogram
- Асинхронное программирование в Python (async/await, управление состоянием)
- Работа с локальной БД (aiosqlite, схемы, сохранение статистики пользователей)
- Дизайн UX для чат‑интерфейсов (Inline / Reply клавиатуры, обработка колбэков)
- Управление состоянием и сессиями пользователей (индексы вопросов, сброс прогресса)
- Простая аналитика пользователя (сохранение последнего результата, best/total)
