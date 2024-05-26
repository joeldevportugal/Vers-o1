# importar as Bibliotecas a Usar -----------------------------------------------------------
from tkinter import *
from tkinter import messagebox
import pyperclip
import threading
#-------------------------------------------------------------------------------------------

# Implementar Todo O Backend----------------------------------------------------------------
def atualiza_cor(event=None):
    # Obtém os valores dos sliders
    r = Svermelho.get()
    g = Sverde.get()
    b = SAzul.get()
    # Formata como uma string hexadecimal
    hex_color = f'#{r:02x}{g:02x}{b:02x}'
    # Atualiza o background do Label e o conteúdo da Entry
    Lcor.config(bg=hex_color)
    Ehexa.delete(0, 'end')
    Ehexa.insert(0, hex_color)

def copiar_hex():
    hex_color = Ehexa.get()
    pyperclip.copy(hex_color)
    messagebox.showinfo('Copiar', 'Codigo Copiado com Sucesso para a Aréa de Traferençia!')

def Limpar():
     # Define a cor preta diretamente
    Svermelho.set(0)
    Sverde.set(0)
    SAzul.set(0)
    atualiza_cor()
    # Limpa o conteúdo da entrada Ehexa
    Ehexa.delete(0, 'end')
    Ehexa.insert(0, 'hex_color')
    Lcor.config(bg='black')
    messagebox.showinfo('LIMPAR','Seus dados Foram Limpos Com Sucesso')

def Sair ():
    resposta=messagebox.askyesno('SAIR', 'Deseja Sair do Programa ?')
    if resposta: 
        janela.quit()
#------------------------------------------------------------------------------------------
# defenir Cores ------------------------------------------------------
Co0="#ffffff" # cor branca Para Janela 
co1 ="#ffce6a" # Cor Laranja Botões 
co2 ="#fffcee" # cor fundo Ehexa Amarelo Claro
#--------------------------------------------------------------------
# configurar a Nossa Janela ---------------------------------------------------------------
janela = Tk()
janela.geometry('744x670+100+100')
janela.resizable(False, False)
janela.title('Selector Versão devJoel Portugal 2024 ©')
janela.config(bg=Co0)
janela.iconbitmap('C:\\Users\\HP\\Desktop\\Python tkinter\\Selector versões\\Versão 1\\Icon\\icon.ico')
#------------------------------------------------------------------------------------------
# implementar O fronte End --------------------------------------------
# criar a Label Painel 
Lcor = Label(janela, bg='Black', width=102, height=25)
Lcor.place(x=10, y=10)

# criar Labels de Control mas Scales 
LVermelho = Label(janela, text='Vermelho', font=('arial 12'), bg=Co0)
LVermelho.place(x=10, y=400)
Svermelho = Scale(janela, orient='horizontal', length=690, from_=0, to=255, command=atualiza_cor, bg=Co0)
Svermelho.place(x=10, y=420)
LVerde = Label(janela, text='Verde', font=('arial 12'), bg=Co0)
LVerde.place(x=10, y=470)
Sverde = Scale(janela, orient='horizontal', length=690, from_=0, to=255, command=atualiza_cor, bg=Co0)
Sverde.place(x=10, y=495)
LAzul = Label(janela, text='Azul', font=('arial 12'), bg=Co0)
LAzul.place(x=10, y=545)
SAzul = Scale(janela, orient='horizontal', length=690, from_=0, to=255, command=atualiza_cor, bg=Co0)
SAzul.place(x=10, y=565)

# criar a Entry onde fica O codigo Hexadecimal 
Ehexa = Entry(janela, font=('arial 14'), width=10, bg=co2)
Ehexa.place(x=10,y=625)
# Criar os Botões Copiar Limpar e Sair
BtnCopiar = Button(janela, text='Copiar', font=('arial 12'),relief=RAISED, overrelief=RIDGE, command=copiar_hex, bg=co1)
BtnCopiar.place(x=130, y=625)
BtnLimpar = Button(janela, text='Limpar', font=('arial 12'),relief=RAISED, overrelief=RIDGE, command=Limpar, bg=co1)
BtnLimpar.place(x=195, y=625)
BtnSair = Button(janela, text='Fechar Aplicação', font=('arial 12'),relief=RAISED, overrelief=RIDGE, command=Sair, bg=co1)
BtnSair.place(x=260, y=625)

#-----------------------------------------------------------------------
janela.mainloop()