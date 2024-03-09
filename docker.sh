$service_name = "geminibot"

docker rm -f $service_name && docker rmi -f $service_name
docker build -t $service_name .
docker run -d --name $service_name $service_name
