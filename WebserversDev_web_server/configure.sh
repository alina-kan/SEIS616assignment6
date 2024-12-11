#!/bin/sh
# Use this to install software packages
# This script is for EC2 userdata. All commands are executed as administrators. 
yum update -y
yum install -y git httpd php
service httpd start
chkconfig httpd on
aws s3 cp s3://seis665-public/index.php /var/www/html/