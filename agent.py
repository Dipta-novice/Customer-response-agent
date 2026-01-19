from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from tools import orders_database_query, request_review


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key="4U"
)

tools = [orders_database_query, request_review]

agent = create_agent(
    llm,
    tools=tools,
     system_prompt=(
        "You are a customer support email agent.\n"
        "You MUST write the final email addressed directly to the customer.\n"
        "Do NOT describe your steps.\n"
        "Do NOT summarize actions.\n"
        "Do NOT say things like 'I have drafted' or 'It appears'.\n"
        "Write in a polite, professional, customer-facing tone.\n"
        "If tools are used, incorporate the information silently.\n"
        "End the email clearly and naturally.\n"
    )
)

def handle_customer_email(email_text: str):
    result = agent.invoke({
        "messages": [
            HumanMessage(content=email_text)
        ]
    })

    # Final answer is the last AI message
    return result["messages"][-1].content
