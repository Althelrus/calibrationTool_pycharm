-----------------------------------------------------
          Convert PTQT4 resource file .rc to .py
------------------------------------------------------
The resource file that is created with the designer must be converted
to .py so the UI.py can import it.

C:\Python27\Lib\site-packages\PyQt4>
pyrcc4.exe -o fm_printer_rc.py fm_printer.qrc

NOTE: The graphic files are only needed for the QTDesigner
      resource file, location is /resource_files.
      
------------------------------------------------------
          Convert QTDesigner to .py
------------------------------------------------------          
Save the .ui file in:
    Example:
    C:\Python27\Lib\site-packages\PyQt4\uic
Execute: python pyuic.py <file_name.ui> -o <file_name.py>
  python pyuic.py fmi_label_creator_ui.ui -o fmi_label_creator_ui.py

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
The .docx file for the procedure is located in:
Z:\PQA\Test_Engineering\Manufacturing_Test\23500002_prod_label_maker\ms_doc_procedure
