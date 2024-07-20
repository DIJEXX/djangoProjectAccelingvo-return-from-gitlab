git clone https://gitlab.com/DIJEXX/djangoProjectAccelingvo.git
cd djangoProjectAccelingvo
docker build -t accelingvo .
docker run -p 8080:8080 accelingvo