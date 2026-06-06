def score_field_match(source_key: str, target_key: str) -> float:
    source = (source_key or "").strip().lower()
    target = (target_key or "").strip().lower()

    if not source or not target:
        return 0.0
    if source == target:
        return 1.0
    if source in target or target in source:
        return 0.7
    return 0.0
