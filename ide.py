#                ______________________________ 
#_______________/ Bibliotecas 
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget, QPushButton, QMenuBar, QMenu, QAction, QFileDialog, QMessageBox, QHBoxLayout, QSplitter
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPainter, QColor


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


class IDE(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal
        self.setWindowTitle("Custom IDE")
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
        self.output_panel.setPlaceholderText("Mensajes de compilación...")

        # Crear el botón de compilar
        self.compile_button = QPushButton("Compilar")
        self.compile_button.clicked.connect(self.compile_code)
        self.compile_button.setFixedSize(100, 25)
        self.compile_button.setEnabled(False)  # Deshabilitar el botón inicialmente

        # Configurar la barra de menú
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Archivo")

        open_action = QAction("Abrir", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        new_action = QAction("Nuevo", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        save_action = QAction("Guardar", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        close_action = QAction("Cerrar", self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        # Crear el layout principal
        main_layout = QVBoxLayout()

        # Crear un layout horizontal para el menú y el botón
        menu_button_layout = QHBoxLayout()
        menu_button_layout.addWidget(menubar)  # Añadir la barra de menú al layout
        menu_button_layout.addStretch()  # Espacio flexible
        menu_button_layout.addWidget(self.compile_button)  # Añadir el botón al layout

        main_layout.addLayout(menu_button_layout)  # Añadir el layout de menú y botón

        # Configurar el diseño principal
        splitter = QSplitter(Qt.Vertical)
        splitter.addWidget(self.editor)
        splitter.addWidget(self.output_panel)

        main_layout.addWidget(splitter)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Inicializar la variable del archivo actual
        self.current_file = None

    #       _________________________________
    #______/ Funcionalidad: Nuevo archivo... \______ 
    def new_file(self):
        self.editor.clear()  # Limpiar el editor
        self.setWindowTitle("Custom IDE - Nuevo Archivo")  # Actualizar el título
        self.current_file = None  # Reiniciar el archivo actual
        self.compile_button.setEnabled(False)  # Deshabilitar el botón de compilar

    #       ___________________________
    #______/ Funcionalidad: Guardar... \______ 
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

    #       ________________________________
    #______/ Funcionalidad: Guardar como... \______ 
    def save_file_as(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Guardar archivo como", "", "Archivos de código (*.mycode);;Todos los archivos (*)", options=options)

        if file_name:
            if not file_name.endswith('.mycode'):
                file_name += '.mycode'

            try:
                with open(file_name, 'w') as file:
                    file.write(self.editor.toPlainText())
                self.current_file = file_name  # Actualizar la variable del archivo actual
                self.setWindowTitle(f"Custom IDE - {file_name}")  # Actualizar el título de la ventana
                self.compile_button.setEnabled(True)  # Habilitar el botón de compilar al guardar
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")

    #       _________________________
    #______/ Funcionalidad: Abrir... \______ 
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de código (*.mycode);;Todos los archivos (*)", options=options)

        if file_name:
            with open(file_name, 'r') as file:
                self.editor.setPlainText(file.read())

            # Actualizar el título de la ventana con el nombre del archivo
            self.setWindowTitle(f"Custom IDE - {file_name}")
            self.current_file = file_name  # Actualizar el archivo actual
            self.compile_button.setEnabled(True)  # Habilitar el botón de compilar al abrir un archivo

    #       ____________________________
    #______/ Funcionalidad: Compilar... \______ 
    def compile_code(self):
        self.output_panel.appendPlainText("Compilando el código...")



def main():
    app = QApplication(sys.argv)
    ide = IDE()
    ide.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


# Faltantes actuales:
# Incorporar boton para el arbol
# Cambiar colo de boton a blanco cuando esta desabilitado


# Faltantes opcionales:
# 1x Validacion de archivo guardado para ejecutar o compilar
# 2xx Cambiar logo de la ventana a otro
# 2xx Cambiar logo del navegador si se puede y hacer exe
# 2xx Mas personalizacion
# 2xx Funcion de cerrar un archivo existente y mantenerme en el ide (puede incluir el guardar un archivo si no se ha hecho)