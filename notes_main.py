from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTextEdit, QListWidget, QLineEdit, QPushButton, QInputDialog
import json

def show_note():
    key = spisok_zam.selectedItems()[0].text()
    zametki.setText(notes[key]['текст'])
    spisok_teg.clear()
    spisok_teg.addItems(notes[key]['теги'])

def add_note():
    notes_name, result = QInputDialog.getText(
        main_window, 'Добавление заметки', 'Название'
    )
    if result:
        notes[notes_name] = {
            'текст': '',
            'теги': []
        }
        spisok_zam.addItem(notes_name)
        with open('nates_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def del_note():
    if spisok_zam.selectedItems():
        key = spisok_zam.selectedItems()[0].text()
        del notes[key]
        spisok_zam.clear()
        spisok_zam.addItems(notes)
        zametki.clear()
        spisok_teg.clear()
        with open('nates_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def save_note():
    if spisok_zam.selectedItems():
        key = spisok_zam. selectedItems()[0].text()
        notes[key]['текст'] = zametki.toPlainText()
        with open('nates_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)

def add_tag():
    if spisok_zam.selectedItems():
        key = spisok_zam.selectedItems()[0].text()
        tag = find.text()
        if tag != '' and not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            spisok_teg.addItem(tag)
            find.clear()
            with open('nates_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)



def del_tag():
            if spisok_teg.selectedItems():
                key = spisok_zam.selectedItems()[0].text()
                tag = spisok_teg.selectedItems()[0].text()
                notes[key]['теги'].remove(tag)
                spisok_teg.clear()
                spisok_teg.addItems(notes[key]['теги'])
                with open('nates_data.json', 'w') as file:
                    json.dump(notes, file, sort_keys=True, ensure_ascii=False)
            

def search_tag():
    tag = find.text()
    if tag and search.text() == 'Искать заметки по тегу':
        notes_filtered = dict()
        for key in notes:
            if tag in notes[key]['теги']:
                notes_filtered[key] = notes[key]
            search.setText('Сбросить поиск')
            spisok_teg.clear()
            spisok_zam.clear()
            zametki.clear()
            spisok_zam.addItems(notes_filtered)
    else:
        find.clear()
        search.setText('Искать заметки по тегу')
        spisok_zam.clear()
        spisok_zam. addItems(notes)











app = QApplication([])
main_window = QWidget()
main_window.resize(900, 600)
main_window.setWindowTitle('Умные заметки')

zametki = QTextEdit()
spisok_zam = QListWidget()
spisok_teg = QListWidget()
text = QLabel('список заметок')
text2 = QLabel('список тегов')
create = QPushButton('Создать заметку')
delete = QPushButton('Удалить заметку')
save = QPushButton('Сохрпанить заметку')
find = QLineEdit('')
find.setPlaceholderText('Введите тег...')
add_zam = QPushButton('Добавить к Заметке')
unteg = QPushButton('Открепить от заметки')
search = QPushButton('Искать заметки по тегу')
v_line1 = QVBoxLayout()
v_line1.addWidget(zametki)
v_line2 = QVBoxLayout()
h_line1 = QHBoxLayout()
h_line1.addWidget(create)
h_line1.addWidget(delete)
h_line2 = QHBoxLayout()
h_line2.addWidget(add_zam)
h_line2.addWidget(unteg)
v_line2.addWidget(text)
v_line2.addWidget(spisok_zam)
v_line2.addLayout(h_line1)
v_line2.addWidget(save)
v_line2.addWidget(text2)
v_line2.addWidget(spisok_teg)
v_line2.addWidget(find)
v_line2.addLayout(h_line2)
v_line2.addWidget(search)
main_h_line = QHBoxLayout()
main_h_line.addLayout(v_line1)
main_h_line.addLayout(v_line2)



with open('nates_data.json', 'r') as file:
    notes = json.load(file)

spisok_zam.addItems(notes)
spisok_zam.itemClicked.connect(show_note)
create.clicked.connect(add_note)
delete.clicked.connect(del_note)
save.clicked.connect(save_note)
add_zam.clicked.connect(add_tag)
unteg.clicked.connect(del_tag)
search.clicked.connect(search_tag)

main_window.setLayout(main_h_line)
main_window.show()
app.exec_()

