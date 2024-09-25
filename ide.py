#                ______________________________ 
#_______________/ Bibliotecas 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton, QLabel, QAction, QFileDialog, QMessageBox, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPainter, QColor

from analizador_lexico import analizador_lexico
from analizador_sintactico import analizador_sintactico


#                ______________________________ 
#_______________/ Área para el número de línea 
class LineNumberArea(QWidget):

    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor


    def sizeHint(self):
        return QSize(self.editor.lineNumberAreaWidth(), 0)


    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)


#                ______________________________ 
#_______________/ Funcionaliadades para el área de número de línea
class CodeEditor(QPlainTextEdit):

    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)

        self.updateLineNumberAreaWidth(0)


    def lineNumberAreaWidth(self):
        fixed_width = 30  # Ancho fijo del aréa de numero de línea
        return fixed_width


    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)


    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)


    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))


    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)

        painter.setPen(QColor(Qt.white))

        right_edge = event.rect().right()
        painter.drawLine(right_edge - 1, event.rect().top(), right_edge - 1, event.rect().bottom())

        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(), Qt.AlignLeft, number)
                
            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            block_number += 1

class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Ventana")
        self.setGeometry(150, 150, 400, 300)

        # Agrega un label o cualquier widget que desees en la nueva ventana
        label = QLabel("Esta es una nueva ventana.", self)
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

class IDE(QMainWindow):

    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Writing Machine IDE")
        self.setGeometry(100, 100, 800, 600)

        # Cargar el archivo de estilo
        with open("style.qss", "r") as file:
            self.setStyleSheet(file.read())

        # Crear el editor de código
        self.editor = CodeEditor()
        self.editor.setPlaceholderText("Escribe tu código aquí...")

        # Crear el panel de salida
        self.output_panel = QPlainTextEdit()
        self.output_panel.setReadOnly(True)
        self.output_panel.setPlaceholderText("...")

        # Crear el botón de compilar
        self.compile_button = QPushButton("Compilar")
        self.compile_button.clicked.connect(self.compile_code)
        self.compile_button.setFixedSize(100, 25)
        self.compile_button.setEnabled(False)
        self.compile_button.setStyleSheet("QPushButton:disabled { background-color: #444; color: #888; }")

        # Crear el botón para abrir la nueva ventana
        self.run_button = QPushButton("Run code")
        self.run_button.setFixedSize(100, 25)
        self.run_button.clicked.connect(self.open_new_window)
        self.run_button.setEnabled(False)
        self.run_button.setStyleSheet("QPushButton:disabled { background-color: #444; color: #888; }")

        # Configurar la barra de menú
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Archivo")

        open_action = QAction("Abrir archivo", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        new_action = QAction("Nuevo archivo", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        save_action = QAction("Guardar archivo", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        close_action = QAction("Cerrar IDE", self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        # Crear el layout principal
        main_layout = QVBoxLayout()

        # Crear un layout horizontal para el menú y los botones
        menu_button_layout = QHBoxLayout()
        menu_button_layout.addWidget(menubar)  # Añadir la barra de menú al layout
        menu_button_layout.addStretch()  
        menu_button_layout.addWidget(self.run_button)  # Añadir el botón de nueva ventana
        menu_button_layout.addWidget(self.compile_button)  # Añadir el botón de compilar al layout

        main_layout.addLayout(menu_button_layout)  # Añadir el layout de menú y botón

        # Configurar el diseño principal
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.output_panel)

        main_layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.current_file = None
        self.tree_window_opened = False

    def open_new_window(self):
        if not self.tree_window_opened:  # Solo abrir si no hay ventana abierta
            self.tree_window = NewWindow()
            self.tree_window.show()
            self.tree_window_opened = True  # Marcar la ventana como abierta
            self.tree_window.closeEvent = self.close_new_window  # Asignar evento de cierre

    def close_new_window(self, event):
        self.tree_window_opened = False  # Marcar la ventana como cerrada
        event.accept()


    def compile_code(self):
        self.output_panel.appendPlainText("Compilando el código...")
        self.run_button.setEnabled(True)  # Habilitar el botón de nueva ventana al compilar


    #       _________________________________
    #______/ Funcionalidad: Nuevo archivo... \______ 
    def new_file(self):
        self.editor.clear()  # Limpiar el editor
        self.setWindowTitle("Writing Machine IDE - Nuevo Archivo")  # Actualizar el título
        self.current_file = None  # Reiniciar el archivo actual
        self.compile_button.setEnabled(False)  # Deshabilitar el botón de compilar
        self.run_button.setEnabled(False)  # Deshabilitar el botón de nueva ventana al crear un nuevo archivo


    #       ___________________________
    #______/ Funcionalidad: Guardar... y Guardar como... \______ 
    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, 'w') as file:
                    file.write(self.editor.toPlainText())
                self.compile_button.setEnabled(True)  # Habilitar el botón de compilar al guardar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")
        else:
            self.save_file_as()  # Si no hay archivo actual, llamar a "guardar como"

    def save_file_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Archivos de código (*.wmce);;Todos los archivos (*)", options=options)

        if file_name:
            if not file_name.endswith('.wmce'):
                file_name += '.wmce'

            try:
                with open(file_name, 'w') as file:
                    file.write(self.editor.toPlainText())
                self.current_file = file_name  # Actualizar la variable del archivo actual
                self.setWindowTitle(f"Writing Machine IDE - {file_name}")  # Actualizar el título de la ventana
                self.compile_button.setEnabled(True)  # Habilitar el botón de compilar al guardar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")


    #       _________________________
    #______/ Funcionalidad: Abrir... \______ 
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de código (*.wmce);;Todos los archivos (*)", options=options)

        if file_name:
            with open(file_name, 'r') as file:
                self.editor.setPlainText(file.read())

            self.setWindowTitle(f"Writing Machine IDE - {file_name}")   # Actualizar el título de la ventana con el nombre del archivo
            self.current_file = file_name  # Actualizar el archivo actual
            self.compile_button.setEnabled(True)  # Habilitar el botón de compilar al abrir un archivo


    #       ____________________________
    #______/ Funcionalidad: Compilar... \______ 
    def compile_code(self):
        self.run_button.setEnabled(True)
        cadena = self.editor.toPlainText()
        self.output_panel.clear()
        print(cadena)
        if cadena != "":
            lista = analizador_lexico(cadena)
            analizador_sintactico(cadena)
        #return lista


def main():
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
