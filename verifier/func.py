import dns.resolver


def get_host_name_from_email(email: str) -> str:
    return email[email.find("@") + 1 :]


async def get_mx_ip(host_name: str) -> list[str]:
    return await dns.resolver.resolve(host_name, "MX")


async def get_mx_hosts(email: str) -> list[str]:
    return await get_mx_ip(get_host_name_from_email(email))
