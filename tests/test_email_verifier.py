import pytest

from verifier import EmailVerifier

from verifier.func import get_host_name_from_email, get_mx_hosts, get_mx_ip


@pytest.mark.asyncio
async def test_host_name_from_email(sample_existing_emails):
    for email in sample_existing_emails:
        host_name = get_host_name_from_email(email)

        assert isinstance(host_name, str)
        assert not "@" in host_name

        ip_list = await get_mx_ip(host_name)

        assert isinstance(ip_list, list)


@pytest.mark.skip
def test_get_mx_hosts(sample_existing_emails):
    for email in sample_existing_emails:
        mx_hosts = get_mx_hosts(email)

        assert isinstance(mx_hosts, list)


@pytest.mark.skip
def test_valid_emails(sample_existing_emails):
    for email in sample_existing_emails:
        assert EmailVerifier(email).validate()


def test_invalid_emails(sample_invalid_emails):
    for email in sample_invalid_emails:
        with pytest.raises(Exception):
            _ = EmailVerifier(email).validate()
