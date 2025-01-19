from googletrans import Translator

def translation_chatbot():
    print("Translation Chatbot: Hi! I can translate text for you. Type 'exit' to end the chat.")
    print("Example: 'Translate 'Hello' to Spanish.'")

    translator = Translator()
    while True:
        # Get user input
        user_input = input("You: ").strip().lower()

        # Exit condition
        if user_input == "exit":
            print("Translation Chatbot: Goodbye! Happy translating!")
            break

        try:
            # Parse the user input for "Translate" command
            if "translate" in user_input:
                user_input = user_input.replace("translate", "").strip()

                # Extract text and target language
                if "to" in user_input:
                    text, target_lang = user_input.split("to")
                    text = text.strip()
                    target_lang = target_lang.strip()

                    # Translate the text
                    translated = translator.translate(text, dest=target_lang)
                    print(f"Translation
