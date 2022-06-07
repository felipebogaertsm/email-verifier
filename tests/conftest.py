import pytest
import pytest_asyncio


@pytest.fixture
@pytest_asyncio.fixture
def sample_existing_emails() -> list[str]:
    return [
        "felipebogaerts@gmail.com",
        "me@felipebm.com",
    ]


@pytest.fixture
@pytest_asyncio.fixture
def sample_invalid_emails() -> list[str]:
    return [
        "jdsnfadsjfdasklm",
        "",
        "@test.com",
        "test@",
        "invalid@felipebm.com",
    ]
