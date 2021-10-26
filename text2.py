import os,time,tkinter as tk,_thread as th

def auto():
    b=''
    f=''
    while True:
        time.sleep(0.1)
        c=T.index(tk.INSERT)
        if c!=f:
            win.title(c)
            f=c
       
        T.tag_add("here", "1.0", "1.end")
        T.tag_config("here",font=('comics',20))
        
        a=T.get('1.0','1.end')
        if a!=b:
            T.delete('2.0','end')
            
            if a in os.listdir():
                
                d=open(a)
                e=d.read()
                d.close()
                T.insert('end','\n')
                T.insert('end',e)
            b=a

def close():
    a=T.get('1.0','1.end')
    b=T.get('2.0','end')
    i=open(a,'w')
    i.write(b)
    i.close()

    win.title('%s is Saved'%a)
    win.update()
    time.sleep(1)
    win.destroy()

def autosave(rt):
    if '1.'in T.index(tk.INSERT):
        pass
    else:
        a=T.get('1.0','1.end')
        b=T.get('2.0','end')
        i=open(a,'w')
        i.write(b)
        i.close()

win=tk.Tk()
win['bg']='white'

T=tk.Text(win,font=('comics',10),wrap='none')
T.pack(padx=2,pady=2,expand=1,fill='both')
T.bind('<Key>',autosave)
T.focus()

win.protocol("WM_DELETE_WINDOW",close)

th.start_new_thread(auto,())

win.mainloop()
