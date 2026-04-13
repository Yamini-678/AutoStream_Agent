def intent_message(message):
    msg = message.lower().strip()

    if "hi" in msg or "hello" in msg:
        return "greeting"
    elif "buy" in msg or "signup" in msg or "try" in msg or "subscribe" in msg:
        return "high_intent"
    elif "price" in msg or "plan" in msg or "cost" in msg:
        return "inquiry"
    return "Unknown"