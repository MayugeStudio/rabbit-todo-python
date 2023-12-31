"""
The Exception to Rabbit-Todo
"""

from __future__ import annotations


class RabbitTodoError(Exception):
    """The Exception to Rabbit Todo Application"""

    def __init__(self, code: str, rabbit_exception: RabbitTodoError | None = None) -> None:
        self._code = code + ";"
        if rabbit_exception is not None:
            self._code += rabbit_exception.code

    @property
    def code(self) -> str:
        """Return error code"""
        return self._code + ";"
