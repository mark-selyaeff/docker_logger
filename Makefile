build:
	docker volume create logger_vol
	docker build . -t logger

start:
	-docker run --detach -p 65432:65432 -v logger_vol:/var/log --name logger_container logger

stop:
	-docker stop logger_container

clean:
	-docker container rm logger_container
	-docker image rm logger
	-docker volume rm logger_vol
