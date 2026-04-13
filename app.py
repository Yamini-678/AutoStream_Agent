from agent.rag import retrieve_answer
from agent.intent import intent_message
from agent.state import state
from agent.tools import mock_lead_capture

print("AutoStream Agent Ready!")

while True:
    user = input("\nYou: ")

    if state["collecting_lead"]:
        if not state["name"]:
            state["name"] = user
            print("Agent: Your email please?")
            continue
        if not state["email"]:
            state["email"] = user
            print("Agent: which creator platform do you use?")
            continue
        if not state["platform"]:
            state["platform"] = user

            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )

            print("Agent: Thank you ! our team will contact you soon.")
            state["collecting_lead"] = False
            continue
    
    intent = intent_message(user)

    if intent == "greeting":
        print("Agent : Hello! Ask me about AutoStream plans.")
    elif intent == "inquiry":
        print("Agent: ", retrieve_answer(user))
    elif intent == "high_intent":
        print("Agent: May I know your name?")
        state["collecting_lead"] = True

    else:
        print("Agent: Can you rephrase?")