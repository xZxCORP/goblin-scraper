from typing import Any, Type
from annotated_types import T


def dict_to_dataclass(cls: Type[T], data: Any) -> T:
    """
    Convertit un dictionnaire en une instance de la dataclass donnée.
    Cette fonction gère également les sous-classes imbriquées.
    """
    if isinstance(data, list):
        return [
            dict_to_dataclass(cls.__args__[0], item) for item in data
        ]  # pour les listes

    if isinstance(data, dict):
        field_types = cls.__annotations__
        return cls(
            **{
                key: (
                    dict_to_dataclass(field_types[key], value)
                    if key in field_types
                    else value
                )
                for key, value in data.items()
            }
        )

    return data
