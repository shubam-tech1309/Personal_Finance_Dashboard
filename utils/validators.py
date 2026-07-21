"""
=========================================================
Personal Finance Dashboard
Validation Utilities
=========================================================

Reusable validation functions.

UI components should call these functions
instead of writing validation logic repeatedly.
"""


def clean_text(value: str) -> str:
    """
    Removes extra spaces.

    Example:
    "  salary income  "
    becomes:
    "salary income"
    """

    if value is None:
        return ""

    return value.strip()



def title_case(value: str) -> str:
    """
    Converts text into Title Case.

    Example:

    "monthly salary"

    becomes:

    "Monthly Salary"
    """

    value = clean_text(value)

    return value.title()



def validate_required(
    value: str,
    field_name: str
):
    """
    Checks required fields.

    Returns:
    (True, "")
    if valid

    (False, error message)
    if invalid
    """

    value = clean_text(value)


    if not value:

        return (
            False,
            f"{field_name} is required."
        )


    return (
        True,
        ""
    )



def validate_amount(
    amount: float
):
    """
    Validates transaction amount.
    """

    if amount <= 0:

        return (
            False,
            "Amount must be greater than zero."
        )


    return (
        True,
        ""
    )



def validate_transaction(
    description: str,
    amount: float
):
    """
    Complete transaction validation.
    """

    valid, message = validate_required(
        description,
        "Description"
    )


    if not valid:

        return (
            False,
            message
        )


    valid, message = validate_amount(
        amount
    )


    if not valid:

        return (
            False,
            message
        )


    return (
        True,
        ""
    )