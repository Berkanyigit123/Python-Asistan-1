#BERKAN YİĞİT.GİTHUB


#konuşulanları dinleme için:
import speech_recognition as sr
#saat ve tarih için:
from datetime import datetime
#web de arama yapmada kullanılan kütüphane:
import webbrowser
import time
#speechten texte
from gtts import gTTS
#python ses çıkışı veren library
from playsound import playsound
import random
from random import choice
import os
from lxml import html  # html dosyasını okumak için
import requests  # istek göndermek için
import json  # json dosyalarını okumak için
import feedparser  # hava  durumunu çekmek için
import colorama  # terminal ekranını özelleştirmek için.Ben yeşil yaptım
from colorama import Fore, Back, \
    Style  # Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.

r = sr.Recognizer()  # speech recognition ile alınan sesi r adlı değikene atıyoruz
colorama.init()

def record(ask=False):
    with sr.Microphone() as source:  # record dan gelen veri işleniyor
        if ask:
            speak(ask)
            print(Fore.BLUE)
            print(ask)

        audio = r.listen(source)  #text audio ya dönüyor
        voice = ''
        try:  #
            voice = r.recognize_google(audio, language='tr-TR')  # Türkçe dinleme yapıp bunu voice e atıyoruz
        except sr.UnknownValueError:  #ses tanımlaması

            print(Fore.GREEN)
            print("MAKİ ASİSTAN = ne dedin, anlamadım , acaba tekrar edermisin")
            speak("ne dedin, anlamadım , acaba tekrar edermisin")


        except sr.RequestError:  # eğerki sistemle alakalı bir hata alırsak burası çalışıyoruz
            speak('Sistemin çalışmıyor')
            print(Fore.GREEN)
            print('MAKİ ASİSTAN = Sistemin çalışmıyor')

        return voice  # dinlediğimiz voice ı geri döndürüyoruz


def response(voice):  # voice ile gelen veriyi sorgululamak için response adında bir fonkiyon
    if 'nasılsın' in voice:  # eğer voice nin içinde nasılsın  diye bir değer varsa bunları yap
        # sözler adlı bir dizi tanımlıyoruz
        sozler = ["iyilik benden ya sen",
                  "iyi ben peki ya sen",
                  "iyi olduğumu duyunca sevineceğini biliyorum",
                  "ben bir yapay zekadan ibaretim duygularım yok ama tüm yazılımım düzgün çalışıyor",

                  ]
        secim = choice(sozler)  # sozlerden birini karışık olarak seçilecek

        speak(secim)  # seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + secim)  # seçilen söz yazdırılacak

    if 'teşekkür ederim' in voice:  # eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = ne demek herzaman")  # ekrana yazılacak veri
        speak("ne demek herzaman")  # sesli bir şekilde söylenmesi için

    if 'iyiyim' in voice:  # eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = iyi olmana sevindim senin için ne yapabilirim")  # ekrana yazılacak veri
        speak("iyi olmana sevindim senin için ne yapabilirim")  # sesli bir şekilde söylenmesi için

    if 'kötüyüm' in voice:  # eğer voice nin içinde kötüyüm diye bir değer varsa bunları yap
        # sozlerOlumsuz adlı bir dizi tanımlıyoruz
        sozlerOlumsuz = ["üzüldüm senin adına yapabileceğim bir şey varmı",
                         "sıkma canını benim yapabileceğim bir şey varmı",
                         "boşver iyi olmaya bak senin için birşey yapabilirmiym",
                         "ben bir yapay zekayım sadece sana yardımcı olabilirim bu konuda elimden birşey gelmez ama  istersen başka bir şey yapabilirim",

                         ]
        secimolumsuz = choice(sozlerOlumsuz)  # sozlerden birini karışık olarak seçilecek

        speak(secimolumsuz)  # seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + secimolumsuz)  # seçilen söz ekrana yazılması için

    if 'Neler yapabilirsin' in voice:  # eğer voice nin içinde neler yapabilirsin diye bir değer varsa bunları yap
        speak(
            'seninle sohbet edebilirim , saati söyleyebiilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım, youtube da video açabilirim ')
        print(Fore.GREEN)
        print(
            'seninle sohbet edebilirim , saati söyleyebiilirim , hava durumunu söylerim ,senin yerine googleda arama yaparım, youtube da video açabilirim ')

    if 'Sen kimsin' in voice:  # eğer voice nin içinde sen kimsin diye bir değer varsa bunları yap
        print(Fore.GREEN)
        speak('Benim adım MAKİ asistan yani baykuş asistan demek 7 24 çalışıyorum.Berkanın oyuncağıyım')  # selendirelecek
        print('MAKİ ASİSTAN = Benim adım MAKİ asistan yani baykuş asistan demek 7 24 çalışıyorum.Berkanın oyuncağıyım')  # ekrana yazılacak

    if 'saat kaç' in voice:  # eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
        speak(datetime.now().strftime('%H:%M:%S'))  # datetime.now sayesinde anlık saati alıyoruz ve seslendiriyouz
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + datetime.now().strftime(
            '%H:%M:%S'))  # datetime.now sayesinde anlık saati alıyoruz ve yazdırıyoruz

    if 'arama yap' in voice:  # eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        search = record(
            'ne aramamı istersin')  # record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp search değişkenine tanımlıyouz
        url = 'https://google.com/search?q=' + search  # https://google.com/search?q= adresine aldığımız search ı ekliyoruz ve url değişkenine tanımlıyouz
        webbrowser.get().open(url)  # web browserı açıyouz ve  url değişkenini dönderiyouz
        speak(search + ' için bulduğum sonuçlar')  # sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + search + ' için bulduğum sonuçlar')  # ekrana yazdırma yapıyouz

    if "YouTube'da ara" in voice:  # eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        searchy = record(
            'ne aramamı istersin')  # record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp searchy değişkenine tanımlıyouz
        urly = 'https://www.youtube.com/results?search_query=' + searchy
        webbrowser.get().open(urly)  # web browserı açıyouz ve  urly değişkenini dönderiyouz
        speak(searchy + ' için bulduğum sonuçlar')  # sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + searchy + ' için bulduğum sonuçlar')  # ekrana yazdırma yapıyouz

    if 'hava durumu' in voice:  # eğer voice nin içinde hava durumu diye bir değer varsa bunları yap
        # feedparser ile link deki veriyi çekip parçalıyouz bunuda parse değişkenine tanımlıyouz
        parse = feedparser.parse(
            "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|81010|DUZCE|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havail = parse[2]  # havaiiladlı adlı değişkene parsenin 3.değeri olan il adını tanımlıyoruz
        havadetay = parse[4]  # havadetay adlı  değişkene parsenin 5. değeri olan dereceyi tanımlıyoruz
        speak(havail + " için hava" + havadetay + " derece")  # sesli söyletiouz
        print(Fore.GREEN)
        print("MAKİ ASİSTAN = " + havail + " için hava" + havadetay + " derece")  # ekrana yazdırıyouz

    if 'güle güle' in voice:  # eğer voice nin içinde güle güle diye bir değer varsa bunları yap
        speak('görüşürüz')  # sesli söyletiouz
        print(Fore.GREEN)
        print('MAKİ ASİSTAN = görüşürüz')  # ekrana yazdırıyouz
        exit()  # uygulamadan çıkış yapıyouz


def speak(string):  # speak adlı bir fonksiyon oluştuyouz
    tts = gTTS(string, lang='tr')  # sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyouz
    rand = random.randint(1,
                          100)  # random 1 ve 100 arası bir sayı üretip rand adlı değişkene tanımlıyouz bunun amacı bir hata ile karşılaşıp mp3 dosyası silinmezse üsütne yazmasın diye
    file = 'ses-' + str(rand) + '.mp3'  # .mp3 uzantılı bir ses dosyası oluşturuyoruz
    tts.save(file)  # dosyayı kayıt ediyouz
    playsound(file)  # dosyayı okutuyoyz
    os.remove(file)  # dosyayı siliyouz

speak('Seni dinliyorum Senin için ne yapabilirim')  # ilk açılışta asiatanın bizi karşılaması için
print(Fore.GREEN)
print(
    'MAKİ ASİSTAN = Seni dinliyorum Senin için ne yapabilirim')  # ilk açılışta asiatanın bizi karşılamasını yazdırmak için
time.sleep(1)  # uygulamyı 1 saniye uyutuyouz dinlemede karışıklık olmaması için
while 1:  # tek bir komut aldıktan sonra kapanmaması için sonsuz döngü oluşturuyoruz
    voice = record()
    print(Fore.BLUE)
    print(voice)
    response(voice)
    print(Fore.GREEN)
    speak('başka bir isteğin varmı')
    print('BAŞKA BİR İSTEĞİN VARMI')
