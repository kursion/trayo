SOURCE=`dirname ${BASH_SOURCE[0]}`
SERVICE_NAME="trayo"
SCRIPT_NAME="trayo.py"
NULL="/dev/null"

echo "ADDING ${SERVICE_NAME} SERVICE"
# sudo cp -f $SOURCE/$SERVICE_NAME.service /usr/lib/systemd/system/ 2> $NULL
sudo cp -f $SOURCE/$SCRIPT_NAME /bin/$SERVICE_NAME
sudo chmod +x /bin/$SERVICE_NAME
echo "ADD cpupower to visudo no password"
echo "eg: kursion ALL=NOPASSWD: /bin/cpupower"
# sudo systemctl daemon-reload
# sudo systemctl start $SERVICE_NAME.service
# sudo systemctl enable $SERVICE_NAME.service
