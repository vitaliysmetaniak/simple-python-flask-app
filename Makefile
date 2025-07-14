.PHONY: build run clean

build:
	docker compose build

run:
	docker compose up

clean:
	docker compose down
	docker rm -f simplepythonapp_container || true
	docker rmi simplepythonapp || true

