from tkinter import *
from tkinter import ttk, filedialog, messagebox
from model.warhammer_dao import crear_tabla, borrar_tabla, listar
from model.warhammer_dao import Warhammer, guardar, listar, editar, eliminar


def barra_menu(root):
    barra_menu = Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)

    menu_inicio = Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)

    menu_inicio.add_command(label= 'Crear Registro en BBDD', command = crear_tabla)
    menu_inicio.add_command(label= 'Eliminar Registro en BBDD', command = borrar_tabla)
    menu_inicio.add_command(label= 'Salir', command = root.destroy)

    menu_consultas = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label = "Consultas", menu = menu_consultas)
    menu_consultas.add_command(label = "Búsqueda")
    menu_consultas.add_command(label = "Gráficos")
    menu_consultas.add_command(label = "Estadísticas")

    menu_config = Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label = "Configuración", menu = menu_config)
    menu_config.add_command(label = "Modo Oscuro")
    menu_config.add_command(label = "Modo Claro")
    menu_config.add_command(label= "Pantalla completa")

    menu_help = Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label = "Ayuda", menu = menu_help)
    menu_help.add_command(label = "Ayuda")
    menu_help.add_command(label = "Acerca de")





class Frame(Frame):

    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack()

        self.id_warhammer = None

        self.campos_warhammer()
        self.deshabilitar_campos()
        self.tabla_datos()

    def campos_warhammer(self):

        #ETIQUETAS DE CADA CAMPO
        self.label_nombre = Label(self, text = 'Chema cabron')
        self.label_nombre.config(font = ('Arial', 12))
        self.label_nombre.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.label_army = Label(self, text = 'Ejército')
        self.label_army.config(font = ('Arial', 12))
        self.label_army.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.label_precio = Label(self, text = 'Precio')
        self.label_precio.config(font = ('Arial', 12))
        self.label_precio.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.label_minis = Label(self, text = 'Nº Minis')
        self.label_minis.config(font = ('Arial', 12))
        self.label_minis.grid(row = 3, column = 0, padx = 5, pady = 5)



        #ENTRADAS DE CADA CAMPO

        self.nombre = StringVar()
        self.entrada_nombre = Entry(self, textvariable = self.nombre)
        self.entrada_nombre.config(width = 30, font = ("Arial", 12))
        self.entrada_nombre.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan=2)

        self.army = StringVar()
        self.entrada_army = Entry(self, textvariable = self.army)
        self.entrada_army.config(width = 30, font = ("Arial", 12))
        self.entrada_army.grid(row = 1, column = 1, padx = 5, pady = 5, columnspan=2)

        self.precio = StringVar()
        self.entrada_precio = Entry(self, textvariable = self.precio)
        self.entrada_precio.config(width = 10, font = ("Arial", 12))
        self.entrada_precio.grid(row = 2, column = 1, padx = 5, pady = 5, columnspan=2)

        self.minis = StringVar()
        self.entrada_minis = Entry(self, textvariable = self.minis)
        self.entrada_minis.config(width = 10, font = ("Arial", 12))
        self.entrada_minis.grid(row = 3, column = 1, padx = 5, pady = 5, columnspan=2)

        #BOTONES
        #BOTON NUEVO REGISTRO-------------------------------------------------------------------------
        
        self.boton_new = Button(self, text = 'Nuevo', command = self.habilitar_campos)
        self.boton_new.config(width = 20, font = ('Arial', 12, 'bold'),
            fg = 'black', bg = '#B4F5B0', activebackground = '#5EEF55', cursor = 'hand2')
        self.boton_new.grid(row = 4, column = 0, padx = 5, pady = 5, columnspan=1)
        #---------------------------------------------------------------------------------------------
        
        #BOTON GUARDAR REGISTRO-----------------------------------------------------------------------

        self.boton_save = Button(self, text = 'Guardar', command=self.guardar_datos)
        self.boton_save.config(width = 20, font = ('Arial', 12, 'bold'),
            fg = 'black', bg = '#9FD1F4', activebackground = '#5AB3F0', cursor = 'hand2')
        self.boton_save.grid(row = 4, column = 1, padx = 5, pady = 5, columnspan=1)
        #---------------------------------------------------------------------------------------------

        #BOTON CANCELAR REGISTRO----------------------------------------------------------------------

        self.boton_cancel = Button(self, text = 'Cancelar', command = self.deshabilitar_campos)
        self.boton_cancel.config(width = 20, font = ('Arial', 12, 'bold'),
            fg = 'black', bg = '#F19D8E', activebackground = '#ED6953', cursor = 'hand2')
        self.boton_cancel.grid(row = 4, column = 2, padx = 5, pady = 5, columnspan=1)
        #----------------------------------------------------------------------------------------------

        

    def habilitar_campos(self):

        self.nombre.set('')
        self.army.set('')
        self.precio.set('')
        self.minis.set('')

        self.entrada_nombre.config(state = 'normal', cursor = 'xterm')
        self.entrada_army.config(state = 'normal', cursor = 'xterm')
        self.entrada_precio.config(state = 'normal', cursor = 'xterm')
        self.entrada_minis.config(state = 'normal', cursor = 'xterm')

        self.boton_save.config(state = 'normal', cursor = 'hand2')
        self.boton_cancel.config(state = 'normal', cursor = 'hand2')

    def deshabilitar_campos(self):

        self.nombre.set('')
        self.army.set('')
        self.precio.set('')
        self.minis.set('')

        self.entrada_nombre.config(state = 'disabled', cursor = 'arrow')
        self.entrada_army.config(state = 'disabled', cursor = 'arrow')
        self.entrada_precio.config(state = 'disabled', cursor = 'arrow')
        self.entrada_minis.config(state = 'disabled', cursor = 'arrow')

        self.boton_save.config(state = 'disabled', cursor = 'arrow')
        self.boton_cancel.config(state = 'disabled', cursor = 'arrow')

    def guardar_datos (self):
        warhammer = Warhammer(
            self.nombre.get(),
            self.army.get(),
            self.precio.get(),
            self.minis.get(),
        )
        if self.id_warhammer == None:
            guardar(warhammer)
        else:
            editar(warhammer, self.id_warhammer)
        
        self.tabla_datos()

        self.deshabilitar_campos()

    def tabla_datos(self):

        #Recuperar la lista de peliculas
        self.lista_warhammer = listar()
        self.lista_warhammer.reverse()

        self.tabla = ttk.Treeview(self, 
        column = ('Nombre', 'Ejercito', 'Precio', 'Minis'))
        self.tabla.grid(row = 5, column = 0, columnspan = 3,sticky= 'nse')

        #Scrollbar para la tabla si excede de 10 registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command = self.tabla.yview)
        self.scroll.grid(row = 5, column = 4, sticky= 'nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'Nombre')
        self.tabla.heading('#2', text = 'Ejército')
        self.tabla.heading('#3', text = 'Precio')
        self.tabla.heading('#4', text = 'Nº Minis')

        #Iterar la lista de peliculas
        for i in self.lista_warhammer:


            self.tabla.insert('', 0, text = i[0],
                values = (i[1], i[2], i[3], i[4]))

        #BOTON DE EDITAR

        self.boton_edit = Button(self, text = 'Editar', command = self.editar_datos)
        self.boton_edit.config(width = 10, font = ('Arial', 12, 'bold'),
            fg = 'black', bg = '#EAE19D', activebackground = '#EBDA5E', cursor = 'hand2')
        self.boton_edit.grid(row = 6, column = 0, padx = 5, pady = 5, columnspan=1)

        #BOTON DE ELIMINAR

        self.boton_delete = Button(self, text = 'Eliminar', command = self.eliminar_datos)
        self.boton_delete.config(width = 10, font = ('Arial', 12, 'bold'),
            fg = 'black', bg = '#F1A19A', activebackground = '#E95D52', cursor = 'hand2')
        self.boton_delete.grid(row = 6, column = 1, padx = 5, pady = 5, columnspan=1)

        self.boton_salir = Button(self, text =  'Salir', command = self.root.destroy)
        self.boton_salir.config(width = 25, font = ("Arial", 14, "bold"),
            fg = 'white', bg = '#180403', activebackground= '#D12719', cursor = 'hand2')
        self.boton_salir.grid(row = 6, column = 2, columnspan=1, padx = 10, pady = 10)

    def editar_datos(self):
        try:
            self.id_warhammer = self.tabla.item(self.tabla.selection())['text']
            self.nombre_warhammer = self.tabla.item(self.tabla.selection())['values'][0]
            self.army_warhammer = self.tabla.item(self.tabla.selection())['values'][1]
            self.precio_warhammer = self.tabla.item(self.tabla.selection())['values'][2]
            self.minis_warhammer = self.tabla.item(self.tabla.selection())['values'][3]

            self.habilitar_campos()

            self.entrada_nombre.insert(0, self.nombre_warhammer)
            self.entrada_army.insert(0, self.army_warhammer)
            self.entrada_precio.insert(0, self.precio_warhammer)
            self.entrada_minis.insert(0, self.minis_warhammer)



        except:
            titulo = 'Edicion de datos'
            msg = 'No se ha seleccionado ningún registro'
            messagebox.showerror(titulo, msg)

    def eliminar_datos(self):
        try:
            self.id_warhammer = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_warhammer)

            self.tabla_datos()
            self.id_warhammer = None
        except:
            titulo = 'Eliminar un registro'
            msg = 'No se ha seleccionado ningún registro'
            messagebox.showerror(titulo, msg)




    
















