# Warface Server Patcher
![GitHub all releases](https://img.shields.io/github/downloads/ShitryaDima/wf-server-patcher/total?style=flat-square)
![GitHub](https://img.shields.io/github/license/shitryadima/wf-server-patcher?style=flat-square)
  
В начале 2021 года в Игровом центре mail.ru был ограничен доступ к выбору любого регионального сервера для игры Warface. Остались доступны лишь сервера с наименьшей задержкой.

Warface Server Patcher вносит изменения в hosts файл Windows, перенаправляя ping-запрос Игрового центра  на локальный хост, что позволяет обойти  данное ограничение без каких-либо изменений в коде клиента.


## Установка
1. Использование собранного exe-файла (**рекомендуется**)  
Скачайте актульнную версию программы на вкладке [Releases](https://github.com/ShitryaDima/wf-server-patcher/releases/).

2. Использование исходников
+ Без сборки. Установите все зависимости из файла requirements.txt и запустите файл patcher.py из скачанного репозитория.
+ Со сборкой. Соберите проект в exe-файл, используя PyInstaller (для этого у вас также должны быть установлены все необходимые зависимости)

## Поддержать меня

Если вы хотите материально поддержать меня, то я буду рад принять ваши донаты [здесь](https://my.qiwi.com/Dmytryi-ShQF-gooIbl).

## Лицензия

[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
