import json

with open("data/knowledge_base.json", "r") as f:
    knowledge = json.load(f)

def retrieve_answer(query):
    query = query.lower().strip()

    if "basic" in query:
        plan = knowledge["Basic Plan"]
        return f"""
Basic Plan Details:
Price : {plan['price']}
Videos : {plan['videos']} 
Resolution : {plan['resolution']}"""
    
    elif "pro" in query or "price" in query:
        plan = knowledge["Pro Plan"]
        return f"""
Pro Plan Details:
Price : {plan['price']}
Videos : {plan['videos']} 
Resolution : {plan['resolution']}
Features : {plan['features']}"""

    elif "refund" in query or "policy" in query:
        policy = knowledge["Policies"]
        return f"""
Company Policies:
Refund Policy : {policy['refund']}
Support : {policy['support']} """
    else:
        return "I'm not sure. Can you ask about pricing or plans?"