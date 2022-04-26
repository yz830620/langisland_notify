cd ..
docker build -t service-line-notify --file ./docker/Dockerfile .
docker system prune -f
cd docker