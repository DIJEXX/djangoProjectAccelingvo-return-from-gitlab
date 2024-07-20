git clone https://gitlab.com/DIJEXX/djangoProjectAccelingvo.git
cd djangoProjectAccelingvo
sudo docker build -t accelingvo .
sudo docker run -p 8080:8080 accelingvo