from carbon_calculator import calculate_carbon_footprint
from pdf_retriever import retrieve_from_pdf
conversation_state = {}

def detect_query_type(user_input):
    user_input = user_input.lower()

    if user_input.startswith("what"):
        return "definition"
    if user_input.startswith("why"):
        return "reason"
    if user_input.startswith("how"):
        return "process"
    if "example" in user_input:
        return "example"

    return "general"

def detect_intent(user_input):
    user_input = user_input.lower()

    if any(word in user_input for word in ["sustainable", "sustainability", "define", "meaning"]):
        return "definition"

    if "carbon" in user_input:
        return "carbon"

    if any(word in user_input for word in ["energy", "electricity", "power", "ac"]):
        return "energy"

    if any(word in user_input for word in ["water", "tap", "leak"]):
        return "water"

    if any(word in user_input for word in ["plastic", "waste", "garbage"]):
        return "waste"

    if any(word in user_input for word in ["climate", "environment", "global warming"]):
        return "climate"

    return "unknown"

def generate_response(user_input, knowledge):
    user_input = user_input.lower()
    intent = detect_intent(user_input)
    query_type = detect_query_type(user_input)

    # COMPOUND QUERY HANDLER

    tokens = user_input.split()
    if len(tokens) == 2 and tokens[1] in ["impact", "examples", "effects"]:
        topic = tokens[0]
        conversation_state["topic"] = topic

        query = f"{topic} {tokens[1]}"
        pdf_context = retrieve_from_pdf(query)

        if pdf_context:
            return (
                f"🌍 **Impact of {topic.capitalize()}**\n\n"
                f"{pdf_context[0][:400]}...\n\n"
                "Would you like **examples** or **how to reduce it**?"
            )

    # TOPIC SELECTION (AGENT MEMORY)
  
    if user_input in ["plastic", "energy", "water", "waste", "climate"]:
        conversation_state["topic"] = user_input

        return (
            f"🌱 Let’s talk about **{user_input.capitalize()}**.\n\n"
            "What would you like to know?\n"
            "• impact\n"
            "• examples\n"
            "• how to reduce"
        )


    #  FOLLOW-UP HANDLING

    if user_input in ["impact", "examples", "how", "next steps"]:
        topic = conversation_state.get("topic")

        if not topic:
            return "⚠️ Please choose a topic first (plastic, energy, water)."

        query = f"{topic} {user_input}"
        pdf_context = retrieve_from_pdf(query)

        if not pdf_context:
            return "⚠️ No relevant information found in the document."

        if user_input == "impact":
            return (
                f"🌍 **Impact of {topic.capitalize()}**\n\n"
                f"{pdf_context[0][:400]}...\n\n"
                "Would you like **examples** or **how to reduce it**?"
            )

        if user_input == "examples":
            return (
                f"📌 **Examples related to {topic.capitalize()}**\n\n"
                f"{pdf_context[0][:300]}...\n\n"
                "Would you like **impact** or **next steps**?"
            )

        if user_input in ["how", "next steps"]:
            return (
                f"✅ **How to reduce {topic.capitalize()} impact**:\n\n"
                f"{pdf_context[0][:300]}...\n\n"
                "Would you like to **calculate your carbon footprint**?"
            )

    
    #  CARBON FLOW

    if intent == "carbon":
        return (
            "🌍 **Carbon Footprint Estimation**\n\n"
            "Enter values as:\n"
            "`electricity, transport, plastic`"
        )

    if "," in user_input:
        try:
            e, t, p = map(float, user_input.split(","))
            score = calculate_carbon_footprint(e, t, p)
            return f"🌱 **Your Estimated Carbon Footprint:** {score} kg CO₂"
        except:
            pass

    # DEFINITION (PDF RAG ONLY)

    if intent == "definition":
        pdf_context = retrieve_from_pdf(user_input)
        if pdf_context:
            return (
                "📄 **From the Sustainability Guide:**\n\n"
                f"{pdf_context[0][:600]}..."
            )

   
    #  FALLBACK
  
    tips = knowledge.get(intent, [])
    pdf_context = retrieve_from_pdf(user_input)

    response = f"🌱 **Tips related to {intent}:**\n\n"
    for tip in tips:
        response += f"• {tip}\n"

    if pdf_context:
        response += "\n📄 **From the Sustainability Guide:**\n" + pdf_context[0][:300] + "..."

    return response
