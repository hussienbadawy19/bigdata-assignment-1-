
#!/bin/bash

CONTAINER_NAME=customer_container


mkdir -p results


docker cp $CONTAINER_NAME:/app/pipeline/*.csv ./results/
docker cp $CONTAINER_NAME:/app/pipeline/*.txt ./results/
docker cp $CONTAINER_NAME:/app/pipeline/*.png ./results/


docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

echo ""
echo "Pipeline finished successfully."