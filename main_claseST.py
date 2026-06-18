import sys
import re

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem
)

from GUI.vtn_principal import Ui_MainWindow


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Fecha actual automática
        self.ui.dtfecha.setDate(QDate.currentDate())

        # Configurar tabla
        self.ui.tbldatos.setColumnCount(4)
        self.ui.tbldatos.setHorizontalHeaderLabels(
            ["Código", "Nombre", "Fecha", "Email"]
        )

        # Conectar botones
        self.ui.btnguardar.clicked.connect(self.guardar)
        self.ui.btnlimpiar.clicked.connect(self.eliminar_registro)

        # Cargar registros existentes
        self.cargar_registros()

    def guardar(self):

        codigo = self.ui.txtcodigo.text().strip()
        nombre = self.ui.txtnombre.text().strip()
        fecha = self.ui.dtfecha.text()
        email = self.ui.txtemail.text().strip()

        # VALIDAR VACÍOS
        if not codigo or not nombre or not email:
            QMessageBox.warning(
                self,
                "Error",
                "Todos los campos son obligatorios."
            )
            return

        # VALIDAR CÓDIGO
        if not codigo.isdigit():
            QMessageBox.warning(
                self,
                "Error",
                "El código solo debe contener números."
            )
            return

        if len(codigo) != 5:
            QMessageBox.warning(
                self,
                "Error",
                "El código debe tener exactamente 5 dígitos."
            )
            return

        # VALIDAR NOMBRE
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre):
            QMessageBox.warning(
                self,
                "Error",
                "El nombre solo debe contener letras."
            )
            return

        # VALIDAR EMAIL
        patron_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron_email, email):
            QMessageBox.warning(
                self,
                "Correo inválido",
                "Ingrese un correo electrónico válido."
            )
            return

        # GUARDAR EN ARCHIVO
        with open("registros.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{codigo}|{nombre}|{fecha}|{email}\n"
            )

        # MOSTRAR EN TABLA
        fila = self.ui.tbldatos.rowCount()

        self.ui.tbldatos.insertRow(fila)

        self.ui.tbldatos.setItem(
            fila, 0, QTableWidgetItem(codigo)
        )

        self.ui.tbldatos.setItem(
            fila, 1, QTableWidgetItem(nombre)
        )

        self.ui.tbldatos.setItem(
            fila, 2, QTableWidgetItem(fecha)
        )

        self.ui.tbldatos.setItem(
            fila, 3, QTableWidgetItem(email)
        )

        QMessageBox.information(
            self,
            "Guardado",
            "Registro guardado correctamente."
        )

        self.limpiar_campos()

    def limpiar_campos(self):

        self.ui.txtcodigo.clear()
        self.ui.txtnombre.clear()
        self.ui.txtemail.clear()

        self.ui.txtcodigo.setFocus()

    def eliminar_registro(self):

        fila = self.ui.tbldatos.currentRow()

        if fila < 0:
            QMessageBox.warning(
                self,
                "Aviso",
                "Seleccione una fila para eliminar."
            )
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar",
            "¿Desea eliminar el registro seleccionado?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:

            self.ui.tbldatos.removeRow(fila)

            self.actualizar_archivo()

            QMessageBox.information(
                self,
                "Eliminado",
                "Registro eliminado correctamente."
            )

    def actualizar_archivo(self):

        with open("registros.txt", "w", encoding="utf-8") as archivo:

            for fila in range(self.ui.tbldatos.rowCount()):

                codigo = self.ui.tbldatos.item(fila, 0).text()
                nombre = self.ui.tbldatos.item(fila, 1).text()
                fecha = self.ui.tbldatos.item(fila, 2).text()
                email = self.ui.tbldatos.item(fila, 3).text()

                archivo.write(
                    f"{codigo}|{nombre}|{fecha}|{email}\n"
                )

    def cargar_registros(self):

        try:

            with open("registros.txt", "r", encoding="utf-8") as archivo:

                for linea in archivo:

                    datos = linea.strip().split("|")

                    if len(datos) == 4:

                        fila = self.ui.tbldatos.rowCount()

                        self.ui.tbldatos.insertRow(fila)

                        for columna, dato in enumerate(datos):

                            self.ui.tbldatos.setItem(
                                fila,
                                columna,
                                QTableWidgetItem(dato)
                            )

        except FileNotFoundError:
            pass


if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = VentanaPrincipal()
    ventana.show()

    sys.exit(app.exec())