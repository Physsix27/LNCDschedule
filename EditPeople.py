from PyQt5 import uic,QtCore, QtWidgets
from LNCDutils import  *

"""
This class provides a window for adding contact information
data in conact_model
"""
class EditPeopleWindow(QtWidgets.QDialog):

    def __init__(self,parent = None):
        
        self.dob = None
        columns=['ctype','changes','pid']
        self.edit_model = { k: None for k in columns }
        super(EditPeopleWindow,self).__init__(parent)
        uic.loadUi('./ui/edit_person.ui',self)
        self.setWindowTitle('Edit person')

        self.ctype_box.activated.connect(self.formatter)
        ## wire up buttons and boxes
        self.ctype_box.activated.connect(lambda: self.allvals('ctype'))
        self.value_box.textChanged.connect(lambda: self.allvals('value'))



    def allvals(self, key = 'all'):
        if(key in ['ctype'    ,'all']): self.edit_model['ctype']=self.ctype_box.currentText()
        if(key in ['value'    ,'all']): self.edit_model['changes']=self.value_box.text()

    def edit_person(self,pid, dob):
        self.dob = dob
        self.value_box_2.setText(str(pid))
        self.edit_model['pid'] = pid

    def formatter(self):
        if(str(self.ctype_box.currentText()) == 'dob'):
            self.value_box.setText(self.dob)
        else:
            self.value_box.clear()