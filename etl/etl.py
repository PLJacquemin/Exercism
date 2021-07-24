def transform(legacy_data):
    return {l.lower() : k for k, v in legacy_data.items() for l in v}
