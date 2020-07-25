def conv(self):
    val = self.bit_txt.text()
    uni1 = self.cbox1.currentText()
    uni2 = self.cbox2.currentText()

    if uni1 == 'Kb':
        if uni2 == 'KB':
            self.byte_txt.setText(str(int(val) / 8))
        elif uni2 == 'MB':
            self.byte_txt.setText(str(int(val) / 8000))
        elif uni2 == 'GB':
            self.byte_txt.setText(str(int(val) / 8000000))
    elif uni1 == 'Mb':
        if uni2 == 'KB':
            self.byte_txt.setText(str(int(val) * 125))
        elif uni2 == 'MB':
            self.byte_txt.setText(str(int(val) / 8))
        elif uni2 == 'GB':
            self.byte_txt.setText(str(int(val) / 8000))
    elif uni1 == 'Gb':
        if uni2 == 'KB':
            self.byte_txt.setText(str(int(val) * 125000))
        elif uni2 == 'MB':
            self.byte_txt.setText(str(int(val) * 125))
        elif uni2 == 'GB':
            self.byte_txt.setText(str(int(val) / 8))
    else:
        pass