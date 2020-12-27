import streamlit as st
import pickle
import numpy as np
from tkinter import *
from tkinter import font as tkFont
model=pickle.load(open('model.pkl','rb'))


def predict_forest(oxygen,humidity,temperature):
    input=np.array([[oxygen,humidity,temperature]]).astype(np.float64)
    prediction=model.predict_proba(input)
    print(prediction)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    print(pred)
    print(float(pred))
    return float(pred)

def main():
    class MyWindow:
        def __init__(self, win):
            self.lbl1=Label(win, text='Oxygen')
            self.lbl2=Label(win, text='Humidity')
            self.lbl4=Label(win, text='Result')
            self.lbl3=Label(win, text='Temperature')
            self.lbl6=Label(win, text='Predict the probability of Forest-Fire Occurence')
            
            self.t1=Entry()
            self.t2=Entry()
            self.t3=Entry()
            self.t4=Entry()
            
            
        
            self.lbl1.place(x=100, y=50)
            self.lbl6.place(x=100, y=10)
            self.t1.place(x=200, y=50)
            self.lbl2.place(x=100, y=100)
            self.t2.place(x=200, y=100)
            #self.lbl5=Label(win, text='Hello')
            self.btn1=Button(win, text='Predict', command=self.add)
            
            self.btn1.place(x=260, y=200)
            
        
            self.lbl4.place(x=100, y=250)
            self.lbl3.place(x=100, y=150)
            #self.lbl5.place(x=100, y=300)
            self.t3.place(x=200, y=150)
            self.t4.place(x=200, y=250)
        
        def add(self):
                self.t4.delete(0, 'end')
                oxygen=int(self.t1.get())
                humidity=int(self.t2.get())
                temperature=int(self.t3.get())
                output=predict_forest(oxygen,humidity,temperature)
                
                self.t4.insert(END, str(output))
    window=Tk()
    mywin=MyWindow(window)
    window.title('FORINTENSHA')
    window.geometry("500x300+30+30")
    window.mainloop()

if __name__=='__main__':
    main()
