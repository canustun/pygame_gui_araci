# Geliştiric @CanÜstün
import os,random,webbrowser
import tkinter as tk
from threading import Thread

try:
    import pygame_gui,pygame
except:
    for i in ["pygame_gui","pygame"]:os.system(f"pip install {i}")
    import pygame_gui,pygame
    
pygame.init()
pygame.display.set_caption("")
font = pygame.font.SysFont("consolas",15)
ekran = pygame.display.set_mode((5,5), pygame.RESIZABLE)

kareler_adet = 0
kareler = []
kareler_cikti = []
kareler_hane = []
xler ,yler = [],[]
metinler = []
genislikler ,yukseklikler = [], []

def daha_fazlasi():
    webbrowser.open("www.ginifab.com/feeds/pms/color_picker_from_image.tr.php")
        
def renk_bilgi():
    renk_bilgi_sayfa = tk.Tk()
    renk_bilgi_sayfa.geometry("240x400")
    renk_bilgi_sayfa.resizable(False,False)
    renk_bilgi_sayfa.title("Renkler")

    ing_renk = ["violet","beige","green","brown","silver","pink","blue","cyan","red","black","gray","purple","yellow","orange"]
    tr_renk = ["Eflatun","Bej","Yeşil","Kahverengi","Gümüş","Pembe","Mavi","Açık Mavi","Kırmızı","Siyah","Gri","Mor","Sarı","Turuncu"]

    tk.Label(renk_bilgi_sayfa,text = "Renkler                         :              Renk Kodu" ).place(x = 10,y = 0)    

    for i_renk, t_renk , sira in zip(ing_renk, tr_renk, range(13)):
        tk.Label(renk_bilgi_sayfa,text = t_renk ,bg = i_renk, width = 15).place(x = 10,y = sira*25+25)    
        tk.Label(renk_bilgi_sayfa,text = i_renk.capitalize() , width = 15).place(x = 150,y = sira*25+25)    

    tk.Button(renk_bilgi_sayfa,text ="> Daha Fazla Renk <",bg = "silver" ,fg = "Red",command = daha_fazlasi).place(x = 60,y = sira*25+55)
    
    renk_bilgi_sayfa.mainloop()

    
def elemanlar(x,y,gen,yuk,tur,i):
    global genislikler,yler,xler,yukseklikler,eleman_ekran,manager
    eleman_ekran = tk.Tk()
    eleman_ekran.title("Sayfadaki Elemanlar")
    eleman_ekran.geometry("200x200")
    tk.Label(eleman_ekran,text = f"{tur} Özellikleri", fg = "Red", font = ("İtalic",10)).place(x = 35, y = 0)

    def guncelle():
        if True:#try:
            """xler[index] = int(butonx.get())
            yler[index] = int(butony.get())
            genislikler[index] = int(butongenis.get())
            yukseklikler[index] = int(butonyuksek.get())"""
            
            butonlara = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((xler[i], yler[i]), (genislikler[i], yukseklikler[i])),
                        text=metinler[i],
                        manager=manager)


        #except:pass
        pencere.after(300,guncelle)
        
    guncelle()
    tk.Label(eleman_ekran,text = "X :").place(x = 0, y = 25)
    butonx = tk.Entry(eleman_ekran)
    butonx.insert(0,str(x))
    butonx.place(x = 60,y = 25)

    tk.Label(eleman_ekran,text = "Y :").place(x = 0, y = 50)
    butony = tk.Entry(eleman_ekran)
    butony.insert(0,str(y))
    butony.place(x = 60,y = 50)

    tk.Label(eleman_ekran,text = "Genişlik :").place(x = 0, y = 75)
    butongenis = tk.Entry(eleman_ekran)
    butongenis.insert(0,str(gen))
    butongenis.place(x = 60,y = 75)

    tk.Label(eleman_ekran,text = "Yükseklik :").place(x = 0, y = 100)
    butonyuksek = tk.Entry(eleman_ekran)
    butonyuksek.insert(0,str(yuk))
    butonyuksek.place(x = 60,y = 100)

    #(command = onayla).place(x, = ,y = )
    eleman_ekran.mainloop()
    
def olustur():
    global eleman_ekran,ekran,xler,yler,yukseklikler,genislikler,kareler_adet,kareler,kareler_hane,kareler_cikti,genis,yuksek, manager
    try:
        genis = int(genislik.get())
        yuksek = int(yukseklik.get())
        manager = pygame_gui.UIManager((genis, yuksek))

        ekran  = pygame.display.set_mode((genis,yuksek), pygame.RESIZABLE)
        ekran.fill(renk.get())
        try:
            kareler_cikti = []
            kareler = []
            kareler_hane = []
            for i in range(kareler_adet):
                
                karecik = pygame.draw.rect(ekran,("White"),pygame.Rect(xler[i],yler[i],genislikler[i], yukseklikler[i]))
                kareler.append(karecik)
                kareler_hane.append(i)
            for i in range(len(yler)):
                butonlara = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((xler[i], yler[i]), (genislikler[i], yukseklikler[i])),
                                             text=metinler[i],
                                             manager=manager)
                kareler_cikti.append(f"""pygame_gui.elements.UIButton(relative_rect=pygame.Rect(({xler[i]}, {yler[i]}), ({genislikler[i]}, {yukseklikler[i]})),text='Tık',manager=manager)""")

        except:pass
        fare_konum = pygame.mouse.get_pos()

        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.display.quit()

         elif event.type == pygame.MOUSEBUTTONUP:

            for i,j in zip(kareler,kareler_hane):
                if kareler[j].collidepoint(fare_konum[0],fare_konum[1]):
                    a = Thread(target = elemanlar,args=(xler[j],yler[j],genislikler[j], yukseklikler[j],"Buton",j)).start()
            
        manager.update(0.1)
        pygame.display.set_caption(baslik.get())
        manager.draw_ui(ekran)
        pygame.display.update()

    except:pass
       
    pencere.after(300,olustur)

def cikti():
    with open("pygame_cikti.txt","w+") as dosyamiz:
        dosyamiz.write(f"import pygame, pygame_gui\npygame.init()\npygame.display.set_caption('{baslik.get()}')\nfont = pygame.font.SysFont('consolas',15)")
        dosyamiz.write(f"\nekran = pygame.display.set_mode(({genislik.get()},{yukseklik.get()}), pygame.RESIZABLE)\n")
        dosyamiz.write("font = pygame.font.SysFont('consolas',15)\n")
        dosyamiz.write(f"manager = pygame_gui.UIManager(({genis}, {yuksek}))\n")
        dosyamiz.write("butonlar = [")
        for i in kareler_cikti:
            dosyamiz.write(i+",")
        dosyamiz.write("]\n")

        dosyamiz.write(f"""calis = True
while calis:
    ekran.fill('{renk.get()}')
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            calis = False
    for i in butonlar:
        
    pygame.display.update()""")

    try:
        os.rename("pygame_cikti.txt","pygame_cikti.py")
    except:
        os.remove("pygame_cikti.py")
        os.rename("pygame_cikti.txt","pygame_cikti.py")
        
def ekleme():
    global xler, yler, genislikler, yuksekliler,kareler_adet,metinler
    kareler_adet+=1
    buton_metin = metin.get()
    butonxx = int(butonx.get())
    butonyy = int(butony.get())
    buttongen = int(butongenis.get())
    buttonyuk = int(butonyuksek.get())
    metinler.append(buton_metin)
    xler.append(butonxx)
    yler.append(butonyy)
    genislikler.append(buttongen)
    yukseklikler.append(buttonyuk)

   
pencere = tk.Tk()
pencere.title("Pencere Ayarları")
pencere.geometry("200x350")
pencere.resizable(False,False)
tk.Label(pencere,text = "Buton Oluşturma ", fg = "Red", font = ("İtalic",10)).place(x = 45, y = 140)

tk.Label(pencere,text = "X :").place(x = 0, y = 160)
butonx = tk.Entry(pencere)
butonx.insert(0,"0")
butonx.place(x = 60,y = 160)

tk.Label(pencere,text = "Y :").place(x = 0, y = 185)
butony = tk.Entry(pencere)
butony.insert(0,"0")
butony.place(x = 60,y = 185)

tk.Label(pencere,text = "Genişlik :").place(x = 0, y = 210)
butongenis = tk.Entry(pencere)
butongenis.insert(0,"50")
butongenis.place(x = 60,y = 210)

tk.Label(pencere,text = "Yükseklik :").place(x = 0, y = 235)
butonyuksek = tk.Entry(pencere)
butonyuksek.insert(0,"50")
butonyuksek.place(x = 60,y = 235)

tk.Label(text = "Renk").place(x = 0, y = 110)
renk = tk.Entry()
renk.insert(0,"Gray")
renk.place(x = 60,y = 110)

tk.Label(text = "Metni").place(x = 0, y = 260)
metin = tk.Entry()
metin.insert(0,"Ben bir butonum")
metin.place(x = 60,y = 260)


renkler = tk.Button(pencere,text = "? ",font = ("Arial",7),width= 2,bg = "Yellow",fg = "Black",command=renk_bilgi)
renkler.place(x = 33, y = 111)

btnols = tk.Button(pencere,text = "Oluştur",bg = "Gray",fg = "White")
btnols.config(command = ekleme)
btnols.place(x = 110, y = 310)

btnols = tk.Button(pencere,text = "Kod Çıktı",bg = "Gray",fg = "White")
btnols.config(command = cikti)
btnols.place(x = 30, y = 310)

   
tk.Label(text = "Pencere Hakkında", fg = "Red", font = ("İtalic",10)).place(x = 45, y = 0)

tk.Label(text = "Genişlik :").place(x = 0, y = 35)
genislik = tk.Entry()
genislik.insert(0,"350")
genislik.place(x = 60,y = 35)

tk.Label(text = "Yukseklik :").place(x = 0, y = 60)
yukseklik = tk.Entry(text = "350")
yukseklik.insert(0,"350")
yukseklik.place(x = 60,y = 60)

tk.Label(text = "Başlık :").place(x = 0, y = 85)
baslik = tk.Entry()
baslik.insert(0,"Uygulama 1")
baslik.place(x = 60,y = 85)

olustur()
pencere.mainloop()
