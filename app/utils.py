def sanitize_item(item: str) -> str:
    """Strip whitespace and return the item, or empty string if blank."""
    if not item:
        return ""
    return item.strip()


def is_valid_index(index: int, collection: list) -> bool:
    """Return True if index is within bounds of the collection."""
    return 0 <= index < len(collection)
