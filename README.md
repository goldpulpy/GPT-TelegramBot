<p align="center">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/goldpulpy/GPT-TelegramBot">
    <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/goldpulpy/GPT-TelegramBot/python-app.yml">

</p>

<h1 align="center"> Бот gpt-assistant для вашего чата </h1>

- Версия Python `3.11`
- Автор: `@goldpulpy`

Этот ассистент для чата предназначен для улучшения взаимодействия в вашем чате в Telegram, используя возможности открытого API GPT (ChatAnyWhere).

- Используется открытый API с GPT
- Бот работает только в чате, который вы указали в .env
- Необходимо предоставить боту права администратора в чате

## Настройки

- Заходим в [BotFather](https://t.me/BotFather) и создаем бота
- Получить CHAT_ID можно [здесь](https://t.me/username_to_id_bot)

Файл `.env.example` переименовать в `.env`

```bash
BOT_TOKEN=your_bot_token # Токен бота
CHAT_ID=your_chat_id # ID чата | -....
CHAT_HISTORY_SIZE=50 # Размер истории чата
```

Если размер истории больше 50, будут удаляться самые старые сообщения.

## Настройка промпта

Поведение бота можно настроить, изменив подсказку, которую он использует для генерации ответов.

## Шаги по настройке подсказки

Создайте файл `prompt.txt` и напишите туда свой промпт.

Например:

```
Ты - полезный помощник, твое имя Jarvis
```

## Запуск docker

```bash
docker build -t assistantbot . # Собираем Docker образ
docker run -d --name assistantbot assistantbot # Запускаем Docker
# или
docker-compose up -d # Запускаем Docker-compose
```

## Обычный запуск (venv)

```bash
python -m venv .venv
source .venv/bin/activate

# Если без виртуального окружения, начинаем с pip
pip install -r requirements.txt
python main.py
```

## Тесты (Если есть необходимость)

После заполнения `.env`, можно запустить тесты:

```bash
pip install pytest
pytest
```
