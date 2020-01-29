#!/usr/bin/python3

import socket
from requests import get
import configparser
from influxdb import InfluxDBClient

basepath = '/home/vpn/cronjobs/'

ip_file = basepath + 'current_ip'
ip_file_reader = open(ip_file,'a+')
last_ip = ip_file_reader.read().strip()
ip_file_reader.close()

current_ip = get('https://api.ipify.org').text.strip()

def update_new_ip():
        ip_file_writer = open(ip_file, 'w')
        ip_file_writer.write(current_ip)
        ip_file_writer.close()
        config = configparser.ConfigParser()
        config.read(basepath + 'ip_detect.config')
        client = InfluxDBClient(config.get('DEFAULT','influx_host'), config.get('DEFAULT','influx_port'), config.get('DEFAULT','influx_user'), config.get('DEFAULT','influx_pass'), config.get('DEFAULT','influx_db'))
        data = {}
        data['measurement'] = 'ip_changes'
        data['tags'] = {}
        data['tags']['machine'] = socket.gethostname()
        data['fields'] = {}
        data['fields']['ip'] = current_ip
        print(data)
        client.write_points([data])

if current_ip != last_ip :
        print ("IP change detected")
        update_new_ip()
