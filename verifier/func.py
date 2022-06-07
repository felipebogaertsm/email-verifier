import dns.resolver


def get_host_name_from_email(email: str) -> str:
    return email[email.find("@") + 1 :]


def get_mx_ip(host_name: str) -> dns.resolver.Answer:
    return dns.resolver.query(host_name, "MX")


def get_mx_hosts(email: str) -> dns.resolver.Answer:
    return get_mx_ip(get_host_name_from_email(email))
