import PySimpleGUI as sg


sg.theme('DarkAmber')

WIN_W=30
WIN_H=50
#menu
menu_tela= [['File',['Open','Save','Exit']],
            ['Edit', ['Paste',['Special','Normal',],'Undo']],
            ['Help',['About...']]]
# Layout
layout=[[sg.Menu(menu_tela)],
        [sg.Input('0',size=(int(WIN_W/2),1),font=('Ariel',14),key='-BOX-'),
         sg.Button('Del',font=('Ariel'),key='-BACKARROW-'),
         sg.Button('ON',font=('Ariel'),key='-CLEAR-')],

        [sg.Button('7',font=('Ariel'),key='-SEVEN-'),
         sg.Button('8',font=('Ariel'),key='-EIGHT-'),
         sg.Button('9',font=('Ariel'),key='-NINE-'),
         sg.Button('+',font=('Ariel'),key='-PLUS-'),
         sg.Button('*',font=('Ariel'),key='-TIMES-')],


        [sg.Button('4',font=('Ariel'),key='-FOUR-'),
         sg.Button('5',font=('Ariel'),key='-FIVE-'),
         sg.Button('6',font=('Ariel'),key='-SIX-'),
         sg.Button('-',font=('Ariel'),key='-MINUS-'),
         sg.Button('/',font=('Ariel'),key='DIVIDED')],

        [sg.Button('1',font=('Ariel'),key='-ONE-'),
         sg.Button('2',font=('Ariel'),key='-TWO-'),
         sg.Button('3',font=('Ariel'),key='THREE-'),
         sg.Button('0',font=('Ariel'),key='-ZERO-'),
         sg.Button('=',font=('Ariel'),key='-RESULT-')]]


class Application():
    def __init__ (self):
        self.window = sg.Window('calculadora',layout=layout,margins=(0,0),resizable=True,return_keyboard_events=False)         
        self.result = 0
        self.oper =''
        self.window.read(timeout=2)
        for  i in range (1, 5): 
             for button in layout [i]: 
                 button.expand(expand_x=True, expand_y=True)  
        

    def about(self):
           sg.popup('About','Calculadora esta na sua versão 0.5 futuramente  terá atualiçãoes')
    
    def resulter(self):
        if self.oper =='+':
            return int(self.result) + int(self.values['-BOX-'])
        if self.oper =='-':
            return  int(self.result) - int(self.values['-BOX-'])
        if self.oper =='*':
            return int(self.result) * int(self.values['-BOX-'])
        if self.oper =='/':
            return int(self.result) // int(self.values['-BOX-']) 

    def start (self):
        while True:
            event,self.values=self.window.read()

            if event in (None,'Exit',sg.WIN_CLOSED):
                break

            if event in ('About'):
                self.about()

            if event in('-ONE-'):
                if self.values['-BOX-']=='0':
                   self.window['-BOX-'].update(value='1')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'1')

            if event in('-TWO-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='2')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'2')        
            if event in('-THREE-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='3')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'3')
            if event in('-FOUR-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='4')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'4')        
            if event in('-FIVE-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='5')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'5')   
            if event in('-SIX-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='6')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'6')  
            if event in('-SEVEN-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='7')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'7')
            if event in('-EIGHT-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='8')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'8')
            if event in('-NINE-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='9')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'9') 
            if event in('-ZERO-'):
                if self.values['-BOX-']=='0':
                    self.window['-BOX-'].update(value='0')
                else:
                    self.window['-BOX-'].update(value=self.values['-BOX-']+'0')  

            if event in ('-CLEAR-'):
                self.result=0
                self.window['-BOX-'].update(value=self.result)

            if event in ('-BACKARROW-'):
                self.window['-BOX-'].update(value=self.values['-BOX-'][:-1])  

            if event in ('-PLUS-'):
                if self.oper != '':
                   self.result=self.resulter()
                else:
                    self.oper ='+'
                    self.result= self.values['-BOX-'] 
                self.window['-BOX-'].update(value='') 

            if event in('-MINUS-'):
                if self.oper !='':
                    self.result =self.resulter()
                else:
                    self.oper='-'
                    self.result=self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-DIVIDED-'):
                if self.oper!='':
                    self.result=self.values['-BOX-']
                else:
                    self.oper='/'
                    self.result=self.values['-BOX-']
                self.window['-BOX-'].update(value='')

            if event in ('-TIMES-'):
                if self.oper!='':
                    self.result=self.values['-BOX-']
                else:
                    self.oper='*'
                    self.result=self.values['-BOX-']
                self.window['-BOX-'].update(value='')    

            if event in ('-RESULT-'):
                self.result= self.resulter()
                self.window['-BOX-'].update(value=self.result)
                self.result=0
                self.oper=''

Application().start()                




