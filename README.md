# Бот gpt-assistant для вашего чата | TeleBot sync
Версия Python `3.11`
Автор: `@goldpulpy`

Этот ассистент для чата предназначен для улучшения взаимодействия в вашем чате в Telegram, используя возможности открытого API gpt-3.5 (ChatAnyWhere).

- Используется открытый API с gpt-3.5.
- Бот работает только в чате, который вы указали в .env
- Необходимо предоставить боту права администратора в чате

## Настройки
- Заходим в [BotFather](https://t.me/BotFather) и создаем бота
- Получить CHAT_ID можно [здесь](https://t.me/username_to_id_bot)


Файл `.env.example` переименовать в `.env`

```bash
BOT_TOKEN=your_bot_token # Токен бота
CHAT_ID=your_chat_id # ID чата | -100000000000
CHAT_HISTORY_SIZE=50 # Размер истории чата
```
Если размер истории больше 50, будут удаляться самые старые сообщения.


Файл `app/prompt.py` - Настройки промпта для роли бота

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
