#tag=`git rev-parse --abbrev-ref HEAD`
tag=latest
USER=tobit6795
IMAGE=deye-solarflow-bridge
docker build -t ${USER}/${IMAGE}:$tag .

docker image push ${USER}/${IMAGE}:$tag
