# Бот gemini для вашего чата на TeleBot
Версия Python `3.11`
Автор: `@goldpulpy`

- Используется открытый API NextChat с gemini-pro 
- Бот работает только в чате который вы указали в `.env`
- Боту нужно выдать админку в чате

## Настройки
- Заходим в [BotFather](https://t.me/BotFather) и создаем бота
- Получить CHAT_ID можно [здесь](https://t.me/username_to_id_bot)


Файл `.env.example` переименовать в `.env`

```bash
BOT_TOKEN=your_bot_token # Токен бота
CHAT_ID=your_chat_id # ID чата | -100000000000
CHAT_HISTORY_SIZE=50 # Размер истории чата
```
Если размер истории больше 50, то будут удаляться самые старые сообщения из истории


Файл `app/prompt.py` - Настройки промпта для роли бота

## Запуск docker
```bash
docker build -t geminibot . # собираем docker образ
docker run -d --name geminibot geminibot # запускаем docker
# или
docker-compose up -d # запускаем docker-compose

```

## Обычный запуск (venv)
```bash
python -m venv .venv
source .venv/bin/activate

# если без виртуального окружения, начинаем с pip
pip install -r requirements.txt
python main.py
```
