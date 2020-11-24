from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from repositorio_particula.particulas import Particulas
from repositorio_particula.particula import Particula
from repositorio_particula.algoritmos import distancia_euclidiana
from PySide2.QtGui import QPen, QColor, QTransform
from random import randint



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.particulas = Particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

        self.ui.actionId.triggered.connect(self.action_ordenar_id)
        self.ui.actionDistancia.triggered.connect(self.action_ordenar_distancia)
        self.ui.actionVelocidad.triggered.connect(self.action_ordenar_velocidad)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)
    
    @Slot()
    def action_ordenar_id(self):
        self.particulas.ordenar_id()
    @Slot()
    def action_ordenar_distancia(self):
        self.particulas.ordenar_distancia()
    @Slot()
    def action_ordenar_velocidad(self):
        self.particulas.ordenar_velocidad()

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2,1.2)
        else:
            self.ui.graphicsView.scale(0.8,0.8)

    @Slot()
    def dibujar(self):
        for Particula in self.particulas:
            print('dibujar')

            pen = QPen()
            pen.setWidth(2)

            red = Particula.red
            green = Particula.green
            blue = Particula.blue

            color = QColor(red, green, blue)
            pen.setColor(color)
                
            self.scene.addEllipse(Particula.origen_x, Particula.origen_y, 6,6, pen)
            self.scene.addEllipse(Particula.destino_x, Particula.destino_y,6,6, pen)
            self.scene.addLine(Particula.origen_x + 3, Particula.origen_y + 3, Particula.destino_x + 3, Particula.destino_y + 3, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()


    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text()
        encontrado = False
        for particula in self.particulas:
            if id == particula.id:
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(particula.id)
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(particula.velocidad)
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue)) 
                distancia_euclidiana_widget = QTableWidgetItem(str(particula.distancia_euclidiana))

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_euclidiana_widget)

                encontrado = True
                return 
        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",
                f'La particula con ID "{id}" no fue encontrada'
            )
        
        


    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        headers = ["ID", "Origen x", "Origen y", "Destino x", "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.particulas))

        row=0
        for particula in self.particulas:
           id_widget = QTableWidgetItem(particula.id)
           origen_x_widget = QTableWidgetItem(str(particula.origen_x))
           origen_y_widget = QTableWidgetItem(str(particula.origen_y))
           destino_x_widget = QTableWidgetItem(str(particula.destino_x))
           destino_y_widget = QTableWidgetItem(str(particula.destino_y))
           velocidad_widget = QTableWidgetItem(particula.velocidad)
           red_widget = QTableWidgetItem(str(particula.red))
           green_widget = QTableWidgetItem(str(particula.green))
           blue_widget = QTableWidgetItem(str(particula.blue))
           distancia_euclidiana_widget = QTableWidgetItem(str(particula.distancia_euclidiana)) 

           self.ui.tabla.setItem(row, 0, id_widget)
           self.ui.tabla.setItem(row, 1, origen_x_widget)
           self.ui.tabla.setItem(row, 2, origen_y_widget)
           self.ui.tabla.setItem(row, 3, destino_x_widget)
           self.ui.tabla.setItem(row, 4, destino_y_widget)
           self.ui.tabla.setItem(row, 5, velocidad_widget)
           self.ui.tabla.setItem(row, 6, red_widget)
           self.ui.tabla.setItem(row, 7, green_widget)
           self.ui.tabla.setItem(row, 8, blue_widget)
           self.ui.tabla.setItem(row, 9, distancia_euclidiana_widget)

           row += 1

    @Slot()
    def action_abrir_archivo(self):
        #print('abrir_archivo')
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        #print('guardar_archivo')
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        print(ubicacion)
        if self.particulas.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo crear el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo " + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        #self.particulas.mostrar()
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.particulas))

    @Slot()
    def click_agregar(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_final(particula)

        #print(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        #self.ui.salida.insertPlainText(id + str(origen_x) + str(origen_y) + str(destino_x) + str(destino_y) + velocidad + str(red) + str(green) + str(blue))
    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.origenx_spinBox.value()
        origen_y = self.ui.origeny_spinBox.value()
        destino_x = self.ui.destinox_spinBox.value()
        destino_y = self.ui.destinoy_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()

        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.particulas.agregar_inicio(particula)