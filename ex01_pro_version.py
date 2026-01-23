def ai_usage(query):
    if not isinstance(query, str):
        return None

    responses = {
        "what": "Chat GPT, Gemini",
        "for what": "Questions about syntaxis, code refactoring",
        "how": (
            "For example I asked whether it worth checking the query variable type or not, "
            "according to the exercise, because it sounded ambiguous for me"
        ),
    }

    clean_query = query.strip().lower()

    for key, value in responses.items():
        if clean_query.startswith(key):
            return value

    return None
