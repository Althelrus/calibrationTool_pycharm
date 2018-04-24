
-----------------------------------------------------
         Start Program
------------------------------------------------------
Program start by running main.py

-----------------------------------------------------
          Convert PTQT4 resource file .rc to .py
------------------------------------------------------
The resource file that is created with the designer must be converted
to .py so the UI.py can import it.

C:\Python27\Lib\site-packages\PyQt4>
pyrcc4.exe -o file.py file.qrc

NOTE: The graphic files are only needed for the QTDesigner
      resource file, location is /resource_files.
      
------------------------------------------------------
          Convert QTDesigner to .py
------------------------------------------------------          
Save the .ui file in:
    Example:
    C:\Python27\Lib\site-packages\PyQt4\uic
   From file directory:  python3 -m PyQt5.uic.pyuic -x  <file_name.ui> -o <file_name.py>
Execute: python pyuic.py <file_name.ui> -o <file_name.py>
  python pyuic.py file.ui -o file.py

------------------------------------------------------
          To Compile the .exe file:
------------------------------------------------------
C:\Python27\Lib\site-packages\PyInstaller-3.0>
python pyinstaller.py -F 235-00002.py

MISC:
.png files are only used in the QDesigner (Issue with Intel NUC PC)
resource file.
-------------------------------------------------------
            MS docx location
-------------------------------------------------------
Need to make documents
