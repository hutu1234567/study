from PyQt5.QtCore import pyqtSlot, QDate
from PyQt5.QtWidgets import QDialog, QApplication, QDialogButtonBox
import sys
from Ui_paymentdlg import Ui_PaymentDlg


class PaymentDlg( QDialog, Ui_PaymentDlg ):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super( PaymentDlg, self ).__init__( parent )
        self.setupUi( self )
        for lineEdit in (self.forenameLineEdit, self.surnameLineEdit,
                         self.checkNumLineEdit, self.accountNumLineEdit,
                         self.bankLineEdit, self.sortCodeLineEdit,
                         self.creditCardLineEdit):
            lineEdit.textEdited.connect( self.updateUi )
        for dateEdit in (self.validFromDateEdit, self.expiryDateEdit):
            dateEdit.dateChanged.connect( self.updateUi )
        self.paidCheckBox.clicked.connect( self.updateUi )
        self.updateUi()
        self.forenameLineEdit.setFocus()

    def updateUi(self):
        today = QDate.currentDate()
        enable = (self.forenameLineEdit.text() and
                  self.surnameLineEdit.text())
        if enable:
            enable = (self.paidCheckBox.isChecked() or
                      (self.checkNumLineEdit.text() and
                       self.accountNumLineEdit.text() and
                       self.bankLineEdit.text() and
                       self.sortCodeLineEdit.text()) or
                      (self.creditCardLineEdit.text() and
                       self.validFromDateEdit.date() <= today and
                       self.expiryDateEdit.date() >= today))
        self.buttonBox.button( QDialogButtonBox.Ok ).setEnabled( bool( enable ) )


if __name__ == "__main__":
    app = QApplication( sys.argv )
    form = PaymentDlg()
    form.show()
    app.exec_()