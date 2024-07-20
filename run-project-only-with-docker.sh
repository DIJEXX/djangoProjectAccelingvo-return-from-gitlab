git clone https://gitlab.com/DIJEXX/djangoProjectAccelingvo.git
cd djangoProjectAccelingvo
sudo docker build -t accelingvo .
sudo docker run -p 8150:8150 accelingvo