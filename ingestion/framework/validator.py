class FlightValidator:

    REQUIRED_FIELDS = [

        "flight",

        "departure",

        "arrival"

    ]

    @classmethod

    def validate(cls, record):

        for field in cls.REQUIRED_FIELDS:

            if field not in record:

                return False

        return True