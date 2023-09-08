#tag=`git rev-parse --abbrev-ref HEAD`
tag=latest
USER=tobit6795
IMAGE=deye-solarflow-bridge

docker stop ${IMAGE} || echo cannot stop, ${IMAGE} does not exist
docker rm ${IMAGE} || echo Cannot delete, ${IMAGE} does not exist
docker build -t ${USER}/${IMAGE}:$tag .
docker image push ${USER}/${IMAGE}:$tag
docker run -d --restart=always --env-file .env --name deye-solarflow-bridge tobit6795/deye-solarflow-bridge:latest
