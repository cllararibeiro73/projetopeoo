from tkinter import *
import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS clientes (nome text, email text, curso text)')

class VendeCursos():
    def __init__(self):
        self.janela = Tk()
        self.janela.geometry("900x500")
        self.janela.title("venda de cursos")
        self.janela.resizable(0, 0)
        self.janela.configure(background="blue")


        self.conteiner1 = Canvas(self.janela, bg="black", height=500, width=400, borderwidth=0, highlightthickness=0)
        self.conteiner1.place(x=0, y=0)
        self.labelcursos = Label(self.conteiner1, bg="green", fg="white", text="CURSOS:", height=2, width=29, font=("Arial", 18), justify="center")
        self.labelcursos.place(x=0, y=0)

        self.imagempy = PhotoImage(file="imagens/pythonlogo2.png")
        

        self.conteinerpy = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinerpy.place(x=40, y=100)


        self.conteinerpy.create_image(44, 41, image=self.imagempy)


        self.imagemjs = PhotoImage(file="imagens/"+"javascriptlogo"+".png").subsample(11)
      


        self.conteinerjs = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinerjs.place(x=40, y=220)

        self.conteinerjs.create_image(30, 30, image=self.imagemjs)


        self.imagemcmais = PhotoImage(file="imagens/c++logo.png").subsample(18)

        self.conteinercmais = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinercmais.place(x=160, y=100)

        self.conteinercmais.create_image(40, 40, image=self.imagemcmais)



        self.imagemjava = PhotoImage(file="imagens/javalogo.png").subsample(2)

        self.conteinerjava = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinerjava.place(x=160, y=220)

        self.conteinerjava.create_image(40, 40, image=self.imagemjava)



        self.imagemcsharp = PhotoImage(file="imagens/csharplogo.png").subsample(3)

        self.conteinercsharp = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinercsharp.place(x=280, y=220)

        self.conteinercsharp.create_image(40, 40, image=self.imagemcsharp)



        self.imagemphp = PhotoImage(file="imagens/phplogo.png").subsample(4)
        self.conteinerphp = Canvas(self.conteiner1, height=80, width=80, borderwidth=0, highlightthickness=0)
        self.conteinerphp.place(x=280, y=100)

        self.conteinerphp.create_image(40, 40, image=self.imagemphp)


        self.botao_maisvendido = Button(self.conteiner1, bg="blue", fg="white", height=1, width=20, text="Curso mais vendido", font=("Arial", 16), justify="center",command=self.exibirMaisVendido)
        self.botao_maisvendido.place(x=70, y=360)
        self.labelmais= Label(self.janela, text="", background="black", fg="white", height=5, width=35, justify="center", font=("Arial", 12))
        self.labelmais.place(x=30, y=400)


        self.labelcompra = Label(self.janela, text="COMPRA:", background="purple", fg="white", height=3, width=35, justify="center", font=("Arial", 16))
        self.labelcompra.place(x=440, y=20)

        self.labelnome = Label(self.janela, text="NOME:", background="orange", fg="white", height=2, width=10, font=("Arial", 14))
        self.labelnome.place(x=420, y=120)

        self.entrynome = Entry(self.janela, font=("Arial", 20))
        self.entrynome.place(x=560, y=125)

        self.labelemail = Label(self.janela, text="EMAIL:", background="orange", fg="white", height=2, width=10, font=("Arial", 14))
        self.labelemail.place(x=420, y=190)

        self.entryemail = Entry(self.janela, font=("Arial", 20))
        self.entryemail.place(x=560, y=195)

        self.labelcurso = Label(self.janela, text="CURSO:", background="orange", fg="white", height=2, width=10, font=("Arial", 14))
        self.labelcurso.place(x=420, y=260)
        self.entrycurso = Entry(self.janela, font=("Arial", 20))
        self.entrycurso.place(x=560, y=265)
        
        self.labelpreco = Label(self.janela, text="PREÇO:", background="orange", fg="white", height=2, width=10, font=("Arial", 14))
        self.labelpreco.place(x=420, y=330)
        self.entrypreco = Entry(self.janela, font=("Arial", 20))
        self.entrypreco.place(x=560, y=335)
        
        self.botao_selecionarjs = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarjs)
        self.botao_selecionarjs.place(x=43, y=305)
        
        self.botao_selecionarpy = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarpy)
        self.botao_selecionarpy.place(x=43, y=185)

        self.botao_selecionarcsharp = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarcsharp)
        self.botao_selecionarcsharp.place(x=283, y=305)

        self.botao_selecionarc = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarc)
        self.botao_selecionarc.place(x=163, y=185)

        self.botao_selecionarphp = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarphp)
        self.botao_selecionarphp.place(x=283, y=185)

        self.botao_selecionarjava = Button(self.conteiner1, bg="green", fg="white", height=1, width=8, text="selecionar", font=("Arial", 10), justify="center", command=self.selecionarjava)
        self.botao_selecionarjava.place(x=163, y=305)

        self.botao_comprar = Button(self.janela, bg="green", fg="white", height=1, text="comprar", font=("Arial", 16), justify="center", command = self.comprar)
        self.botao_comprar.place(x=500, y=400)

        self.botao_cancelar = Button(self.janela, bg="red", fg="white", height=1, text="cancelar compra", font=("Arial", 16), justify="center", command = self.cancelar)
        self.botao_cancelar.place(x=630, y=400)

        self.labelfim = Label(self.janela, text="", background="blue", fg="white", height=1, width=20, font=("Arial", 14))
        self.labelfim.place(x=530, y=450)

        self.janela.mainloop()

    def preenche_cursopreco(self, nome_curso,valor_preco):
        self.entrycurso.insert(0, nome_curso)
        self.entrypreco.insert(0, valor_preco)

    def selecionarpy(self):
        self.preenche_cursopreco('Python',150.00)

    def selecionarc(self):
        self.preenche_cursopreco('C++',120.00)

    def selecionarphp(self):
        self.preenche_cursopreco('PHP',89.90)

    def selecionarjs(self):
        self.preenche_cursopreco('JavaScript',250.50)

    def selecionarjava(self):
        self.preenche_cursopreco('Java',350.00)

    def selecionarcsharp(self):
        self.preenche_cursopreco('C-Sharp',136.80)
    

    #coloca no botao comprar
    def comprar(self):
        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()
        cursor.execute('INSERT INTO clientes (nome,email,curso) VALUES (?,?,?)',(self.entrynome.get(),self.entryemail.get(),self.entrycurso.get()))
        banco.commit()
        banco.close()
        self.labelfim.config(text="Compra realizada")

    def cancelar(self):
        banco = sqlite3.connect('banco.db')
        cursor = banco.cursor()
        cursor.execute('SELECT * FROM clientes WHERE email = ?', (self.entryemail.get(),))
        cliente = cursor.fetchone()
        print(cliente)  
        if cliente:
            cursor.execute('DELETE FROM clientes WHERE email = ?',(self.entryemail.get(),))
            banco.commit()
            banco.close()
            self.labelfim.config(text="Compra cancelada!")
        else:
            self.labelfim.config(text="Registro não encontrado.")
        
    def exibirMaisVendido(self):
        cursor.execute('SELECT curso FROM clientes')
        todos = cursor.fetchall()
        qtdPython = 0
        qtdjava = 0
        qtdc = 0
        qtdcsharp = 0
        qtdphp = 0
        qtdjavascript = 0
        for curso in todos:
            if curso[0] == 'Python':
                qtdPython += 1
        print(qtdPython)
        for curso in todos:
            if curso[0] == 'C++':
                qtdc+= 1
        print(qtdc)
        for curso in todos:
            if curso[0] == 'C-Sharp':
                qtdcsharp += 1
        print(qtdcsharp)
        for curso in todos:
            if curso[0] == 'PHP':
                qtphp += 1
        print(qtdphp)
        for curso in todos:
            if curso[0] == 'Java':
                qtdjava += 1
        print(qtdjava)
        for curso in todos:
            if curso[0] == 'JavaScript':
                qtdjavascript += 1
        print(qtdjavascript)
        self.labelmais.config(text=f"Python: {qtdPython}\nC++: {qtdc}\nPHP: {qtdphp}\nJavaScript: {qtdjavascript}\nJava: {qtdjava}C-Sharp: {qtdcsharp}")
        
app = VendeCursos()