#this
from tkinter import *
from tkinter import ttk, messagebox 
from gtts import gTTS
import random
import time
import playsound

root0=Tk()
root0.title("Русский язык")
root0.geometry("1350x800")


def on_closing():
    if messagebox.askokcancel("Выход из приложения","Хотите выйти из приложения?"):
        root0.destroy()

root0.protocol("WM_DELETE_WINDOW",on_closing)
root0.title("Русский язык")
root0.resizable(0,0)
root0.wm_attributes("-topmost",1)
canvas=Canvas(root0,width=900,height=600,bd=0,highlightthickness=0)
canvas.pack()
def gp():
    mes='Здравствуйте Я Голосовой помощник. Я вам помогу учить русский язык.'
    def say_mes(mes):
        voice=gTTS(mes, lang="ru")
        file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
        voice.save(file_voice_name)
        playsound.playsound(file_voice_name)

    say_mes(mes)
btn=Button(root0,text='Голосовой помощник',bg='#FFF',command=gp, font=("Times New Roman",13,'bold'))
btn.place(x=600,y=300)


def b1():
    root0.withdraw()
    root1 = Tk()     
    root1.title("Урок 1 Здравствуйте!\Dars. Salom!")     
    root1.geometry("1350x800")
    def bt16():
        root1.withdraw()
        root0.deiconify()
    btn=Button(root1,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
        
    def table1():
        root1.withdraw()
        y1=Tk()
        y1.title("Здравствуйте!\Dars. Salom!")
        y1.geometry("1350x800")
        label = Label(y1,text="Здравствуйте!\ Salom!", bg="#FFF", font=("Times New Roman",21,"bold")) # создаем текстовую метку
        label.pack()
        def bt16():
            y1.withdraw()
            root1.deiconify()
        btn=Button(y1,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)

        def bt():
            mes='Здравствуйте.'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=60)

        def bt1():
            label = Label(y1,text="Salom",  font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=60)
        btn = Button(y1,text="Здравствуйте.",bg="#FFF",command=bt1,font=("Times New Roman",13) )
        btn.place(x=70,y=60,width=250,height=32)

        def bt2():
            mes='Добрый день.'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt2,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=95)

        def bt3():
            label = Label(y1,text="Hayirli kun.", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=95)
        btn = Button(y1,text="Добрый день.",bg="#FFF", command=bt3,font=("Times New Roman",13) )
        btn.place(x=70,y=95,width=250,height=32)

        def bt4():
            mes='Извините, можно войти?'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt4,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=130)

        def bt5():
            label = Label(y1,text="Kechiring, kirsam maylimi?",  font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=130)
        btn = Button(y1,text="Извините, можно войти?",bg="#FFF", command=bt5,font=("Times New Roman",13) )
        btn.place(x=70,y=130,width=250,height=32)

        def bt6():
            mes='Да, пожалуйста.Вы на экзамен?'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt6,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=165)

        def bt7():
            label = Label(y1,text="Ha, marhamat. Siz imtihongamisiz?", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=165)
        btn = Button(y1,text="Да, пожалуйста.Вы на экзамен?",bg="#FFF",command=bt7,font=("Times New Roman",13) )
        btn.place(x=70,y=165,width=250,height=32)

        def bt8():
            mes='Да, на экзамен.'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt8,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=199)

        def bt9():
            label = Label(y1,text="Ha, imtihonga.", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=199)
        btn = Button(y1,text="Да, на экзамен.",bg="#FFF",command=bt9,font=("Times New Roman",13) )
        btn.place(x=70,y=199,width=250,height=32)

        def bt10():
            mes='Подождите минуту.'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt10,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=235)

        def bt11():
            label = Label(y1,text="Bir daqiqa kutib turing.", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=235)
        btn = Button(y1,text="Подождите минуту.",bg="#FFF",command=bt11,font=("Times New Roman",13) )
        btn.place(x=70,y=235,width=250,height=32)

        def bt12():
            mes='Хорошо!'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)


        btn = Button(y1,text="Голос",command=bt12,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=269)

        def bt13():
            label = Label(y1,text="Yaxshi!", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=269)
        btn = Button(y1,text="Хорошо!",bg="#FFF",command=bt13,font=("Times New Roman",13) )
        btn.place(x=70,y=269,width=250,height=32)
        def bt14():
            mes='Здравствуйте.— Добрый день.— Извините, можно войти?— Да, пожалуйста. Вы на экзамен?— Да, на экзамен.— Подождите минуту.— Хорошо!'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
                label = Label(y1,text="Salom", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=60)
                label = Label(y1,text="Hayirli kun.", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=95)
                label = Label(y1,text="Kechiring, kirsam maylimi?",  font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=130)
                label = Label(y1,text="Ha, marhamat. Siz imtihongamisiz?", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=165)
                label = Label(y1,text="Ha, imtihonga.", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=199)
                label = Label(y1,text="Bir daqiqa kutib turing.", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=235)
                label = Label(y1,text="Yaxshi!", font=("Times New Roman",18)) # создаем текстовую метку
                label.place(x=320,y=269)
            say_mes(mes)
        btn = Button(y1,text="Bce голоса",command=bt14,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=303)
            
        y1.mainloop()
    btn=Button(root1,text="Здравствуйте!\Dars. Salom!",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root1.withdraw()
        y2=Tk()
        y2.title('Учим грамматику')
        y2.geometry("1350x800")
        def bt16():
            y2.withdraw()
            root1.deiconify()
        btn=Button(y2,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
        def bt14():
            label1=Label(y2,text='Одушевлённые существительные обозначают живые объекты:'+'\n'+' людей и животных, и отвечают на вопрос КТО? Неодушевлённые'+'\n'+ 'существительные обозначают неживые предметы и отвечают'+'\n'+ 'на вопрос ЧТО?'+'\n'+
                '— Кто это?'+'\n'+'— Это мужчина. Это женщина. Это собака.'+'\n'+'— Что это?'+'\n'+'— Это дом. Это книга.',font=("Times New Roman",12,))
            label1.place(x=445,y=50)
            label2=Label(y2,text='Jonli otlar tirik ob’ektlarning ma’nosini bildiradilar: odamlarni va'+'\n'+'hayvonlarni va KIM? so’rog’iga javob beradilar. Jonsiz otlar jonsiz'+'\n'+'ob’ektlarning ma’nosini bildiradi va NIMA? so’rog’iga javob beradilar.'+'\n'+'— Bu kim ?'+'\n'+'— Bu erkak. Bu ayol. Bu it.'+'\n'+'— Bu nima?'+'\n'+'— Bu uy. Bu kitob.',font=("Times New Roman",12))
            label2.place(x=905,y=50)
        btn=Button(y2,text="1) Одушевлённые и неодушевлённые существительные"+'\n'+
                   'Jonli va jonsiz otlar',bg='#FFF',command=bt14, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=50,width=440,height=64)

        def bt15():
            label1=Label(y2,text='Обратите внимание, что местоимение вы употребляется не только в'+'\n'+'значении множественного числа, но и как форма вежливого'+'\n'+
                'обращения к одному человеку. В этом случае оно обычно пишется'+'\n'+'с большой буквы. Местоимение оно употребляется вместо'+'\n'+
                'неодушевлённых существительных среднего рода.',font=("Times New Roman",12))
            label1.place(x=445,y=215)
            label2=Label(y2,text='Etibor qiling, «вы» (siz) olmoshi nafaqat ko’pchilik ma’nosida, balki'+'\n'+
                'bir insonga hurmat yuzasida hamqo’llanadi. Bunday holatlarda u bosh'+'\n'+
                'harf bilan yoziladi. «оно» olmoshi jonsiz otlar o’rnida qo’llanadi.',font=("Times New Roman",12))
            label2.place(x=905,y=215)
        btn=Button(y2,text='2) Личные местоимения в именительном падеже'+'\n'+
                   'Kishilik olmoshlar',bg='#FFF',command=bt15, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=215,width=440,height=64)
        def bt17():
            label1=Label(y2,text='Когда вы здороваетесь или обращаетесь к незнакомому человеку'+'\n'+'или старшему по возрасту и по званию, надо обращаться к нему на'+'\n'+ '«Вы» и говорить здравствуйте, извините, скажите, подождите и т.д.'+
                        '\n'+'«Вы»'+'\n'+'— Здравствуйте!'+'\n'+'— Добрый день!'+'\n'+'— Извините, можно войти?'+'\n'+'— Подождите минуту!'+
                         '\n'+'— Хорошо.'+'\n'+'«Ты»'+'\n'+'— Здравствуй!'+'\n'+'— Добрый день!'+'\n'+'— Извини, можно войти?'+
                         '\n'+'— Подожди минуту!'+'\n'+'— Хорошо.',font=("Times New Roman",12))
            label1.place(x=445,y=380)
            label2=Label(y2,text='Notanish yoki sizdan yoshi va maqomi ulug’ inson bilan'+'\n'+ 'salomlashganingizda yoki unga murojat qilganingizda «Вы» deb'+'\n'+ 'murojat qilish kerak va «здравствуйте, извините, скажите,'+'\n'+ 'подождите» deb so’zlashish kerak.'+
                        '\n'+'«Siz»'+'\n'+'— Salom!'+'\n'+'— Hayrli kun!'+'\n'+'— Kechiring, kirsam maylimi?'+'\n'+'— Bir daqiqa kutib turing!'+
                        '\n'+'— Yaxshi.'+'\n'+'«Sen»'+'\n'+'— Salom!'+'\n'+'— Hayrli kun!'+'\n'+'— Kechirasan, kirsam maylimi?'+
                         '\n'+'— Bir daqiqa kutib tur!'+'\n'+'— Yaxshi.',font=("Times New Roman",12))
            label2.place(x=910,y=380)
        btn=Button(y2,text='3) Формы обращения – Вы и ты'+'\n'+
                   'Muloqot shakillari - Siz va sen',bg='#FFF',command=bt17, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=380,width=440,height=64)
        
        y2.mainloop()
    btn=Button(root1,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root1.withdraw()
        y3=Tk()
        y3.title('Учим грамматику')
        y3.geometry("1350x800")
        def bt16():
            y3.withdraw()
            root1.deiconify()
        btn=Button(y3,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
        
        label=Label(y3,text='Задание 1'+'\n'+'Выберите правильный ответ:',font=("Times New Roman",12,'bold'))
        label.place(x=0,y=10)
        label=Label(y3,text='Это Антон. ... это?',font=("Times New Roman",12))
        label.place(x=0,y=50)
        def z1():
            mes='Хорошо!'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn=Button(y3,text='Кто',bg='#FFF',command=z1,font=("Times New Roman",12))
        btn.place(x=0,y=75)
        def z2():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn=Button(y3,text='Что',bg='#FFF',command=z2,font=("Times New Roman",12))
        btn.place(x=50,y=75)
        
        label=Label(y3,text='Это работа. ... это?',font=("Times New Roman",12))
        label.place(x=0,y=110)        
        def z3():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)            
        btn=Button(y3,text='Кто',bg='#FFF',command=z3,font=("Times New Roman",12))
        btn.place(x=0,y=135)
        def z4():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)            
        btn=Button(y3,text='Что',bg='#FFF',command=z4,font=("Times New Roman",12))
        btn.place(x=50,y=135)
        label=Label(y3,text='Это собака. ... это?',font=("Times New Roman",12))
        label.place(x=0,y=170)         
        def z5():
            mes='Отлично'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)  
        btn=Button(y3,text='Что',bg='#FFF',command=z5,font=("Times New Roman",12))
        btn.place(x=0,y=195)
        def z6():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)  
        btn=Button(y3,text='Кто',bg='#FFF',command=z6,font=("Times New Roman",12))
        btn.place(x=50,y=195)
        
        label=Label(y3,text='Задание 2'+'\n'+'Выберите правильный ответ:',font=("Times New Roman",12,'bold'))
        label.place(x=220,y=10)
        label=Label(y3,text='Это Иван. Кто ... ?',font=("Times New Roman",12))
        label.place(x=220,y=50)
        def z7():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)  
        btn=Button(y3,text='Он',bg='#FFF',command=z7,font=("Times New Roman",12))
        btn.place(x=220,y=75)
        def z8():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)  
        btn=Button(y3,text='Она',bg='#FFF',command=z8,font=("Times New Roman",12))
        btn.place(x=270,y=75)
        def z9():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Они',bg='#FFF',command=z9,font=("Times New Roman",12))
        btn.place(x=320,y=75)   
        label=Label(y3,text='— Проходите, пожалуйста!'+'\n'+'— ……',font=("Times New Roman",12))
        label.place(x=220,y=115)
        def z10():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Извините',bg='#FFF',command=z10,font=("Times New Roman",12))
        btn.place(x=220,y=165) 
        def z11():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Спасибо',bg='#FFF',command=z11,font=("Times New Roman",12))
        btn.place(x=220,y=199)  
        def z12():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Пожалуйста',bg='#FFF',command=z12,font=("Times New Roman",12))
        btn.place(x=220,y=233)
        label=Label(y3,text='— Подождите, пожалуйста!'+'\n'+'— ……',font=("Times New Roman",12))
        label.place(x=220,y=267)
        def z13():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Спасибо',bg='#FFF',command=z13,font=("Times New Roman",12))
        btn.place(x=220,y=301)  
        def z14():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Добрый день',bg='#FFF',command=z14,font=("Times New Roman",12))
        btn.place(x=220,y=335)
        def z15():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Нет',bg='#FFF',command=z15,font=("Times New Roman",12))
        btn.place(x=220,y=369) 
        label=Label(y3,text='— Вы на экзамен?'+'\n'+'— ……',font=("Times New Roman",12))
        label.place(x=220,y=403)
        def z16():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Извините',bg='#FFF',command=z16,font=("Times New Roman",12))
        btn.place(x=220,y=437) 
        def z17():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Спасибо',bg='#FFF',command=z17,font=("Times New Roman",12))
        btn.place(x=220,y=471)
        def z18():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Да',bg='#FFF',command=z18,font=("Times New Roman",12))
        btn.place(x=220,y=505) 
        label=Label(y3,text='— Здравствуйте!'+'\n'+'— ……',font=("Times New Roman",12))
        label.place(x=220,y=539)
        def z19():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Пожалуйста',bg='#FFF',command=z19,font=("Times New Roman",12))
        btn.place(x=220,y=573) 
        def z20():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Спасибо',bg='#FFF',command=z20,font=("Times New Roman",12))
        btn.place(x=220,y=607)
        def z21():
            mes='Отлично'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn=Button(y3,text='Добрый день',bg='#FFF',command=z21,font=("Times New Roman",12))
        btn.place(x=220,y=641) 
        label=Label(y3,text='— ………., можно войти?' ,font=("Times New Roman",12))
        label.place(x=450,y=10)
        def z19():
            mes='Ошибка'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Спасибо',bg='#FFF',command=z19,font=("Times New Roman",12))
        btn.place(x=450,y=44) 
        def z20():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Извините',bg='#FFF',command=z20,font=("Times New Roman",12))
        btn.place(x=450,y=78)
        def z21():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn=Button(y3,text='Хорошо',bg='#FFF',command=z21,font=("Times New Roman",12))
        btn.place(x=450,y=112)
        label=Label(y3,text='— ………… минуту.' ,font=("Times New Roman",12))
        label.place(x=450,y=146)
        def z22():
            mes='Нет'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Проходите',bg='#FFF',command=z22,font=("Times New Roman",12))
        btn.place(x=450,y=180) 
        def z23():
            mes='Молодец'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)              
        btn=Button(y3,text='Подождите',bg='#FFF',command=z23,font=("Times New Roman",12))
        btn.place(x=450,y=214)
        def z24():
            mes='Неправильно'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn=Button(y3,text='Извините',bg='#FFF',command=z24,font=("Times New Roman",12))
        btn.place(x=450,y=248)
        y3.mainloop()
    btn=Button(root1,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200)   
    
    root1.mainloop()
btn = Button(root0,text="Урок 1 Здравствуйте!\Dars. Salom!",bg="#FFF",command=b1,font=("Times New Roman",13,'bold') )
btn.place(x=0,y=60)


def b2():
    root0.withdraw()
    root2 = Tk()     
    root2.title("Урок 2 Давайте познакомимся\Keling, tanishaylik")     
    root2.geometry("1350x800")
    def bt16():
        root2.withdraw()
        root0.deiconify()
    btn=Button(root2,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root2.withdraw()
        y21=Tk()
        y21.title("Давайте познакомимся\Keling, tanishaylik")
        y21.geometry("1350x800")
        def bt16():
            y21.withdraw()
            root2.deiconify()
        btn=Button(y21,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
        def bt():
            mes='Давайте'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=60)

        def bt1():
            label = Label(y21,text="Keling", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=60)
        btn = Button(y21,text="Давайте",bg="#FFF",command=bt1,font=("Times New Roman",13) )
        btn.place(x=70,y=60,width=250,height=32)
        
        def bt2():
            mes='Давайте познакомимся!'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt2,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=95)

        def bt3():
            label = Label(y21,text="Keling, tanishaylik!", font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=95)
        btn = Button(y21,text="Давайте познакомимся!",bg="#FFF", command=bt3,font=("Times New Roman",13) )
        btn.place(x=70,y=95,width=250,height=32)
        
        def bt4():
            mes='Как вас зовут?'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt4,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=130)

        def bt5():
            label = Label(y21,text="Ismingiz nima?!",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=130)
        btn = Button(y21,text="Как вас зовут?",bg="#FFF", command=bt5,font=("Times New Roman",13) )
        btn.place(x=70,y=130,width=250,height=32)
        
        def bt6():
            mes='Меня зовут…'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt6,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=165)

        def bt7():
            label = Label(y21,text="Mening ismim…",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=165)
        btn = Button(y21,text="Меня зовут…",bg="#FFF", command=bt7,font=("Times New Roman",13) )
        btn.place(x=70,y=165,width=250,height=32)
        
        def bt8():
            mes='Я'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt8,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=200)
        def bt9():
            label = Label(y21,text="Men",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=200)
        btn = Button(y21,text="Я",bg="#FFF", command=bt9,font=("Times New Roman",13) )
        btn.place(x=70,y=200,width=250,height=32)       
        
        def bt10():
            mes='Меня'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt10,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=235)
        def bt11():
            label = Label(y21,text="Mening/Meni",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=235)
        btn = Button(y21,text="Меня",bg="#FFF", command=bt11,font=("Times New Roman",13) )
        btn.place(x=70,y=235,width=250,height=32)    
        
        def bt12():
            mes='Моя'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt12,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=270)
        def bt13():
            label = Label(y21,text="Mening",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=270)
        btn = Button(y21,text="Моя",bg="#FFF", command=bt13,font=("Times New Roman",13) )
        btn.place(x=70,y=270,width=250,height=32)
        
        def bt14():
            mes='Вы'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt14,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=305)
        def bt15():
            label = Label(y21,text="Siz",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=305)
        btn = Button(y21,text="Вы",bg="#FFF", command=bt15,font=("Times New Roman",13) )
        btn.place(x=70,y=305,width=250,height=32)
        
        def bt16():
            mes='Вас'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt16,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=340)
        def bt17():
            label = Label(y21,text="Sizning/Sizni",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=340)
        btn = Button(y21,text="Вас",bg="#FFF", command=bt17,font=("Times New Roman",13) )
        btn.place(x=70,y=340,width=250,height=32)
        
        def bt18():
            mes='Ваша'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt18,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=375)
        def bt19():
            label = Label(y21,text="Sizning/Sizlarning",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=375)
        btn = Button(y21,text="Ваша",bg="#FFF", command=bt19,font=("Times New Roman",13) )
        btn.place(x=70,y=375,width=250,height=32)
    
        def bt20():
            mes='Имя'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt20,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=410)
        def bt21():
            label = Label(y21,text="Ism",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=410)
        btn = Button(y21,text="Имя",bg="#FFF", command=bt21,font=("Times New Roman",13) )
        btn.place(x=70,y=410,width=250,height=32)
        
        def bt22():
            mes='Отчество'
            def say_mes(mes):
                voice=gTTS(mes, lang="ru")
                file_voice_name='_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
                voice.save(file_voice_name)
                playsound.playsound(file_voice_name)
            say_mes(mes)
        btn = Button(y21,text="Голос",command=bt22,font=("Times New Roman",13,"bold") )
        btn.place(x=0,y=445)
        def bt23():
            label = Label(y21,text="Otasining ismi/otchestvo",font=("Times New Roman",18)) # создаем текстовую метку
            label.place(x=320,y=445)
        btn = Button(y21,text="Отчество",bg="#FFF", command=bt23,font=("Times New Roman",13) )
        btn.place(x=70,y=445,width=250,height=32)
        
        
    btn=Button(root2,text="Давайте познакомимся\Keling, tanishaylik",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root2.withdraw()
        y22=Tk()
        y22.title('Учим грамматику')
        y22.geometry("1350x800")
        def bt16():
            y22.withdraw()
            root2.deiconify()
        btn=Button(y22,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root2,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root2.withdraw()
        y23=Tk()
        y23.title('Учим грамматику')
        y23.geometry("1350x800")
        def bt16():
            y23.withdraw()
            root2.deiconify()
        btn=Button(y23,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root2,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 2 Давайте познакомимся\Keling, tanishaylik",bg="#FFF",command=b2,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=95)

def b3():
    root0.withdraw()
    root3 = Tk()     
    root3.title("Урок 3 Родной язык\Ona tili")     
    root3.geometry("1350x800")
    def bt16():
        root3.withdraw()
        root0.deiconify()
    btn=Button(root3,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root3.withdraw()
        y31=Tk()
        y31.title("Родной язык\Ona tili")
        y31.geometry("1350x800")
        def bt16():
            y31.withdraw()
            root3.deiconify()
        btn=Button(y31,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root3,text="Родной язык\Ona tili",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root3.withdraw()
        y32=Tk()
        y32.title('Учим грамматику')
        y32.geometry("1350x800")
        def bt16():
            y32.withdraw()
            root3.deiconify()
        btn=Button(y32,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root3,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root3.withdraw()
        y33=Tk()
        y33.title('Учим грамматику')
        y33.geometry("1350x800")
        def bt16():
            y33.withdraw()
            root3.deiconify()
        btn=Button(y33,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root3,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 3 Родной язык\Ona tili",bg="#FFF",command=b3,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=129)

def b4():
    root0.withdraw()
    root4 = Tk()     
    root4.title("Урок 4 Моя семья\Mening oilam")     
    root4.geometry("1350x800")
    
    def bt16():
        root4.withdraw()
        root0.deiconify()
    btn=Button(root4,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root4.withdraw()
        y41=Tk()
        y41.title("Моя семья\Mening oilam")
        y41.geometry("1350x800")
        def bt16():
            y41.withdraw()
            root4.deiconify()
        btn=Button(y41,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root4,text="Моя семья\Mening oilam",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200) 
    def table2():
        root4.withdraw()
        y42=Tk()
        y42.title('Учим грамматику')
        y42.geometry("1350x800")
        def bt16():
            y42.withdraw()
            root4.deiconify()
        btn=Button(y42,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root4,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root4.withdraw()
        y43=Tk()
        y43.title('Учим грамматику')
        y43.geometry("1350x800")
        def bt16():
            y43.withdraw()
            root4.deiconify()
        btn=Button(y43,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root4,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 4 Моя семья\Mening oilam",bg="#FFF",command=b4,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=163)

def b5():
    root0.withdraw()
    root5 = Tk()     
    root5.title("Урок 5 Где вы живете?\Siz qayerda yashaysiz?")     
    root5.geometry("1350x800")
    
    def bt16():
        root5.withdraw()
        root0.deiconify()
    btn=Button(root5,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root5.withdraw()
        y51=Tk()
        y51.title("Где вы живете?\Siz qayerda yashaysiz?")
        y51.geometry("1350x800")
        def bt16():
            y51.withdraw()
            root5.deiconify()
        btn=Button(y51,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root5,text="Где вы живете?\Siz qayerda yashaysiz?",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root5.withdraw()
        y52=Tk()
        y52.title('Учим грамматику')
        y52.geometry("1350x800")
        def bt16():
            y52.withdraw()
            root5.deiconify()
        btn=Button(y52,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root5,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root5.withdraw()
        y53=Tk()
        y53.title('Учим грамматику')
        y53.geometry("1350x800")
        def bt16():
            y53.withdraw()
            root5.deiconify()
        btn=Button(y53,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root5,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 5 Где вы живете?\Siz qayerda yashaysiz?",bg="#FFF",command=b5,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=197)

def b6():
    root0.withdraw()
    root6 = Tk()     
    root6.title("Урок 6 Сколько вам лет?\Sizning yoshingiz nechida?")     
    root6.geometry("1350x800")
    
    def bt16():
        root6.withdraw()
        root0.deiconify()
    btn=Button(root6,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root6.withdraw()
        y61=Tk()
        y61.title("Сколько вам лет?\Sizning yoshingiz nechida?")
        y61.geometry("1350x800")
        def bt16():
            y61.withdraw()
            root6.deiconify()
        btn=Button(y61,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root6,text="Сколько вам лет?\Sizning yoshingiz nechida?",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200) 
    def table2():
        root6.withdraw()
        y62=Tk()
        y62.title('Учим грамматику')
        y62.geometry("1350x800")
        def bt16():
            y62.withdraw()
            root6.deiconify()
        btn=Button(y62,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root6,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root6.withdraw()
        y63=Tk()
        y63.title('Учим грамматику')
        y63.geometry("1350x800")
        def bt16():
            y63.withdraw()
            root6.deiconify()
        btn=Button(y63,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root6,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 6 Сколько вам лет?\Sizning yoshingiz nechida?",bg="#FFF",command=b6,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=231)

def b7():
    root0.withdraw()
    root7 = Tk()     
    root7.title("Урок 7 Моя работа\Mening ishim")     
    root7.geometry("1350x800")
    
    def bt16():
        root7.withdraw()
        root0.deiconify()
    btn=Button(root7,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root7.withdraw()
        y71=Tk()
        y71.title("Моя работа\Mening ishim")
        y71.geometry("1350x800")
        def bt16():
            y71.withdraw()
            root7.deiconify()
        btn=Button(y71,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root7,text="Моя работа\Mening ishim",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root7.withdraw()
        y72=Tk()
        y72.title('Учим грамматику')
        y72.geometry("1350x800")
        def bt16():
            y72.withdraw()
            root7.deiconify()
        btn=Button(y72,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root7,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root7.withdraw()
        y73=Tk()
        y73.title('Учим грамматику')
        y73.geometry("1350x800")
        def bt16():
            y73.withdraw()
            root7.deiconify()
        btn=Button(y73,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root7,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 7 Моя работа\Mening ishim",bg="#FFF",command=b7,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=265)

def b8():
    root0.withdraw()
    root8 = Tk()     
    root8.title("Урок 8 Кафе\Kafe")     
    root8.geometry("1350x800")
    
    def bt16():
        root8.withdraw()
        root0.deiconify()
    btn=Button(root8,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root8.withdraw()
        y81=Tk()
        y81.title("Кафе\Kafe")
        y81.geometry("1350x800")
        def bt16():
            y81.withdraw()
            root8.deiconify()
        btn=Button(y81,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root8,text="Кафе\Kafe",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200) 
    def table2():
        root8.withdraw()
        y82=Tk()
        y82.title('Учим грамматику')
        y82.geometry("1350x800")
        def bt16():
            y82.withdraw()
            root8.deiconify()
        btn=Button(y82,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root8,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root8.withdraw()
        y83=Tk()
        y83.title('Учим грамматику')
        y83.geometry("1350x800")
        def bt16():
            y83.withdraw()
            root8.deiconify()
        btn=Button(y83,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root8,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 8 Кафе\Kafe",bg="#FFF",command=b8,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=299)

def b9():
    root0.withdraw()
    root9 = Tk()     
    root9.title("Урок 9 Транспорт\Transport")     
    root9.geometry("1350x800")
    
    def bt16():
        root9.withdraw()
        root0.deiconify()
    btn=Button(root9,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root9.withdraw()
        y91=Tk()
        y91.title("Транспорт\Transport")
        y91.geometry("1350x800")
        def bt16():
            y91.withdraw()
            root9.deiconify()
        btn=Button(y91,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root9,text="Транспорт\Transport",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root9.withdraw()
        y92=Tk()
        y92.title('Учим грамматику')
        y92.geometry("1350x800")
        def bt16():
            y92.withdraw()
            root9.deiconify()
        btn=Button(y92,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root9,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root9.withdraw()
        y93=Tk()
        y93.title('Учим грамматику')
        y93.geometry("1350x800")
        def bt16():
            y93.withdraw()
            root9.deiconify()
        btn=Button(y93,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root9,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 9 Транспорт\Transport",bg="#FFF",command=b9,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=333)

def b10():
    root0.withdraw()
    root10 = Tk()     
    root10.title("Урок 10 Свободное время\Bo’sh vaqt")     
    root10.geometry("1350x800")
    
    def bt16():
        root10.withdraw()
        root0.deiconify()
    btn=Button(root10,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root10.withdraw()
        y101=Tk()
        y101.title("Свободное время\Bo’sh vaqt")
        y101.geometry("1350x800")
        def bt16():
            y101.withdraw()
            root10.deiconify()
        btn=Button(y101,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root10,text="Свободное время\Bo’sh vaqt",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root10.withdraw()
        y102=Tk()
        y102.title('Учим грамматику')
        y102.geometry("1350x800")
        def bt16():
            y102.withdraw()
            root10.deiconify()
        btn=Button(y102,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
        
    btn=Button(root10,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root10.withdraw()
        y103=Tk()
        y103.title('Учим грамматику')
        y103.geometry("1350x800")
        def bt16():
            y103.withdraw()
            root10.deiconify()
        btn=Button(y103,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root10,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 10 Свободное время\Bo’sh vaqt",bg="#FFF",command=b10,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=367)

def b11():
    root0.withdraw()
    root11 = Tk()     
    root11.title("Урок 11 Идем в гости\Mehmonga borayapmiz")     
    root11.geometry("1350x800")
    
    def bt16():
        root11.withdraw()
        root0.deiconify()
    btn=Button(root11,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root11.withdraw()
        y111=Tk()
        y111.title("Идем в гости\Mehmonga borayapmiz")
        y111.geometry("1350x800")
        def bt16():
            y111.withdraw()
            root11.deiconify()
        btn=Button(y111,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root11,text="Идем в гости\Mehmonga borayapmiz",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root11.withdraw()
        y112=Tk()
        y112.title('Учим грамматику')
        y112.geometry("1350x800")
        def bt16():
            y112.withdraw()
            root11.deiconify()
        btn=Button(y112,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root11,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root11.withdraw()
        y113=Tk()
        y113.title('Учим грамматику')
        y113.geometry("1350x800")
        def bt16():
            y113.withdraw()
            root11.deiconify()
        btn=Button(y113,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root11,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 11 Идем в гости\Mehmonga borayapmiz",bg="#FFF",command=b11,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=401)

def b12():
    root0.withdraw()
    root12 = Tk()     
    root12.title("Урок 12 Погода\Ob-havo")     
    root12.geometry("1350x800")
    
    def bt16():
        root12.withdraw()
        root0.deiconify()
    btn=Button(root12,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root12.withdraw()
        y121=Tk()
        y121.title("Погода\Ob-havo")
        y121.geometry("1350x800")
        def bt16():
            y121.withdraw()
            root12.deiconify()
        btn=Button(y121,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root12,text="Погода\Ob-havo",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root12.withdraw()
        y122=Tk()
        y122.title('Учим грамматику')
        y122.geometry("1350x800")
        def bt16():
            y122.withdraw()
            root12.deiconify()
        btn=Button(y122,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root12,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root12.withdraw()
        y123=Tk()
        y123.title('Учим грамматику')
        y123.geometry("1350x800")
        def bt16():
            y123.withdraw()
            root12.deiconify()
        btn=Button(y123,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root12,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 12 Погода\Ob-havo",bg="#FFF",command=b12,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=435)

def b13():
    root0.withdraw()
    root13 = Tk()     
    root13.title("Урок 13 Новая работа\Yangi ish")     
    root13.geometry("1350x800")
    
    def bt16():
        root13.withdraw()
        root0.deiconify()
    btn=Button(root13,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root13.withdraw()
        y131=Tk()
        y131.title("Новая работа\Yangi ish")
        y131.geometry("1350x800")
        def bt16():
            y131.withdraw()
            root13.deiconify()
        btn=Button(y131,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root13,text="Новая работа\Yangi ish",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200) 
    def table2():
        root13.withdraw()
        y132=Tk()
        y132.title('Учим грамматику')
        y132.geometry("1350x800")
        def bt16():
            y132.withdraw()
            root13.deiconify()
        btn=Button(y132,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root13,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root13.withdraw()
        y133=Tk()
        y133.title('Учим грамматику')
        y133.geometry("1350x800")
        def bt16():
            y133.withdraw()
            root13.deiconify()
        btn=Button(y133,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root13,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 13 Новая работа\Yangi ish",bg="#FFF",command=b13,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=469)

def b14():
    root0.withdraw()
    root14 = Tk()     
    root14.title("Урок 14 Наш город\Bizning shahar")     
    root14.geometry("1350x800")
    
    def bt16():
        root14.withdraw()
        root0.deiconify()
    btn=Button(root14,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root14.withdraw()
        y141=Tk()
        y141.title("Наш город\Bizning shahar")
        y141.geometry("1350x800")
        def bt16():
            y141.withdraw()
            root14.deiconify()
        btn=Button(y141,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root14,text="Наш город\Bizning shahar",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root14.withdraw()
        y142=Tk()
        y142.title('Учим грамматику')
        y142.geometry("1350x800")
        def bt16():
            y142.withdraw()
            root14.deiconify()
        btn=Button(y142,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root14,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root14.withdraw()
        y143=Tk()
        y143.title('Учим грамматику')
        y143.geometry("1350x800")
        def bt16():
            y143.withdraw()
            root14.deiconify()
        btn=Button(y143,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root14,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 14 Наш город\Bizning shahar",bg="#FFF",command=b14,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=503)

def b15():
    root0.withdraw()
    root15 = Tk()     
    root15.title("Урок 15 Спорт\Sport")     
    root15.geometry("1350x800")
    
    def bt16():
        root15.withdraw()
        root0.deiconify()
    btn=Button(root15,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root15.withdraw()
        y151=Tk()
        y151.title("Спорт\Sport")
        y151.geometry("1350x800")
        def bt16():
            y151.withdraw()
            root15.deiconify()
        btn=Button(y151,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root15,text="Спорт\Sport",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root15.withdraw()
        y152=Tk()
        y152.title('Учим грамматику')
        y152.geometry("1350x800")
        def bt16():
            y152.withdraw()
            root15.deiconify()
        btn=Button(y152,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root15,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root15.withdraw()
        y153=Tk()
        y153.title('Учим грамматику')
        y153.geometry("1350x800")
        def bt16():
            y153.withdraw()
            root15.deiconify()
        btn=Button(y153,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root15,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 15 Спорт\Sport",bg="#FFF",command=b15,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=537)

def b16():
    root0.withdraw()
    root16 = Tk()     
    root16.title("Урок 16 Как вы себя чувствуете?\Siz o’zingizni qanday his qilayapsiz ?")     
    root16.geometry("1350x800")
    
    def bt16():
        root16.withdraw()
        root0.deiconify()
    btn=Button(root16,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root16.withdraw()
        y161=Tk()
        y161.title("Как вы себя чувствуете?\Siz o’zingizni qanday his qilayapsiz ?")
        y161.geometry("1350x800")
        def bt16():
            y161.withdraw()
            root16.deiconify()
        btn=Button(y161,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root16,text="Как вы себя чувствуете?\Siz o’zingizni qanday his qilayapsiz ?",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root16.withdraw()
        y162=Tk()
        y162.title('Учим грамматику')
        y162.geometry("1350x800")
        def bt16():
            y162.withdraw()
            root16.deiconify()
        btn=Button(y162,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root16,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root16.withdraw()
        y163=Tk()
        y163.title('Учим грамматику')
        y163.geometry("1350x800")
        def bt16():
            y163.withdraw()
            root16.deiconify()
        btn=Button(y163,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root16,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 16 Как вы себя чувствуете?\Siz o’zingizni qanday his qilayapsiz ?",bg="#FFF",command=b16,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=571)

def b17():
    root0.withdraw()
    root17 = Tk()     
    root17.title("Урок 17 Новости\Yangiliklar")     
    root17.geometry("1350x800")
    
    def bt16():
        root17.withdraw()
        root0.deiconify()
    btn=Button(root17,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root17.withdraw()
        y171=Tk()
        y171.title("Новости\Yangiliklar")
        y171.geometry("1350x800")
        def bt16():
            y171.withdraw()
            root17.deiconify()
        btn=Button(y171,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root17,text="Новости\Yangiliklar",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root17.withdraw()
        y172=Tk()
        y172.title('Учим грамматику')
        y172.geometry("1350x800")
        def bt16():
            y172.withdraw()
            root17.deiconify()
        btn=Button(y172,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root17,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)  
    def table3():
        root17.withdraw()
        y173=Tk()
        y173.title('Учим грамматику')
        y173.geometry("1350x800")
        def bt16():
            y173.withdraw()
            root17.deiconify()
        btn=Button(y173,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root17,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 17 Новости\Yangiliklar",bg="#FFF",command=b17,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=605)

def b18():
    root0.withdraw()
    root18 = Tk()     
    root18.title("Урок 18 В банке\Bankda")     
    root18.geometry("1350x800")
    def bt16():
        root18.withdraw()
        root0.deiconify()
    btn=Button(root18,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root18.withdraw()
        y181=Tk()
        y181.title("В банке\Bankda")
        y181.geometry("1350x800")
        def bt16():
            y181.withdraw()
            root18.deiconify()
        btn=Button(y181,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root18,text="В банке\Bankda",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)
    def table2():
        root18.withdraw()
        y182=Tk()
        y182.title('Учим грамматику')
        y182.geometry("1350x800")
        def bt16():
            y182.withdraw()
            root18.deiconify()
        btn=Button(y182,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root18,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root18.withdraw()
        y183=Tk()
        y183.title('Учим грамматику')
        y183.geometry("1350x800")
        def bt16():
            y183.withdraw()
            root18.deiconify()
        btn=Button(root18,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root18,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 18 В банке\Bankda",bg="#FFF",command=b18,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=639)

def b19():
    root0.withdraw()
    root19 = Tk()     
    root19.title("Урок 19 В школе\Maktabda")     
    root19.geometry("1350x800")
    
    def bt16():
        root19.withdraw()
        root0.deiconify()
    btn=Button(root19,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root19.withdraw()
        y191=Tk()
        y191.title("В школе\Maktabda")
        y191.geometry("1350x800")
        def bt16():
            y191.withdraw()
            root19.deiconify()
        btn=Button(y191,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root19,text="В школе\Maktabda",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root19.withdraw()
        y192=Tk()
        y192.title('Учим грамматику')
        y192.geometry("1350x800")
        def bt16():
            y192.withdraw()
            root19.deiconify()
        btn=Button(y192,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root19,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root19.withdraw()
        y193=Tk()
        y193.title('Учим грамматику')
        y193.geometry("1350x800")
        def bt16():
            y193.withdraw()
            root19.deiconify()
        btn=Button(y193,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root19,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 19 В школе\Maktabda",bg="#FFF",command=b19,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=673)

def b20():
    root0.withdraw()
    root20 = Tk()     
    root20.title("Урок 20 В парке\Parkda")     
    root20.geometry("1350x800")
    def bt16():
        root20.withdraw()
        root0.deiconify()
    btn=Button(root20,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
    btn.place(x=0,y=650)
    def table1():
        root20.withdraw()
        y201=Tk()
        y201.title("В парке\Parkda")
        y201.geometry("1350x800")
        def bt16():
            y201.withdraw()
            root20.deiconify()
        btn=Button(y201,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root20,text="В парке\Parkda",bg='#FFF',command=table1, font=("Times New Roman",13,'bold'))
    btn.place(x=200,y=200)  
    def table2():
        root20.withdraw()
        y202=Tk()
        y202.title('Учим грамматику')
        y202.geometry("1350x800")
        def bt16():
            y202.withdraw()
            root20.deiconify()
        btn=Button(y202,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root20,text="Учим грамматику\Grammatikani yodlaymiz",bg='#FFF',command=table2, font=("Times New Roman",13,'bold'))
    btn.place(x=400,y=400)
    def table3():
        root20.withdraw()
        y203=Tk()
        y203.title('Учим грамматику')
        y203.geometry("1350x800")
        def bt16():
            y203.withdraw()
            root20.deiconify()
        btn=Button(y203,text='Назад\Orqaga',bg='#FFF',command=bt16, font=("Times New Roman",13,'bold'))
        btn.place(x=0,y=650)
    btn=Button(root20,text="Проверяем себя. Выполняем тест.",bg='#FFF', command=table3,font=("Times New Roman",13,'bold'))
    btn.place(x=800,y=200) 
btn=Button(root0,text="Урок 20 В парке\Parkda",bg="#FFF",command=b20,font=("Times New Roman",13,'bold'))
btn.place(x=0,y=707)

root0.mainloop()
