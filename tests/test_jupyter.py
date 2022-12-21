import logits

from unittest.mock import MagicMock


def test_run() -> None:
    session = MagicMock(return_value=None)
    logits.jupyter.run(session)
