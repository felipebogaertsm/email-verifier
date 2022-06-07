import re
import smtplib
import socket
from typing import Optional

from .func import get_mx_hosts


class NotValidEmail(Exception):
    pass


class EmailVerifier:
    def __init__(self, email: str):
        self.email = email

    def validate(self, startswith: str = "validate_"):
        for method in dir(self):
            if method.startswith(startswith):
                result = getattr(self, method)()
                if not result:
                    pass
                    # raise NotValidEmail(f"{self.email} is not valid")

    def validate_format(self):
        if re.match(
            self.email,
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",
        ):
            return True

        return False

    def validate_mx_registry(self, timeout: Optional[float | int] = 1):
        email = self.email
        mx = get_mx_hosts(self.email)

        smtp = smtplib.SMTP(str(mx[0].to_text().split()[1][:-1]), timeout=timeout)

        status, _ = smtp.ehlo()

        if status >= 400:
            smtp.quit()
            return False

        smtp.mail("")
        status, _ = smtp.rcpt(email)
        smtp.quit()

        if int(status / 100) == 2:  # response status is 2xx
            return True
        else:
            return False
