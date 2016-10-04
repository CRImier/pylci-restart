cp pylci-restart.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable pylci-restart.service
systemctl start pylci-restart.service

