APP_STYLE = """
QWidget{
    background:#F4F6F9;
    color:#1F2937;
    font-family:'Segoe UI';
    font-size:10pt;
}

QMainWindow{
    background:#F4F6F9;
}

QMenuBar{
    background:#FFFFFF;
}

QStatusBar{
    background:#FFFFFF;
}

QPushButton{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:8px;
    padding:8px 16px;
    font-weight:600;
}

QPushButton:hover{
    background:#1D4ED8;
}

QPushButton:pressed{
    background:#1E40AF;
}

QLineEdit,
QComboBox,
QDateEdit,
QSpinBox,
QDoubleSpinBox{
    background:white;
    border:1px solid #D1D5DB;
    border-radius:8px;
    padding:8px;
}

QTableWidget{
    background:white;
    border:1px solid #D1D5DB;
    gridline-color:#E5E7EB;
    border-radius:10px;
}

QHeaderView::section{
    background:#E5E7EB;
    padding:8px;
    border:none;
    font-weight:bold;
}

QGroupBox{
    border:1px solid #D1D5DB;
    border-radius:10px;
    margin-top:12px;
    background:white;
    font-weight:bold;
}

QGroupBox::title{
    subcontrol-origin:margin;
    left:12px;
    padding:0 4px;
}
"""