from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QApplication, QListWidget, QFileDialog
import os
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.filename = None
        self.dir = None
        self.save_dir = "/Сохранённые фото"
 
    def loadimage(self, filename):
        self.filename = filename
        image_path = os.path.join(workdir, self.filename)
        self.image = Image.open(image_path)


    def showimage(self, path):
        nadpis.hide()
        pixmap = QPixmap(path)
        w, h = nadpis.width(), nadpis.height()
        piximage = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        nadpis.setPixmap(piximage)
        nadpis.show()

    def saveImage(self):
        path = os.path.join(workdir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_bw(self):
        if self.image != None:
            self.image = self.image.convert("L")
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showimage(image_path)

    def rotate(self):
        if self.image != None:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showimage(image_path)

    def rotate2(self):
        if self.image != None:
            self.image = self.image.transpose(Image.ROTATE_270)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showimage(image_path)

    def flip(self):
        if self.image != None:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showimage(image_path)

    def sharp(self):
        if self.image != None:
            self.image = self.image.transpose(Image.sharpness)
            self.saveImage()
            image_path = os.path.join(workdir, self.save_dir, self.filename)
            self.showimage(image_path)




app = QApplication([])
main = QWidget()
main.setWindowTitle("Easy Editor")
main.resize(500, 450)

papka = QPushButton("Папка")

spisok = QListWidget()

nadpis = QLabel("Картинка")

button1 = QPushButton("Влево")
button2 = QPushButton("Вправо")
button3 = QPushButton("Отзеркалить")
button4 = QPushButton("Резкость")
button5 = QPushButton("Ч/Б")

main_lile = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()

v_line1.addWidget(papka)
v_line1.addWidget(spisok)

h_line1.addWidget(button1)
h_line1.addWidget(button2)
h_line1.addWidget(button3)
h_line1.addWidget(button4)
h_line1.addWidget(button5)

v_line2.addWidget(nadpis)
v_line2.addLayout(h_line1)

h_line2.addLayout(v_line1)
h_line2.addLayout(v_line2)

main.setLayout(h_line2)

workdir = ""
ImageProcessor = ImageProcessor()
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(filenames, es):
    result = []
    for name in filenames:
        for e in es:
            if name.endswith(e):
                result.append(name)
    return result

def show():
    chooseWorkdir()
    es = [".png", ".jpg", ".jpeg", ".bnp"]
    filenames = os.listdir(workdir)
    result = filter(filenames, es)
    spisok.clear()
    for name in result:
        spisok.addItem(name)

papka.clicked.connect(show)

def showImage():
    if spisok.currentRow() >= 0 :
        filename = spisok.currentItem().text()
        ImageProcessor.loadimage(filename)
        image_path = os.path.join(workdir, filename)
        ImageProcessor.showimage(image_path)

spisok.currentRowChanged.connect(showImage)

button5.clicked.connect(ImageProcessor.do_bw)

button1.clicked.connect(ImageProcessor.rotate)

button2.clicked.connect(ImageProcessor.rotate2)

button3.clicked.connect(ImageProcessor.flip)

button4.clicked.connect(ImageProcessor.sharp)



main.show()
app.exec()