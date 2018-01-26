#!/usr/bin/env bash
# Setup luma.led_matrix requirements

if ! lsmod | egrep -iq spi; then
	echo "SPI driver not loaded, must run 'sudo raspi-config' and enable SPI under Interfacing Options!"
	exit 1
fi

sudo usermod -a -G spi,gpio pi
sudo apt-get install build-essential python-dev python-pip libfreetype6-dev libjpeg-dev -y
sudo -i pip install --upgrade pip setuptools
sudo apt-get purge python-pip -y

sudo -H pip install --upgrade luma.led_matrix

echo "Installed luma.led_matrix requirements"
