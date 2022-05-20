import pytest

from commander import Application


def test_basic():
    with pytest.raises(SystemExit):
        app = Application()
        app.run(["test", "--help"])
