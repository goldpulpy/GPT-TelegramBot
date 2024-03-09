$service_name = "telegrambot"

docker rm -f $service_name && docker rmi -f $service_name
docker build -t $service_name .
docker run -d --name $service_name \
           -v ./chat_history.json:/app/chat_history.json \
           $service_name
