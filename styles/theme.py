APP_STYLE = """
/* =====================================================
   GLOBAL
===================================================== */

QWidget{
    background:#F3F6FA;
    color:#1F2937;
    font-family:"Segoe UI";
    font-size:10pt;
}

/* =====================================================
   MAIN WINDOW
===================================================== */

QMainWindow{
    background:#F3F6FA;
}

/* =====================================================
   LABELS
===================================================== */

QLabel{
    background:transparent;
    color:#1F2937;
}

/* =====================================================
   LINE EDIT
===================================================== */

QLineEdit{
    background:white;
    border:1px solid #D6DBE3;
    border-radius:10px;
    padding:8px 12px;
    min-height:22px;
}

QLineEdit:hover{
    border:1px solid #3B82F6;
}

QLineEdit:focus{
    border:2px solid #2563EB;
}

/* =====================================================
   COMBO BOX
===================================================== */

QComboBox{
    background:white;
    border:1px solid #D6DBE3;
    border-radius:10px;
    padding:8px;
    min-height:22px;
}

QComboBox:hover{
    border:1px solid #3B82F6;
}

QComboBox:focus{
    border:2px solid #2563EB;
}

QComboBox::drop-down{
    border:none;
    width:24px;
}

/* =====================================================
   DATE EDIT
===================================================== */

QDateEdit{
    background:white;
    border:1px solid #D6DBE3;
    border-radius:10px;
    padding:8px;
}

QDateEdit:focus{
    border:2px solid #2563EB;
}

/* =====================================================
   DOUBLE SPIN BOX
===================================================== */

QDoubleSpinBox{
    background:white;
    border:1px solid #D6DBE3;
    border-radius:10px;
    padding:8px;
}

QDoubleSpinBox:focus{
    border:2px solid #2563EB;
}

/* =====================================================
   BUTTON
===================================================== */

QPushButton{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    font-weight:600;

    padding:10px 18px;

    min-height:24px;
}

QPushButton:hover{

    background:#1D4ED8;
}

QPushButton:pressed{

    background:#1E3A8A;
}

/* =====================================================
   TABLE
===================================================== */

QTableWidget{

    background:white;

    alternate-background-color:#F8FAFC;

    border:1px solid #D6DBE3;

    border-radius:12px;

    gridline-color:#ECEFF3;

    selection-background-color:#DBEAFE;

    selection-color:#111827;
}

QHeaderView::section{

    background:#EEF2F7;

    border:none;

    border-bottom:1px solid #D6DBE3;

    padding:10px;

    font-weight:700;
}

/* =====================================================
   SCROLL BAR
===================================================== */

QScrollBar:vertical{

    border:none;

    background:#EEF2F7;

    width:12px;

    margin:0px;
}

QScrollBar::handle:vertical{

    background:#C6CBD3;

    border-radius:6px;
}

QScrollBar::handle:vertical:hover{

    background:#AEB6C2;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{

    height:0px;
}

QScrollBar:horizontal{

    height:12px;

    background:#EEF2F7;
}

QScrollBar::handle:horizontal{

    background:#C6CBD3;

    border-radius:6px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal{

    width:0px;
}

/* =====================================================
   SPLITTER
===================================================== */

QSplitter::handle{

    background:#E5E7EB;
}

QSplitter::handle:hover{

    background:#CBD5E1;
}
"""