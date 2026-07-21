APP_STYLE = """

/* ==========================
   GLOBAL APPLICATION
========================== */


QMainWindow
{
    background:#F8FAFC;
}


QWidget
{
    font-family:"Segoe UI";
    font-size:14px;
    color:#1F2937;
}



/* ==========================
   LABELS
========================== */


QLabel
{
    color:#111827;
}



/* ==========================
   INPUTS
========================== */


QLineEdit,
QComboBox,
QDateEdit,
QDoubleSpinBox
{

    background:#FFFFFF;

    border:1px solid #CBD5E1;

    border-radius:10px;

    padding:9px;

}


QLineEdit:focus,
QComboBox:focus,
QDateEdit:focus,
QDoubleSpinBox:focus
{

    border:2px solid #2563EB;

}



/* ==========================
   BUTTONS
========================== */


QPushButton
{

    background:#2563EB;

    color:white;

    border:none;

    border-radius:10px;

    padding:10px 18px;

    font-weight:600;

}



QPushButton:hover
{

    background:#1D4ED8;

}



QPushButton:pressed
{

    background:#1E40AF;

}



/* Secondary buttons */


QPushButton#secondary
{

    background:#E5E7EB;

    color:#111827;

}



QPushButton#secondary:hover
{

    background:#D1D5DB;

}



/* ==========================
   TABLE
========================== */


QTableWidget
{

    background:white;

    border:none;

    border-radius:12px;

    gridline-color:#E5E7EB;

}



QHeaderView::section
{

    background:#F1F5F9;

    padding:10px;

    border:none;

    font-weight:700;

}



QTableWidget::item
{

    padding:8px;

}



QTableWidget::item:hover
{

    background:#EFF6FF;

}



QTableWidget::item:selected
{

    background:#DBEAFE;

    color:#1E3A8A;

}



/* ==========================
   COMBO POPUP
========================== */


QComboBox QAbstractItemView
{

    background:white;

    selection-background-color:#DBEAFE;

    selection-color:#1E3A8A;

    border-radius:8px;

}



/* ==========================
   SCROLLBAR
========================== */


QScrollBar:vertical
{

    width:10px;

}



QScrollBar::handle:vertical
{

    background:#CBD5E1;

    border-radius:5px;

}


"""