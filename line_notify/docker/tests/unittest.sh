cd ../..
docker build -t test-image -f ./docker/tests/Dockerfile .
docker run --env-file ./docker/.env --name unittest_line_notify test-image
cd docker/tests
docker system prune -f