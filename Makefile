build:
	docker build -t postnote .

run:
	docker run -d --name pn -p 8081:80 postnote

clean:
	docker stop pn
	docker rm pn