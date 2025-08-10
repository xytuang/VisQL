import datetime
from typing import Any, Type


def coerce_type(typ: str) -> Type[Any]:
    """Coereces a DuckDB type to Python type

    Args:
        typ (str): DuckDB type to coerce

    Returns:
        Type[Any]: Python equivalent type
    """
    typ = typ.lower()
    if typ in {"tinyint", "smallint", "integer", "int", "bigint"}:
        return int
    elif typ in {"float", "float4", "float8", "double", "real", "decimal", "numeric"}:
        return float
    elif typ in {"boolean", "bool"}:
        return bool
    elif typ in {"varchar", "char", "text", "string"}:
        return str
    elif typ in {"date", "timestamp", "timestamp_ntz", "timestamp_tz"}:
        return datetime.datetime
    elif typ == "time":
        return datetime.time
    elif typ == "blob":
        return bytes
    else:
        return Any
