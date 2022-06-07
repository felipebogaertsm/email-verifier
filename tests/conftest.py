import pytest


@pytest.fixture
def sample_existing_emails() -> list[str]:
    return [
        "felipebogaerts@gmail.com",
        "me@felipebm.com",
    ]


@pytest.fixture
def sample_invalid_emails() -> list[str]:
    return [
        "jdsnfadsjfdasklm",
        "",
        "@test.com",
        "test@",
        "invalid@felipebm.com",
    ]
