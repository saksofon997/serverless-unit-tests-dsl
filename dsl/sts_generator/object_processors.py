from textx.exceptions import TextXSemanticError
from textx import get_location


def check_env_unique(jsonObj):
    if ("JSONObject" in jsonObj.__class__.__name__):
        keys = [member.key for member in jsonObj.members]

        duplicate_keys = set(
            [key for key in keys if keys.count(key) > 1])

        if len(duplicate_keys) != 0:
            raise TextXSemanticError(
                f"Duplicate environment variable keys found {duplicate_keys}, on\n\n{get_location(jsonObj)}")

        for member in jsonObj.members:
            check_env_unique(member)


def environment_processor(env):
    try:
        if env.type == "json":
            check_env_unique(env.value)
    except TextXSemanticError as e:
        print(e.message)
