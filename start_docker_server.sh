#build
#docker build -t osc-party-app .

#run
#docker run -it --rm -p 8090:80 -p 12345:12345 osc-party-app

#dev
#docker run -it --rm -p 8090:80 -p 12345:12345 -v $PWD/src:/var/www/html  --entrypoint /bin/bash osc-party-app
docker run -it --rm -p 8090:80 -p 4330:4330 -v $PWD/src:/var/www/html  --entrypoint /bin/bash osc-party-app
