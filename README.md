# ip_changes_detector
A simple python3 script that detects public IP changes and logs this to InfluxDB.
I built this not to spam duckdns.org with generated subdomains for cases when I need to know IP addresses (say to update Amazon EC2 firewall to let certaint traffic through) 

## Config
There are two/three changes you have to consider:
1. Give your machine a hostname that rings a bell (you wouldn't  want them all in InfluxDB with same standard hostname, right?)
2. Update ```ip_detect.config``` with your InfluxDB params
3. Update ```ip_detect.py``` with correct basepath (i.e. from where the script runs)

## Running
Just set it up via cron:
```*/30 * * * * python3 ~/cronjobs/ip_detect.py&```

## Just in case - how to set up new InfluxDB database and/or user
```
CREATE USER "iot_user" WITH PASSWORD 'iot56'
CREATE DATABASE "iot_db"
GRANT WRITE ON "iot_db" TO "iot_user"
```

