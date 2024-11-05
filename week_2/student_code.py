def key_path(prefix, key):
        return f"{prefix}.{key}" if prefix else key



def validate(data, template, path=""):
    for key, expected_type in template.items():
        keypath = key_path(path, key)
        
        # Check if the key exists in the data
        if key not in data:
            return False, f"mismatched keys: {keypath}"
        
        # Check if the value is a nested dictionary
        if isinstance(expected_type, dict):
            if not isinstance(data[key], dict):
                return False, f"bad type: {keypath}"
            # Recursive call for nested dictionary
            state, error = validate(data[key], expected_type, keypath)
            if not state:
                return state, error
        else:
            # Check if the value matches the expected type
            if not isinstance(data[key], expected_type):
                return False, f"bad type: {keypath}"

    # Check for extra keys in the data not in the defined template
    for key in data:
        if key not in template:
            keypath = key_path(path, key)
            return False, f"mismatched keys: {keypath}"

    return True, ""
