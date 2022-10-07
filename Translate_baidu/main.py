#-*- coding: utf-8 -*-
from tkinter import *
from urllib import parse
from urllib import request
import hashlib
import json

def translate_word(word):
    URL = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    form_data = {}
    form_data['from'] = "en"
    form_data['to'] ='zh'
    form_data['q'] = word
    form_data['appid'] = '20220704001264213'
    form_data['salt'] = "143522088"
    Key = "a1RLJSAJ7Av4xEyB8KfC"
    m = form_data['appid'] + word + form_data['salt'] + Key
    m_MD5 = hashlib.md5(m.encode("utf-8"))
    form_data['sign'] = m_MD5.hexdigest()
    data = parse.urlencode(form_data).encode("utf-8")
    response = request.urlopen(URL,data)
    html = response.read().decode("utf-8")
    translate_word = json.loads(html)
    print(translate_word)
    translate_result = translate_word['trans_result'][0]['dst']

    print(f"translate_result:{translate_result}")
    return translate_result



def leftClick1(event):
    pass

def leftClick2(event):
    pass

if __name__ == '__main__':
    # root = Tk()
    # root.title('Translations')
    # root['width']=250;root['height']=250
    # Label(root,text='Translations words',width=15).place(x=1,y=1)
    # Entry1 = Entry(root,width=20)
    # Entry1.place(x=110,y=1)
    # Label(root,text='Results',width=15).place(x=1,y=20)
    # s = StringVar()
    # s.set('Test Count')
    # Entry2 = Entry(root,width=20,textvariable=s)
    # Entry2.place(x=110,y=20)
    # Button1 = Button(root,width=20,text='Translate')
    # Button1.place(x=0,y=80)
    # Button2 = Button(root,width=20,text='Empty Translations')
    # Button1.bind("<Button-1>",leftClick1)
    # Button2.bind("<Button-1>",leftClick2)
    # Button2.place(x=110,y=80)
    # root.mainloop()
    translate_word("apples is my favorite food")