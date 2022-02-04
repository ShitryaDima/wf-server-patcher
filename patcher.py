# Copyright © 2022 Шитря Дмитрий

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from PySide2 import QtWidgets
from design import Ui_Form
from pythonping import ping
from functools import partial
import math
import os


hosts = [
    "global.ping.warface.ru",
"novosibirsk.ping.warface.ru",
"krasnodar.ping.warface.ru", 
"khabarovsk.ping.warface.ru"
]

class Patcher(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.__version__ = 1.0
        self.setupUi(self)
        self.msk_button.clicked.connect(partial(self.server_button_pushed, 0))
        self.novosibirsk_button.clicked.connect(partial(self.server_button_pushed, 1))
        self.krasnodar_button.clicked.connect(partial(self.server_button_pushed, 2))
        self.habarovsk_button.clicked.connect(partial(self.server_button_pushed, 3))
        self.setFixedSize(self.size())
        self.show()

        self.server_data = [
            {'name' : "Москва", 'ping' : 0, 'patched' : False},
            {'name' : "Новосибирск", 'ping' : 0, 'patched' : False},
            {'name' : "Краснодар", 'ping' : 0, 'patched' : False},
            {'name' : "Хабаровск", 'ping' : 0, 'patched' : False}
        ]
        self.set_ping()
        self.set_patch_status()
        self.update_button()

    def update_ping(self):
        self.server_data[0]['ping'] = ping(target=hosts[0], count=1, timeout=2).rtt_avg_ms
        self.server_data[1]['ping'] = ping(target=hosts[1], count=1, timeout=2).rtt_avg_ms
        self.server_data[2]['ping'] = ping(target=hosts[2], count=1, timeout=2).rtt_avg_ms
        self.server_data[3]['ping'] = ping(target=hosts[3], count=1, timeout=2).rtt_avg_ms
        return

    def set_ping(self, need_update = True):
        self.update_ping() if need_update else None
        self.label_mskping.setText(str(math.ceil(self.server_data[0]['ping'])) + ' мс')
        self.label_novosibping.setText(str(math.ceil(self.server_data[1]['ping'])) + ' мс')
        self.label_krasnodarping.setText(str(math.ceil(self.server_data[2]['ping'])) + ' мс')
        self.label_habarovskping.setText(str(math.ceil(self.server_data[3]['ping'])) + ' мс')
        
    def set_patch_status(self, need_update = True):
        self.update_patch_status() if need_update else None
        self.label_mskpatchstatus.setText(str("Сервер добавлен" if self.server_data[0]['patched'] else "Сервер не добавлен"))
        self.label_novosibpatchstatus.setText(str("Сервер добавлен" if self.server_data[1]['patched'] else "Сервер не добавлен"))
        self.label_krasnodarpatchstatus.setText(str("Сервер добавлен" if self.server_data[2]['patched'] else "Сервер не добавлен"))
        self.label_habarovskpatchstatus.setText(str("Сервер добавлен" if self.server_data[3]['patched'] else "Сервер не добавлен"))

    def update_patch_status(self):
        self.update_ping()
        for server in self.server_data:
            if server['ping'] < 1:
                server['patched'] = True
            else:
                server['patched'] = False
        return

    def update_button(self):
        self.msk_button.setText(str("Удалить" if self.server_data[0]['patched'] else "Добавить"))
        self.novosibirsk_button.setText(str("Удалить" if self.server_data[1]['patched'] else "Добавить"))
        self.krasnodar_button.setText(str("Удалить" if self.server_data[2]['patched'] else "Добавить"))
        self.habarovsk_button.setText(str("Удалить" if self.server_data[3]['patched'] else "Добавить"))

    def patch_server(self, server):
        def add(file, number_server):
            f.write(f"\n127.0.0.1 {hosts[number_server]}")
            return

        if os.path.exists(fr"{os.getenv('WINDIR')}\System32\drivers\etc\hosts"):
            try:
                f = open(fr"{os.getenv('WINDIR')}\System32\drivers\etc\hosts", "a+")
                add(f, server)
                f.close()

            except PermissionError:
                QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)
        else:
            try:
                f = open(fr"{os.getenv('WINDIR')}\System32\drivers\etc\hosts", "w")
                add(f, server)
                f.close()
            except PermissionError:
                QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)
        
        self.set_ping()
        self.set_patch_status()
        self.update_button()

    def unpatch_server(self, server):
        try:
            f = open(fr"{os.getenv('WINDIR')}\System32\drivers\etc\hosts", "r+")
            texts = f.read()
            f.seek(0)
            texts = texts.replace(f'\n127.0.0.1 {hosts[server]}', '')
            f.write(texts)
            f.truncate()
            f.close()
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)
        
        self.set_ping()
        self.set_patch_status()
        self.update_button()

    def server_button_pushed(self, server_number):
        if self.server_data[server_number]['patched']:
            self.unpatch_server(server_number)
        else:
            self.patch_server(server_number)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    pathcer = Patcher()
    sys.exit(app.exec_())