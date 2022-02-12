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

import re
from sys import exit, argv
from PySide2 import QtWidgets
from design import Ui_Form
from pythonping import ping
from functools import partial
from math import ceil
from os import getenv, path

class Patcher(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.__version__ = 1.1
        self.setupUi(self)

        self.server_data = {
            "Moscow": {'title': "Moscow", 'ip': "global.ping.warface.ru", 'ping': 0, 'patched': False, 'ping_label': self.label_msk_ping, 'patch_label': self.label_msk_patchstatus, 'button': self.msk_button},
            "Novosibirsk": {'title': "Novosibirsk", 'ip': "novosibirsk.ping.warface.ru", 'ping': 0, 'patched': False, 'ping_label': self.label_novosib_ping, 'patch_label': self.label_novosib_patchstatus, 'button': self.novosibirsk_button},
            "Krasnodar": {'title': "Krasnodar", 'ip': "krasnodar.ping.warface.ru", 'ping': 0, 'patched': False, 'ping_label': self.label_krasnodar_ping, 'patch_label': self.label_krasnodar_patchstatus, 'button': self.krasnodar_button},
            "Khabarovsk": {'title': "Khabarovsk", 'ip': "khabarovsk.ping.warface.ru", 'ping': 0, 'patched': False, 'ping_label': self.label_khabarovsk_ping, 'patch_label': self.label_khabarovsk_patchstatus, 'button': self.khabarovsk_button},
            "Amsterdam": {'title': "Amsterdam", 'ip': "ams.ping.wf.my.com", 'ping': 0, 'patched': False, 'ping_label': self.label_amsterdam_ping, 'patch_label': self.label_amsterdam_patchstatus, 'button': self.ams_button},
            "Hong-Kong": {'title': "Hong-Kong", 'ip': "hongkong.ping.wf.my.com", 'ping': 0, 'patched': False, 'ping_label': self.label_hongkong_ping, 'patch_label': self.label_hongkong_patchstatus, 'button': self.hongkong_button},
            "Washington": {'title': "Washington", 'ip': "wa.ping.wf.my.com", 'ping': 0, 'patched': False, 'ping_label': self.label_wa_ping, 'patch_label': self.label_wa_patchstatus, 'button': self.wa_button},
            "Sao-Paulo": {'title': "Sao-Paulo", 'ip': "saopaulo.ping.wf.my.com", 'ping': 0, 'patched': False, 'ping_label': self.label_saopaulo_ping, 'patch_label': self.label_saopaulo_patchstatus, 'button': self.saopaulo_button},
            "Istanbul": {'title': "Istanbul", 'ip': "istanbul.ping.wf.my.com", 'ping': 0, 'patched': False, 'ping_label': self.label_istanbul_ping, 'patch_label': self.label_istanbul_patchstatus, 'button': self.istanbul_button}
        }

        for server in self.server_data.values():
            server['button'].clicked.connect(partial(self.server_button_pushed, server))

        self.setFixedSize(self.size())
        self.show()

        self.set_ping()
        self.set_patch_status()
        self.update_button()

    def update_ping(self, server = None):
        if server:
            server['ping'] = ping(target=server['ip'], count=1, timeout=2).rtt_avg_ms
            return
        for server in self.server_data.values():
            server['ping'] = ping(target=server['ip'], count=1, timeout=2).rtt_avg_ms
        return

    def set_ping(self, server = None, need_update = True):
        if server:
            self.update_ping(server) if need_update else None
            server['ping_label'].setText(str(ceil(server['ping'])) + ' мс')
            return
        self.update_ping() if need_update else None
        for server in self.server_data.values():
            server['ping_label'].setText(str(ceil(server['ping'])) + ' мс')
        return
        
    def set_patch_status(self, server = None, need_update = True):
        if server:
            self.update_patch_status(server) if need_update else None
            server['patch_label'].setText(str("Сервер добавлен" if server['patched'] else "Сервер не добавлен"))
            return
        self.update_patch_status() if need_update else None
        for server in self.server_data.values():
            server['patch_label'].setText(str("Сервер добавлен" if server['patched'] else "Сервер не добавлен"))
        return

    def update_patch_status(self, server = None):
        if server:
            self.update_ping(server)
            server['patched'] = True if server['ping'] < 1 else False
            return
        self.update_ping()
        for server in self.server_data.values():
            if server['ping'] < 1:
                server['patched'] = True
            else:
                server['patched'] = False
        return

    def update_button(self, server = None):
        if server:
            server['button'].setText(str("Удалить" if server['patched'] else "Добавить"))
            return
        for server in self.server_data.values():
            server['button'].setText(str("Удалить" if server['patched'] else "Добавить"))
        return

    def patch_server(self, server):
        def add(f, server):
            f.write(f"\n127.0.0.1 {server['ip']}")
            return

        if path.exists(fr"{getenv('WINDIR')}\System32\drivers\etc\hosts"):
            try:
                f = open(fr"{getenv('WINDIR')}\System32\drivers\etc\hosts", "a+")
                add(f, server)
                f.close()

            except PermissionError:
                QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)
        else:
            try:
                f = open(fr"{getenv('WINDIR')}\System32\drivers\etc\hosts", "w")
                add(f, server)
                f.close()
            except PermissionError:
                QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

            except Exception:
                QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)
        
        self.set_ping(server)
        self.set_patch_status(server)
        self.update_button(server)

    def unpatch_server(self, server):
        try:
            f = open(fr"{getenv('WINDIR')}\System32\drivers\etc\hosts", "r+")
            texts = f.read()
            f.seek(0)
            texts = texts.replace(f"\n127.0.0.1 {server['ip']}", '')
            f.write(texts)
            f.truncate()
            f.close()
        except PermissionError:
            QtWidgets.QMessageBox.critical(self, "Недостаточно прав!", "Запустите программу от имени администратора", QtWidgets.QMessageBox.Ok)

        except Exception:
            QtWidgets.QMessageBox.critical(self, "Ошибка!", "Что-то пошло не так :(", QtWidgets.QMessageBox.Ok)

        self.set_ping(server)
        self.set_patch_status(server)
        self.update_button(server)

    def server_button_pushed(self, server):
        if server['patched']:
            self.unpatch_server(server)
        else:
            self.patch_server(server)
if __name__ == '__main__':
    app = QtWidgets.QApplication(argv)
    pathcer = Patcher()
    exit(app.exec_())