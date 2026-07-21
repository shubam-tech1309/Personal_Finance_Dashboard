class SuggestionEngine:
    """
    Provides intelligent suggestions
    based on previous user entries.
    """


    def __init__(self):

        self.categories = [

            "Salary",

            "Business",

            "Food",

            "Transport",

            "Shopping",

            "Bills",

            "Investment",

            "Medical",

            "Education",

            "Entertainment",

            "Other"

        ]


        self.descriptions = []



    def add_description(
        self,
        text
    ):

        text = (
            text
            .strip()
            .title()
        )


        if text and text not in self.descriptions:

            self.descriptions.append(
                text
            )



    def get_category_suggestions(
        self,
        text
    ):


        text = (
            text
            .lower()
            .strip()
        )


        if not text:

            return self.categories



        results = []


        for item in self.categories:


            if text in item.lower():

                results.append(
                    item
                )


        return results



    def get_description_suggestions(
        self,
        text
    ):


        text = (
            text
            .lower()
            .strip()
        )


        if not text:

            return self.descriptions[-5:]



        results = []


        for item in self.descriptions:


            if text in item.lower():

                results.append(
                    item
                )


        return results[-10:]