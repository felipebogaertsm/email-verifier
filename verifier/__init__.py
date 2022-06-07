import re
import smtplib
import socket
from typing import Optional

from .func import get_mx_hosts


class NotValidEmail(Exception):
    pass


class SMTPServerDisconnected(Exception):
    pass


class SMTPConnectionError(Exception):
    pass


class RequestTimeout(Exception):
    pass


class SocketError(Exception):
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

    def validate_mx_registry(self, timeout: Optional[float | int] = 5):
        email = self.email
        mx = get_mx_hosts(self.email)

        try:
            smtp = smtplib.SMTP(mx[0].to_text(), timeout=timeout)

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
        except smtplib.SMTPServerDisconnected:
            raise SMTPServerDisconnected(f"Host '{mx}' disconnected")
        except smtplib.SMTPConnectError:
            raise SMTPConnectionError(f"Unable to connect to host '{mx}'")
        except socket.timeout:
            raise RequestTimeout(f"Request timed out")
        except socket.error:
            raise SocketError(f"Socket error")
