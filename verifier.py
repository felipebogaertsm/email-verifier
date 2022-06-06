import aiodns
import re
import smtplib


class NotValidEmail(Exception):
    pass


class EmailVerifier:
    def __init__(self, email):
        self.email = email

    def validate(self, startswith="validate_"):
        for method in dir(self):
            if method.startswith("validate_"):
                result = getattr(self, method)()
                if not result:
                    raise NotValidEmail(f"{self.email} is not valid")

    def validate_format(self):
        if re.match(
            self.email,
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        ):
            return True

        return False

    def validade_mx_registry(self):
        pass
