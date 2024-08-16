#!/bin/bash

# Ambil argumen pertama sebagai mode (dev atau prod)
mode=$1

# Fungsi untuk menjalankan perintah collectstatic dan menyimpan file statik
function run_collectstatic {
    echo "Running collectstatic..."
    sudo rm -rf /home/sekawansystema/project/pos/staticfiles
    echo "yes" | /home/sekawansystema/project/pos/penv/bin/python3 /home/sekawansystema/project/pos/manage.py collectstatic
    sudo rm -rf /var/www/pos/static/*
    sudo cp -r /home/sekawansystema/project/pos/staticfiles/* /var/www/pos/static
}

# Fungsi untuk menghentikan dan memulai ulang service menggunakan systemctl
function restart_service {
    sudo systemctl stop pos.service
    sudo systemctl start pos.service
}

# Fungsi untuk menjalankan server Django dengan mode dev
function run_server_dev {
    port=7001
    sudo systemctl stop pos.service
    echo "Running Django server in dev mode on port $port..."
    /home/sekawansystema/project/pos/penv/bin/python3 /home/sekawansystema/project/pos/manage.py runserver 0.0.0.0:$port
}

# Fungsi untuk menjalankan server menggunakan Gunicorn
function run_gunicorn {
    echo "Running Gunicorn server in prod mode..."
    # Ganti dengan konfigurasi Gunicorn Anda
    # Contoh: /path/to/venv/bin/gunicorn my_project.wsgi:application --bind 0.0.0.0:8000 --workers 3
}

# Main script logic
if [ "$mode" == "dev" ]; then
    run_collectstatic
    clear
    run_server_dev
elif [ "$mode" == "prod" ]; then
    run_collectstatic
    restart_service
else
    echo "Usage: $0 {dev|prod}"
    exit 1
fi

