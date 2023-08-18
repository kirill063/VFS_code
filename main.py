import datetime
import telebot
from telebot import types
import requests
from supabase import create_client, Client
from dotenv import load_dotenv


load_dotenv()

url: str = "https://tsppbudfocbwnbegwewt.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzcHBidWRmb2Nid25iZWd3ZXd0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5MTUzNDE5NywiZXhwIjoyMDA3MTEwMTk3fQ.CwWdh3pLjx36cOcyvdKsSY1EbcCluiask8jHLCO9FGg"
supabase: Client = create_client(url, key)

bot = telebot.TeleBot('6494937849:AAGFWDDRV-v_oofvPTjSntySzJBxS8uwe-I')



#first page
visa_application_centre = None
ls_q = None
sub_c = None

#passport
first_name = None
last_name = None
Gender = None
date_of_birth = None
current_nat = None
passport_s = None
passport_n = None
pass_exp_date = None

#contact info
phone_code = None
phone_num = None
email_cl = None

#register date
#reg_date = None

#Редактирование данных
k = 0
k1 = 1
current_date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

@bot.message_handler(commands=['send_photos'])
def send_photos(message):
    global k1, current_date
    chat_id = message.chat.id

    # Получаем список фото из сообщения пользователя
    photos = message.photo

    # Создаем новую папку на Яндекс диске
    folder_name = f'{last_name}_{first_name}_{k1}_{current_date}'
    create_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources?path=Docs/' + folder_name
    headers = {'Authorization': 'y0_AgAAAABwAI0nAApXqAAAAADqW7za-AXhm2fIRrqWjHAHGz0vzK9nGNg'}
    response = requests.put(create_folder_url, headers=headers)

    if response.status_code == 201:
        # Если папка успешно создана, сохраняем фото в эту папку
        folder_path = f'Docs/{folder_name}/'

        for i, photo in enumerate(photos):
            # Скачиваем фото с сервера Telegram
            file_info = bot.get_file(photo.file_id)
            file_url = 'https://api.telegram.org/file/bot{}/{}'.format(bot.token, file_info.file_path)
            response = requests.get(file_url)

            if response.status_code == 200:
                # Если фото успешно скачано, сохраняем его на Яндекс диск
                file_name = 'photo_{}.jpg'.format(i + 1)
                upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path={}'.format(
                    folder_path + file_name)
                headers = {'Authorization': 'y0_AgAAAABwAI0nAApXqAAAAADqW7za-AXhm2fIRrqWjHAHGz0vzK9nGNg'}
                response = requests.get(upload_url, headers=headers)

                if response.status_code == 200:
                    upload_info = response.json()

                    # Загружаем фото на Яндекс диск
                    upload_response = requests.put(upload_info['href'], data=response.content)

                    if upload_response.status_code == 201:
                        # Если фото успешно загружено, отправляем сообщение пользователю
                        bot.send_message(chat_id, 'Фото {} успешно загружено'.format(i + 1))
                    else:
                        bot.send_message(chat_id, 'Ошибка при загрузке фото {}'.format(i + 1))
                else:
                    bot.send_message(chat_id,
                                     'Ошибка при получении ссылки для загрузки фото {}'.format(i + 1))
            else:
                bot.send_message(chat_id, 'Ошибка при скачивании фото {} с сервера Telegram'.format(i + 1))
    else:
        bot.send_message(chat_id, 'Ошибка при создании папки')
    markup_photo_ed = types.ReplyKeyboardMarkup()
    btn_photo1 = types.KeyboardButton('Загрузить фото')
    btn_photo2 = types.KeyboardButton('Завершить загрузку фото')
    markup_photo_ed.add(btn_photo1)
    markup_photo_ed.add(btn_photo2)
    bot.send_message(message.chat.id, 'Загрузите фотографии всех необходимых документов.\n'
                                      'Для загрузки нажмите: Загрузить фото\n'
                                      'Если все фотографии загружены нажмите: Завержить загрузку фото\n'
                                      'Загрузите все фото одним сообщением', reply_markup=markup_photo_ed)
    k1 += 1
    bot.register_next_step_handler(message, send_photo)
@bot.message_handler()
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton('✉️Создать заявку')
    markup.add(btn0)
    bot.send_message(message.chat.id, 'Добро пожаловать в VFS Global.\n'
                                      'Для того, чтобы создать заяку, нажмите на кнопку: '
                                      '✉️Создать заявку', reply_markup=markup)
    bot.register_next_step_handler(message, start_2)

def start_2(message):
    if message.text == '✉️Создать заявку':
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Irkutsk')
        btn2 = types.KeyboardButton('Kaliningrad')
        btn3 = types.KeyboardButton('Kazan')
        btn4 = types.KeyboardButton('Khabarovsk')
        btn5 = types.KeyboardButton('Krasnodar')
        btn6 = types.KeyboardButton('Krasnoyarsk')
        btn7 = types.KeyboardButton('Moscow')
        btn8 = types.KeyboardButton('Nizhniy Novgorod')
        btn9 = types.KeyboardButton('Novosibirsk')
        btn10 = types.KeyboardButton('Omsk')
        btn11 = types.KeyboardButton('Perm')
        btn12 = types.KeyboardButton('Rostov on Don')
        btn13 = types.KeyboardButton('Samara')
        btn14 = types.KeyboardButton('Saratov')
        btn15 = types.KeyboardButton('St Petersburg')
        btn16 = types.KeyboardButton('Ufa')
        btn17 = types.KeyboardButton('Vladivostok')
        btn18 = types.KeyboardButton('Yekaterinburg')
        btn19 = types.KeyboardButton('Любое')
        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6,
                    btn7, btn8, btn9, btn10, btn11, btn12,
                    btn13, btn14, btn15, btn16, btn17, btn18, btn19)
        bot.send_message(message.chat.id, '1. Выберите место подачи заявления:', reply_markup=markup2)
        bot.register_next_step_handler(message, first_part)
    else:
        bot.send_message(message.chat.id,
                         'Неправильный ввод. Если вы хотите создать заявку, введите: ✉️Создать заявку')
        bot.register_next_step_handler(message, start)

def first_part(message):
    global visa_application_centre
    visa_application_centre = message.text
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2_1 = types.KeyboardButton('Длительная поездка')
    btn2_2 = types.KeyboardButton('Короткая поездка')
    btn2_3 = types.KeyboardButton('Любая')
    markup3.add(btn2_1, btn2_2, btn2_3)
    bot.send_message(message.chat.id, '2. Укажите длительность поездки', reply_markup=markup3)
    bot.register_next_step_handler(message, first_part_3)


def first_part_3(message):
    global ls_q
    ls_q = message.text
    if k == 2:
        bot.register_next_step_handler(message, mail_f)
    else:
        if message.text == 'Короткая поездка':
            markup_ss = types.ReplyKeyboardMarkup()
            btn_ss_1 = types.KeyboardButton('Settlement in France of an ascendant of a EU citizen or his foreign spouse')
            btn_ss_2 = types.KeyboardButton('All kind of other short stay visas')
            btn_ss_3 = types.KeyboardButton('Children of spouse of French/EU/EEA/CH/UK')
            btn_ss_4 = types.KeyboardButton('Flight/cargo crew (following to their base or training)')
            btn_ss_5 = types.KeyboardButton('For medical treatment or burial of a family member')
            btn_ss_6 = types.KeyboardButton('Foreign minor children of a French/EU citizen')
            btn_ss_7 = types.KeyboardButton('International truck drivers')
            btn_ss_8 = types.KeyboardButton('Married or PACS to French/EEA/CH/UK citizen')
            btn_ss_9 = types.KeyboardButton('Veafarers')
            btn_ss_10 = types.KeyboardButton('Visa Parent of a French child')
            btn_ss_11 = types.KeyboardButton('Visa for business or professional purpose')
            btn_ss_12 = types.KeyboardButton('Visa to marry a French citizen in France')
            btn_ss_13 = types.KeyboardButton('Ascendant of French citizen or of his foreign spouse')
            markup_ss.add(btn_ss_1)
            markup_ss.add(btn_ss_2)
            markup_ss.add(btn_ss_3)
            markup_ss.add(btn_ss_4)
            markup_ss.add(btn_ss_5)
            markup_ss.add(btn_ss_6)
            markup_ss.add(btn_ss_7)
            markup_ss.add(btn_ss_8)
            markup_ss.add(btn_ss_9)
            markup_ss.add(btn_ss_10)
            markup_ss.add(btn_ss_11)
            markup_ss.add(btn_ss_12)
            markup_ss.add(btn_ss_13)
            bot.send_message(message.chat.id, '3. Укажите цель поездки:', reply_markup=markup_ss)
            bot.register_next_step_handler(message, stay_type)
        elif message.text == 'Длительная поездка':
            markup_ls = types.ReplyKeyboardMarkup()
            btn_ls_1 = types.KeyboardButton('All kind of other long stay visas')
            btn_ls_2 = types.KeyboardButton('Ascendant of French citizen or of his foreign spouse')
            btn_ls_3 = types.KeyboardButton('Beneficiary of OFII decision for family reunification')
            btn_ls_4 = types.KeyboardButton('Lecteur et assistant de langue')
            btn_ls_5 = types.KeyboardButton('Official posting - Carte PRO-MAE')
            btn_ls_6 = types.KeyboardButton('Passeport-Talents and accompanying spouses and minor children')
            btn_ls_7 = types.KeyboardButton('Salarie OFII Guyane projet SOYUZ')
            btn_ls_8 = types.KeyboardButton('Foreign children of a French/EU citizen')
            btn_ls_9 = types.KeyboardButton('Married or PACS to EU/ EEA/CH/UK citizen resident in France')
            btn_ls_10 = types.KeyboardButton('Married or PACS to a French citizen')
            btn_ls_11 = types.KeyboardButton('Researchers invited by French research institution')
            btn_ls_12 = types.KeyboardButton('Visa Parent of a French child')
            btn_ls_13 = types.KeyboardButton('Visa for children of spouse of French/EU')
            btn_ls_14 = types.KeyboardButton('Long visa for studying in a higher education institution')
            markup_ls.add(btn_ls_1)
            markup_ls.add(btn_ls_2)
            markup_ls.add(btn_ls_3)
            markup_ls.add(btn_ls_4)
            markup_ls.add(btn_ls_5)
            markup_ls.add(btn_ls_6)
            markup_ls.add(btn_ls_7)
            markup_ls.add(btn_ls_8)
            markup_ls.add(btn_ls_9)
            markup_ls.add(btn_ls_10)
            markup_ls.add(btn_ls_11)
            markup_ls.add(btn_ls_12)
            markup_ls.add(btn_ls_13)
            markup_ls.add(btn_ls_14)
            bot.send_message(message.chat.id, '3. Укажите цель поездки:', reply_markup=markup_ls)
            bot.register_next_step_handler(message, stay_type)
        elif message.text == 'Любая':
            stay_type(message)
        else:
            bot.send_message(message.chat.id, 'Неправильный ввод! Попробуйте еще раз')
            bot.register_next_step_handler(message, first_part_3)

def stay_type(message):
    global sub_c
    if message.text == 'Любая':
        sub_c = '-'
    else:
        sub_c = message.text
    a = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Данные сохранены! Заполните паспотрные данные. \n\n'
                                      '1. Введите свое имя: \n(на английском как в паспорте)', reply_markup=a)
    bot.register_next_step_handler(message, first_name_f)

def first_name_f(message):
    global first_name
    first_name = message.text.strip()
    bot.send_message(message.chat.id, '2. Введите свою фамилию: \n(на английском как в паспорте)')
    bot.register_next_step_handler(message, last_name_f)

def last_name_f(message):
    global last_name
    last_name = message.text.strip()
    markup_gender = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btg1 = types.KeyboardButton('Male')
    btg2 = types.KeyboardButton('Female')
    btg3 = types.KeyboardButton('Others / Transgender')
    markup_gender.add(btg1, btg2, btg3)
    bot.send_message(message.chat.id, '3. Укажите свой пол: \n(на английском как в паспорте)', reply_markup=markup_gender)
    bot.register_next_step_handler(message, if_gender)

def if_gender(message):
    global Gender
    a = telebot.types.ReplyKeyboardRemove()
    if message.text == 'Male':
        Gender = 'Male'
    elif message.text == 'Female':
        Gender = 'Female'
    elif message.text == 'Others / Transgender':
        Gender = 'Others / Transgender'
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод. Попробуйте еще раз')
        bot.register_next_step_handler(message, if_gender)
    bot.send_message(message.chat.id, '7. Введите дату своего рождения: ДД/ММ/ГГГГ', reply_markup=a)
    bot.register_next_step_handler(message, date_of_birth_f)

def date_of_birth_f(message):
    global date_of_birth
    date_of_birth = message.text
    bot.send_message(message.chat.id, '8. Укажите свое текущее гражданство: '
                                      '\n(на английском полностью как в паспорте)')
    bot.register_next_step_handler(message, nationality)

def nationality(message):
    global current_nat
    current_nat = message.text.upper()
    bot.send_message(message.chat.id, '9. Введите серию и номер своего паспорта: \n(через пробел)')
    bot.register_next_step_handler(message, series_f)

def series_f(message):
    global passport_s, passport_n
    temp_p = message.text.split()
    passport_s = temp_p[0]
    passport_n = temp_p[1]
    bot.send_message(message.chat.id, '10. Введите срок действия паспорта: \n(в формате ДД/ММ/ГГГГ)')
    bot.register_next_step_handler(message, expiary_f)

def expiary_f(message):
    global pass_exp_date
    pass_exp_date = message.text
    bot.send_message(message.chat.id, 'Паспортные данные сохранены! \n'
                                      'Введите свою контактную информацию:\n\n'
                                      '11. Укажите свой контактный телефон: \n'
                                      '(в формате [код без +][пробел][основной номер])')
    bot.register_next_step_handler(message, phone)

def phone(message):
    global phone_num, phone_code
    num = message.text.split(sep=None)
    phone_code = num[0]
    phone_num = num[1]
    a_delete = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '13. Укажите свою почту:', reply_markup=a_delete)
    bot.register_next_step_handler(message, mail_f)

def mail_f(message):
    if k == 0 or k == 12:
        global email_cl
        email_cl = message.text
    ask_photo(message)

def ask_photo(message):
    markup_photo = types.ReplyKeyboardMarkup()
    btn_photo1 = types.KeyboardButton('Загрузить фото')
    btn_photo2 = types.KeyboardButton('Завершить загрузку фото')
    markup_photo.add(btn_photo1)
    markup_photo.add(btn_photo2)
    bot.send_message(message.chat.id, 'Загрузите фотографии всех необходимых документов.\n'
                                          'Для загрузки нажмите: Загрузить фото\n'
                                          'Если все фотографии загружены нажмите: Завержить загрузку фото\n'
                                          'Загрузите все фото одним сообщением', reply_markup=markup_photo)
    bot.register_next_step_handler(message, send_photo)
def send_photo(message):
    if message.text == "Загрузить фото":
        bot.send_message(message.chat.id, "Пришлите фотографии")
        bot.register_next_step_handler(message, send_photos)
    elif message.text == "Завершить загрузку фото":
        check(message)
    else:
        bot.send_message(message.chat.id, 'Неверный ввод')
        ask_photo(message)
def check(message):
    markup_all = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('ДА✅')
    button2 = types.KeyboardButton('НЕТ❌')
    markup_all.add(button1, button2)
    bot.send_message(message.chat.id, 'Контактные данные сохранены!\n'
                                      'Ваша заявка:\n'
                                      'ОСНОВНАЯ ИНФОРМАЦИЯ✅\n'
                                      f'1. Визовый центр подачи заявки: {visa_application_centre}\n'
                                      f'2. Длительность поездки: {ls_q}\n'
                                      f'3. Цель поездки: {sub_c}\n'
                                      'ПАСПОРТНЫЕ ДАННЫЕ✅\n'
                                      f'4. Имя: {first_name}\n'
                                      f'5. Фамилия: {last_name}\n'
                                      f'6. Пол: {Gender}\n'
                                      f'7. Дата рождения: {date_of_birth}\n'
                                      f'8. Гражданство: {current_nat}\n'
                                      f'9. Серия и номер паспорта: {passport_s} {passport_n}\n'
                                      f'10.Дата окончания срока действия паспорта: {pass_exp_date}\n'
                                      'КОНТАКТНАЯ ИНФОРМАЦИЯ✅\n'
                                      f'11.Номер телефона: +{phone_code}{phone_num}\n'
                                      f'12.Почта: {email_cl}\n\n'
                                      'Все верно?', reply_markup=markup_all)
    bot.register_next_step_handler(message, all)

#####################################################################################################################

def all(message):
    if message.text == 'ДА✅':
        a1 = types.ReplyKeyboardMarkup()
        btn_again = types.KeyboardButton('✉️Создать заявку')
        btn_stop = types.KeyboardButton('Завершить работу')
        a1.add(btn_again)
        a1.add(btn_stop)

        data = supabase.table("VFS_Global").insert({"visa city": f"{visa_application_centre}",
                                                    "long_short": f"{ls_q}",
                                                    "sub_c": f"{sub_c}",
                                                    "first name": f"{first_name}",
                                                    "second name": f"{last_name}",
                                                    "sex": f"{Gender}",
                                                    "birth date": f"{date_of_birth}",
                                                    "nationality": f"{current_nat}",
                                                    "passport series": f"{passport_s}",
                                                    "passport number": f"{passport_n}",
                                                    "passport exp. date": f"{pass_exp_date}",
                                                    "phone code": f"{phone_code}",
                                                    "phone number": f"{phone_num}",
                                                    "email": f"{email_cl}",
                                                    "ya_link": "https://disk.yandex.ru/d/obL0b1MFwRfrTg"
                                                   }).execute()



        bot.send_message(message.chat.id, 'Заявка успешно подана! \n'
                                          'Хотите составить ещё одну зявку? Если да, нажмите'
                                          ' "✉️Создать заявку"', reply_markup=a1)
        bot.register_next_step_handler(message, again_f)
    elif message.text == 'НЕТ❌':
        markup_edit = types.ReplyKeyboardMarkup()
        butn1 = types.KeyboardButton('1')
        butn2 = types.KeyboardButton('2,3')
        butn4 = types.KeyboardButton('4')
        butn5 = types.KeyboardButton('5')
        butn6 = types.KeyboardButton('6')
        butn7 = types.KeyboardButton('7')
        butn8 = types.KeyboardButton('8')
        butn9 = types.KeyboardButton('9')
        butn10 = types.KeyboardButton('10')
        butn11 = types.KeyboardButton('11')
        butn12 = types.KeyboardButton('12')
        butn13 = types.KeyboardButton('13')
        markup_edit.add(butn1, butn2, butn4,
                        butn5, butn6, butn7,
                        butn8, butn9, butn10,
                        butn11, butn12, butn13)
        bot.send_message(message.chat.id, 'Выберите пункт, который вы хотели бы изменить:', reply_markup=markup_edit)
        bot.register_next_step_handler(message, if_edit)
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод. Нажмите на кнопку ДА✅/НЕТ❌')
        bot.register_next_step_handler(message, all)




#####################################################################################################################

def if_edit(message):
    global k
    if message.text == '1':
        k = 1
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Irkutsk')
        btn2 = types.KeyboardButton('Kaliningrad')
        btn3 = types.KeyboardButton('Kazan')
        btn4 = types.KeyboardButton('Khabarovsk')
        btn5 = types.KeyboardButton('Krasnodar')
        btn6 = types.KeyboardButton('Krasnoyarsk')
        btn7 = types.KeyboardButton('Moscow')
        btn8 = types.KeyboardButton('Nizhniy Novgorod')
        btn9 = types.KeyboardButton('Novosibirsk')
        btn10 = types.KeyboardButton('Omsk')
        btn11 = types.KeyboardButton('Perm')
        btn12 = types.KeyboardButton('Rostov on Don')
        btn13 = types.KeyboardButton('Samara')
        btn14 = types.KeyboardButton('Saratov')
        btn15 = types.KeyboardButton('St Petersburg')
        btn16 = types.KeyboardButton('Ufa')
        btn17 = types.KeyboardButton('Vladivostok')
        btn18 = types.KeyboardButton('Yekaterinburg')
        btn19 = types.KeyboardButton('Любое')
        markup2.add(btn1, btn2, btn3, btn4, btn5, btn6,
                    btn7, btn8, btn9, btn10, btn11, btn12,
                    btn13, btn14, btn15, btn16, btn17, btn18, btn19)
        bot.send_message(message.chat.id, 'Выберите место подачи заявления:', reply_markup=markup2)
        bot.register_next_step_handler(message, visa_a_c_edit)
    elif message.text == '2,3':
        k = 2
        markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn2_1 = types.KeyboardButton('Длительная поездка')
        btn2_2 = types.KeyboardButton('Короткая поездка')
        btn2_3 = types.KeyboardButton('Любая')
        markup3.add(btn2_1, btn2_2, btn2_3)
        bot.send_message(message.chat.id, 'Укажите длительность поездки:', reply_markup=markup3)
        bot.register_next_step_handler(message, ls_edit)
    elif message.text == '4':
        k = 4
        bot.send_message(message.chat.id, 'Введите свое имя: (на английском как в паспорте)')
        bot.register_next_step_handler(message, first_name_edit)
    elif message.text == '5':
        k = 5
        bot.send_message(message.chat.id, 'Введите свою фамилию: (на английском как в паспорте)')
        bot.register_next_step_handler(message, last_name_edit)
    elif message.text == '6':
        k = 6
        markup_gender = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btg1 = types.KeyboardButton('Male')
        btg2 = types.KeyboardButton('Female')
        btg3 = types.KeyboardButton('Others / Transgender')
        markup_gender.add(btg1, btg2, btg3)
        bot.send_message(message.chat.id, '3. Укажите свой пол:', reply_markup=markup_gender)
        bot.register_next_step_handler(message, gender_edit)
    elif message.text == '7':
        k = 7
        bot.send_message(message.chat.id, '7. Введите дату своего рождения: ДД/ММ/ГГГГ')
        bot.register_next_step_handler(message, date_of_birth_edit)
    elif message.text == '8':
        k = 8
        bot.send_message(message.chat.id, '8. Укажите свое текущее гражданство: '
                                          '(на английском полностью как в паспорте)')
        bot.register_next_step_handler(message, national_edit)
    elif message.text == '9':
        k = 9
        bot.send_message(message.chat.id, '9. Введите серию и номер своего паспорта: (через пробел)')
        bot.register_next_step_handler(message, series_edit)
    elif message.text == '10':
        k = 10
        bot.send_message(message.chat.id, '10. Введите срок действия паспорта: ДД/ММ/ГГГГ')
        bot.register_next_step_handler(message, expiary_edit)
    elif message.text == '11':
        k = 11
        bot.send_message(message.chat.id, 'Паспортные данные сохранены! \n'
                                          'Введите свою контактную информацию:\n\n'
                                          '11. Укажите свой контактный телефон: \n'
                                          '(в формате [код без +][пробел][основной номер])')
        bot.register_next_step_handler(message, phone_edit)
    elif message.text == '12':
        bot.send_message(message.chat.id, '12. Укажите свою почту:')
        bot.register_next_step_handler(message, mail_f)

#######################################################################################################################
def visa_a_c_edit(message):
    global visa_application_centre
    visa_application_centre = message.text
    check(message)

def ls_edit(message):
    global ls_q
    ls_q == message.text
    if ls_q == 'Короткая поездка':
        markup_ss = types.ReplyKeyboardMarkup()
        btn_ss_1 = types.KeyboardButton('Settlement in France of an ascendant of a EU citizen or his foreign spouse')
        btn_ss_2 = types.KeyboardButton('All kind of other short stay visas')
        btn_ss_3 = types.KeyboardButton('Children of spouse of French/EU/EEA/CH/UK')
        btn_ss_4 = types.KeyboardButton('Flight/cargo crew (following to their base or training)')
        btn_ss_5 = types.KeyboardButton('For medical treatment or burial of a family member')
        btn_ss_6 = types.KeyboardButton('Foreign minor children of a French/EU citizen')
        btn_ss_7 = types.KeyboardButton('International truck drivers')
        btn_ss_8 = types.KeyboardButton('Married or PACS to French/EEA/CH/UK citizen')
        btn_ss_9 = types.KeyboardButton('Veafarers')
        btn_ss_10 = types.KeyboardButton('Visa Parent of a French child')
        btn_ss_11 = types.KeyboardButton('Visa for business or professional purpose')
        btn_ss_12 = types.KeyboardButton('Visa to marry a French citizen in France')
        btn_ss_13 = types.KeyboardButton('Ascendant of French citizen or of his foreign spouse')
        markup_ss.add(btn_ss_1)
        markup_ss.add(btn_ss_2)
        markup_ss.add(btn_ss_3)
        markup_ss.add(btn_ss_4)
        markup_ss.add(btn_ss_5)
        markup_ss.add(btn_ss_6)
        markup_ss.add(btn_ss_7)
        markup_ss.add(btn_ss_8)
        markup_ss.add(btn_ss_9)
        markup_ss.add(btn_ss_10)
        markup_ss.add(btn_ss_11)
        markup_ss.add(btn_ss_12)
        markup_ss.add(btn_ss_13)
        bot.send_message(message.chat.id, '3. Укажите цель поездки:', reply_markup=markup_ss)
        bot.register_next_step_handler(message, ls_edit2)
    elif ls_q == 'Длительная поездка':
        markup_ls = types.ReplyKeyboardMarkup()
        btn_ls_1 = types.KeyboardButton('All kind of other long stay visas')
        btn_ls_2 = types.KeyboardButton('Ascendant of French citizen or of his foreign spouse')
        btn_ls_3 = types.KeyboardButton('Beneficiary of OFII decision for family reunification')
        btn_ls_4 = types.KeyboardButton('Lecteur et assistant de langue')
        btn_ls_5 = types.KeyboardButton('Official posting - Carte PRO-MAE')
        btn_ls_6 = types.KeyboardButton('Passeport-Talents and accompanying spouses and minor children')
        btn_ls_7 = types.KeyboardButton('Salarie OFII Guyane projet SOYUZ')
        btn_ls_8 = types.KeyboardButton('Foreign children of a French/EU citizen')
        btn_ls_9 = types.KeyboardButton('Married or PACS to EU/ EEA/CH/UK citizen resident in France')
        btn_ls_10 = types.KeyboardButton('Married or PACS to a French citizen')
        btn_ls_11 = types.KeyboardButton('Researchers invited by French research institution')
        btn_ls_12 = types.KeyboardButton('Visa Parent of a French child')
        btn_ls_13 = types.KeyboardButton('Visa for children of spouse of French/EU')
        btn_ls_14 = types.KeyboardButton('Long visa for studying in a higher education institution')
        markup_ls.add(btn_ls_1)
        markup_ls.add(btn_ls_2)
        markup_ls.add(btn_ls_3)
        markup_ls.add(btn_ls_4)
        markup_ls.add(btn_ls_5)
        markup_ls.add(btn_ls_6)
        markup_ls.add(btn_ls_7)
        markup_ls.add(btn_ls_8)
        markup_ls.add(btn_ls_9)
        markup_ls.add(btn_ls_10)
        markup_ls.add(btn_ls_11)
        markup_ls.add(btn_ls_12)
        markup_ls.add(btn_ls_13)
        markup_ls.add(btn_ls_14)
        bot.send_message(message.chat.id, '3. Укажите цель поездки:', reply_markup=markup_ls)
        bot.register_next_step_handler(message, ls_edit2)
    elif ls_q == 'Любая':
        ls_edit2(message)

def ls_edit2(message):
    global sub_c
    if message.text == 'Любая':
        sub_c = '-'
    else:
        sub_c = message.text
    check(message)

def first_name_edit(message):
    global first_name
    first_name = message.text
    check(message)

def last_name_edit(message):
    global last_name
    last_name = message.text
    check(message)

def gender_edit(message):
    global Gender
    Gender = message.text
    check(message)

def date_of_birth_edit(message):
    global date_of_birth
    date_of_birth = message.text
    check(message)

def national_edit(message):
    global current_nat
    current_nat = message.text.upper()
    check(message)

def series_edit(message):
    global passport_s, passport_n
    temp_p = message.text.split()
    passport_s = temp_p[0]
    passport_n = temp_p[1]
    check(message)

def expiary_edit(message):
    global pass_exp_date
    pass_exp_date = message.text
    check(message)

def phone_edit(message):
    global phone_num, phone_code
    num = message.text.split(sep=None)
    phone_code = num[0]
    phone_num = num[1]
    check(message)

#предложить заполнить заявку для еще одного человека
def again_f(message):
    if message.text == '✉️Создать заявку':
        start_2(message)
    else:
        markup_end = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Finish', reply_markup=markup_end)



bot.polling(none_stop=True)