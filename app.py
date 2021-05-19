import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
from PyQt5.QtPrintSupport import *
import googletrans
import speech_recognition as sr
import gtts
from playsound import playsound

class Translator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Translator")
        # self.setWindowFlags(Qt.CustomizeWindowHint)

        self.setWindowIcon(QIcon(os.path.join("VisualElements", "VisualElements_512.svg")))

        self.setFixedWidth(863)
        self.setFixedHeight(606)

        self.widget = QWidget(self)
        self.widget.move(2000,2000)
        self.layout = QVBoxLayout(self.widget)

        self.input  =QTextEdit(self)
        self.input.move(10,40)
        self.input.textChanged.connect(self.Translate)
        self.input.setStyleSheet("border-radius : 1px")
        self.input.setFont(QFont("Calibri", 12))
        self.input.resize(415,520)

        self.output  = QTextBrowser(self)
        self.output.setStyleSheet("background-color : #f9f9f9; border-radius : 1px")
        self.output.setFontPointSize(10)
        self.output.move(435,40)
        self.output.resize(420,520)

        self.ToolBarTop = QToolBar(self)
        self.ToolBarTop.setMovable(False)
        self.ToolBarTop.setIconSize(QSize(45,45))
        self.addToolBar(Qt.TopToolBarArea, self.ToolBarTop)

        self.Select_Language_Output = QComboBox()
        self.Select_Language_Output.addItems(["Default(Tamil)", "English", "Hindi"])
        self.Select_Language_Output.activated.connect(self.Translate)
        self.Select_Language_Output.move(519,15)
        self.Select_Language_Output.setFont(QFont("Calibri", 10))
        self.ToolBarTop.addWidget(self.Select_Language_Output)

        self.ToolBarBottom = QToolBar(self)
        self.ToolBarBottom.setStyleSheet("background-color : white; color : #7d7d7d; border-radius : 1px")
        self.ToolBarBottom.setMovable(False)
        self.ToolBarBottom.setIconSize(QSize(35,35))
        self.addToolBar(Qt.BottomToolBarArea, self.ToolBarBottom)

        self.Voice_Speech = QAction(QIcon(os.path.join("assests", "microphone-logo.png")), "Voice", self)
        self.Voice_Speech.triggered.connect(self.Speech_To_Translate)
        self.ToolBarBottom.addAction(self.Voice_Speech)

        self.Speak = QAction(QIcon(os.path.join("assests", "audio-logo.png")), "Speak", self)
        self.Speak.triggered.connect(self.Translate_and_Speak)
        self.ToolBarBottom.addAction(self.Speak)

        self.show()

    def Translate(self):
        try:
            if "Hindi" in self.Select_Language_Output.currentText():
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(self.input.toPlainText())
                Result = Google_Translator.translate(Translate_from_input, dest="hi")
                self.output.setText(Result.text)
            elif "English" in self.Select_Language_Output.currentText():
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(self.input.toPlainText())
                Result = Google_Translator.translate(Translate_from_input, dest="en")
                self.output.setText(Result.text)
            else:
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(self.input.toPlainText())
                Result = Google_Translator.translate(Translate_from_input, dest="ta")
                self.output.setText(Result.text)
        except Exception:
            pass

    def Speech_To_Translate(self):
        try:
            listener = sr.Recognizer()
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source)
                Audio = listener.listen(source)
                Speech_To_Text = listener.recognize_google(Audio).lower()
            if "Hindi" in self.Select_Language_Output.currentText():
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(Speech_To_Text)
                Result = Google_Translator.translate(Translate_from_input, dest="hi")
                self.input.setText(Speech_To_Text)
                self.output.setText(Result.text)
            elif "English" in self.Select_Language_Output.currentText():
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(Speech_To_Text)
                Result = Google_Translator.translate(Translate_from_input, dest="en")
                self.input.setText(Speech_To_Text)
                self.output.setText(Result.text)
            else:
                Google_Translator = googletrans.Translator()
                Translate_from_input = str(Speech_To_Text)
                Result = Google_Translator.translate(Translate_from_input, dest="ta")
                self.input.setText(Speech_To_Text)
                self.output.setText(Result.text)
        except Exception:
            pass

    def Translate_and_Speak(self):
        try:
            if "Hindi" in self.Select_Language_Output.currentText():
                GTTSENGINE = gtts.gTTS(self.output.toPlainText(), lang="hi")
                GTTSENGINE.save(os.getcwd() + "/hindi.mp3")
                playsound(os.getcwd() + "/hindi.mp3")
                os.remove(os.getcwd() + "/hindi.mp3")
            elif "English" in self.Select_Language_Output.currentText():
                GTTSENGINE = gtts.gTTS(self.output.toPlainText(), lang="en")
                GTTSENGINE.save(os.getcwd() + "/english.mp3")
                playsound(os.getcwd() + "/english.mp3")
                os.remove(os.getcwd() + "/english.mp3")
            else:
                GTTSENGINE = gtts.gTTS(self.output.toPlainText(), lang="ta")
                GTTSENGINE.save(os.getcwd() + "/default.mp3")
                playsound(os.getcwd() + "/default.mp3")
                os.remove(os.getcwd() + "/default.mp3")
        except Exception:
            pass
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Translator()
    sys.exit(app.exec_())
