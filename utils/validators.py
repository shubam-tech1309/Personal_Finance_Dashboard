import re

from PySide6.QtCore import QDate



def clean_text(
    text
):
    """
    Cleans and formats user text.
    """

    if text is None:

        return ""


    text = str(text)


    # Remove extra spaces

    text = re.sub(
        r"\s+",
        " ",
        text
    )


    text = text.strip()



    # Title case conversion

    text = text.title()



    return text





def clean_category(
    category
):

    category = clean_text(
        category
    )


    if not category:

        return "Other"


    return category





def clean_description(
    description
):

    return clean_text(
        description
    )





def clean_amount(
    amount
):


    try:

        amount = float(
            amount
        )


    except:

        return 0



    if amount < 0:

        return 0



    return round(
        amount,
        2
    )





def validate_date(
    date_text
):


    if not date_text:

        return False



    date = QDate.fromString(

        date_text,

        "yyyy-MM-dd"

    )


    return date.isValid()





def validate_transaction(
    data
):

    errors = []



    if not data.get(
        "date"
    ):

        errors.append(
            "Date is required."
        )



    if not data.get(
        "type"
    ):

        errors.append(
            "Transaction type required."
        )



    if not data.get(
        "category"
    ):

        errors.append(
            "Category required."
        )



    if not data.get(
        "description"
    ):

        errors.append(
            "Description required."
        )



    amount = clean_amount(

        data.get(
            "amount",
            0
        )

    )



    if amount <= 0:

        errors.append(
            "Amount must be greater than zero."
        )



    return (

        len(errors) == 0,

        errors

    )