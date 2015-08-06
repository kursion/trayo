#!/usr/bin/python3

import sys
import os
import time
from PyQt4 import QtGui


class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        time.sleep(1)

        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        self.menu = QtGui.QMenu(parent)

        self.current = self.menu.addAction("Current:"+self.getGovernor())
        self.current.setEnabled(False)
        self.menu.addSeparator()

        setPerf = self.menu.addAction("Set performance")
        setPerf.triggered.connect(self.setPerformance)
        setPerf = self.menu.addAction("Set powersave")
        setPerf.triggered.connect(self.setPowersave)
        self.menu.addSeparator()

        exitAction = self.menu.addAction("Exit")
        exitAction.triggered.connect(self.exit)
        self.setContextMenu(self.menu)

    def updateCurrentText(self):
        scaling = self.getGovernor()
        self.current.setText("Current: "+scaling)

    def setPerformance(self):
        self.setGovernor("performance")

    def setPowersave(self):
        self.setGovernor("powersave")

    def setGovernor(self, governor):
        os.system("sudo cpupower frequency-set -g "+governor)
        self.updateCurrentText()

    def getGovernor(self):
        f = open("/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor", "r")
        scaling = f.read()
        f.close()
        return scaling

    def exit(self):
        print(self.getGovernor())
        sys.exit()


def main():
    app = QtGui.QApplication(sys.argv)
    style = app.style()
    icon = QtGui.QIcon(style.standardPixmap(QtGui.QStyle.SP_FileIcon))
    trayIcon = SystemTrayIcon(icon)

    trayIcon.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
