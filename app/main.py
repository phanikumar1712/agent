from app.agents.agent import create_agent


def main():

    agent = create_agent()

    print("AI Agent started.")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() in {
            "exit",
            "quit"
        }:
            print("Goodbye!")
            break

        try:

            result = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input,
                        }
                    ]
                }
            )

            messages = result["messages"]

            final_message = messages[-1]

            print(
                f"\nAgent: {final_message.content}\n"
            )

        except Exception as e:

            print(
                f"\nError: {str(e)}\n"
            )


if __name__ == "__main__":
    main()