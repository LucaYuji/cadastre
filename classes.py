from tkinter import *
from tkinter import ttk
root = Tk()
class Application:
    def __init__(self): # posso chamar as funções com o init (metodo construtor)
        self.root = root # Criando a janela
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.treeview_frame2()
        root.mainloop() # Mantendo a janela aberta

    def tela(self):
        self.root.title('Cadastro de Clientes') # Título da janela
        self.root.configure(background='black') # Cor de fundo da janela
        self.root.geometry('700x500') # Dimensão de inicialização da janela (horizontal e vertical)
        self.root.resizable(True,True) # Se eu quero que a janela seja expansiva ou não
        self.root.maxsize(width=900,height=700) # tamanho máximo de expansão
        self.root.minsize(width=500, height=400) # Valores mínimos do tamanho da tela
    # Frames da tela são caixas de separação(áreas de utilização)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg='gray', highlightbackground='white', highlightthickness=3) # bd (), bg = cor do frame, highlightbackground = cor da borda do frame, highlightthickness = largura da borda do frame
        # Place posição em x e y na tela, com porcentagem de tela
        # Pack mais fácil de usar, mas possui menos recursos, não da para colocar em posições especificas
        # Grid transforma em formato de planilha
        self.frame_1.place(relx=0.02,rely=0.02,relwidth= 0.96,relheight=0.46) # relx e rely posição, relwidth e relheight são largura e altura, informações em porcentagem (0 a 1)
        self.frame_2 = Frame(self.root, bg='gray', highlightbackground='white', highlightthickness=3)
        self.frame_2.place(relx=0.02,rely=0.5,relwidth= 0.96,relheight=0.46)
    def widgets_frame1(self):
        # Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text='Limpar',bd= 2, bg='purple',fg='white',font=('verdana', 8, 'bold')) # Criando botão
        self.bt_limpar.place(relx=0.2,rely=0.1,relwidth=0.1,relheight=0.15) # posição e tamanho do botão
        # Criação do botão buscar
        self.bt_limpar = Button(self.frame_1, text='Buscar',bd= 2, bg='purple',fg='white',font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.3,rely=0.1,relwidth=0.1,relheight=0.15)
        # Criação do botão novo
        self.bt_limpar = Button(self.frame_1, text='Novo',bd= 2, bg='purple',fg='white',font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.6,rely=0.1,relwidth=0.1,relheight=0.15)
        # Criação do botão alterar
        self.bt_limpar = Button(self.frame_1, text='Alterar',bd= 2, bg='purple',fg='white',font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.7,rely=0.1,relwidth=0.1,relheight=0.15)
        # Criação do botão apagar
        self.bt_limpar = Button(self.frame_1, text='Apagar',bd= 2, bg='purple',fg='white',font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.8,rely=0.1,relwidth=0.1,relheight=0.15)

        # Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text= 'Código', bg='gray', fg='purple',font=('verdana', 8, 'bold')) # Criando um texto
        self.lb_codigo.place(relx=0.05, rely=0.05) # posição
        #input do tkinter
        self.codigo_entry = Entry(self.frame_1, bg='gray', fg='purple',font=('verdana', 12)) # Criando um input
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08) # posiçãõ e tamanho do input
        # Criação da label e entrada do cliente
        self.lb_cliente = Label(self.frame_1, text= 'Nome', bg='gray', fg='purple',font=('verdana', 8, 'bold'))
        self.lb_cliente.place(relx=0.05, rely=0.35)
        #input do tkinter
        self.cliente_entry = Entry(self.frame_1, bg='gray', fg='purple',font=('verdana', 12))
        self.cliente_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.85)
        # Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text= 'Telefone', bg='gray', fg='purple',font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)
        #input do tkinter
        self.telefone_entry = Entry(self.frame_1, bg='gray', fg='purple',font=('verdana', 12))
        self.telefone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)
        # Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text= 'Cidade', bg='gray', fg='purple',font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6)
        #input do tkinter
        self.cidade_entry = Entry(self.frame_1, bg='gray', fg='purple',font=('verdana', 12))
        self.cidade_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)

    def treeview_frame2(self):
        self.lista = ttk.Treeview(self.frame_2, height= 3, column= ('col1', 'col2', 'col3', 'col4')) # Criando um visualizador
        self.lista.heading('#0', text='') #  (#0 número da coluna)
        self.lista.heading('#1', text='Código')
        self.lista.heading('#2', text='Nome')
        self.lista.heading('#3', text='Telefone')
        self.lista.heading('#4', text='Cidade')

        self.lista.column('#0', width=1) # tamanho de cada item para somatoria = 500
        self.lista.column('#1', width=50)
        self.lista.column('#2', width=200)
        self.lista.column('#3', width=125)
        self.lista.column('#4', width=125)

        self.lista.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85) # posição da lista

        self.scrool_lista = Scrollbar(self.frame_2, orient='vertical')
        self.lista.configure(yscroll=self.scrool_lista.set) # a barra de rolagem pertence a lista
        self.scrool_lista.place(relx=0.96,rely=0.1,relwidth=0.03, relheight=0.85)

Application()
