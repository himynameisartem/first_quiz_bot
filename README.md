# First Quiz Bot / Бот «Первая Викторина»

---

EN — English
=============

Table of Contents
-----------------
- [Overview](#overview)
- [Features](#features)
- [Commands & Keyboards](#commands--keyboards)
- [Installation (macOS)](#installation-macos)
- [Configuration](#configuration)
- [Run](#run)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [How to test (for the reviewer)](#how-to-test-for-the-reviewer)
- [Troubleshooting](#troubleshooting)
- [Recommendations & Improvements](#recommendations--improvements)
- [Privacy & License](#privacy--license)
- [Contact / Bot username](#contact--bot-username)

Overview
--------
Simple Telegram quiz bot built with aiogram and aiosqlite. Presents multiple-choice questions, saves the user's last result and basic statistics (number of games, best score). Reply keyboard allows starting, restarting and viewing stats.

Features
--------
- Start quiz and answer multiple-choice questions.
- Save last result, total games and best score.
- Reply keyboard with:
  - "Start game" / "Start over" / "Try again"
  - "View statistics"
- Ability to interrupt and restart the quiz at any time.

Commands & Keyboards
--------------------
- /start — initialize DB if needed and show start keyboard
- /quiz — start the quiz
- /stats — show user statistics

Installation (macOS)
--------------------
1. Clone the repository from GitHub (replace <REPO_URL> with your repo link):
   ```bash
   git clone <REPO_URL>
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

Project Structure
-----------------
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

Contact / Bot username
----------------------
Replace with real bot username so your reviewer can find it:
- Bot username: @YourBotUsername

---

RU — Русская версия
===================

Оглавление
---------
- [Описание](#описание)
- [Функционал](#функционал)
- [Команды и клавиатуры](#команды-и-клавиатуры)
- [Установка (macOS)](#установка-macos)
- [Конфигурация](#конфигурация)
- [Запуск](#запуск)
- [Схема БД](#схема-бд)
- [Структура проекта](#структура-проекта)
- [Как проверить (для проверяющего)](#как-проверить-для-проверяющего)
- [Устранение проблем](#устранение-проблем)
- [Рекомендации по улучшению](#рекомендации-по-улучшению)
- [Приватность и лицензия](#приватность-и-лицензия)
- [Контакт / Имя бота](#контакт--имя-бота)

Описание
--------
Простейший Telegram-бот для викторин на aiogram + aiosqlite. Задаёт вопросы с вариантами, сохраняет последний результат пользователя и базовую статистику (число игр, лучший результат). Reply-клавиатура позволяет запускать, перезапускать игру и смотреть статистику.

Функционал
---------
- Прохождение квиза с вариантами ответов.
- Сохранение результатов.
- ReplyKeyboard:
  - "Начать игру" / "Начать заново" / "Попробовать ещё раз"
  - "Посмотреть статистику"
- Возможность прервать и перезапустить квиз.

Команды
-------------------
- /start — инициализация (создание таблицы БД) и показ стартовой клавиатуры
- /quiz — запустить квиз
- /stats — показать статистику

Установка (macOS)
-----------------
1. Клонируйте репозиторий с GitHub (замените <REPO_URL> на ссылку вашего репо):
   ```bash
   git clone <REPO_URL>
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

Структура проекта
----------------
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

Контакт / Имя бота
-----------------
Замените на реальное имя бота, чтобы проверяющий мог найти:
- Имя бота: @YourBotUsername

