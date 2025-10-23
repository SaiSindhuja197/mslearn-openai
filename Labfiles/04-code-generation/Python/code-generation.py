import os
from dotenv import load_dotenv

# Add OpenAI import
from openai import AzureOpenAI

# Set to True to print the full response from OpenAI for each call
printFullResponse = False

def main(): 
    try: 
        # Get configuration settings 
        load_dotenv()
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_DEPLOYMENT")
        
        # Print environment variables to verify (optional debug)
        print("Endpoint:", azure_oai_endpoint)
        print("Key:", azure_oai_key[:5] + "..." + azure_oai_key[-5:])  # Masked display
        print("Deployment:", azure_oai_model)

        # Set OpenAI configuration settings
        global client
        client = AzureOpenAI(
            api_key=azure_oai_key,
            azure_endpoint=azure_oai_endpoint,
            api_version="2024-06-01"  # Ensure this matches your resource version
        )

        # Ensure 'result' folder exists
        os.makedirs("result", exist_ok=True)

        while True:
            print('\n1: Add comments to my function\n' +
                '2: Write unit tests for my function\n' +
                '3: Fix my Go Fish game\n' +
                '\"quit\" to exit the program\n')
            command = input('Enter a number to select a task:')
            if command == '1':
                file = open(file="../sample-code/function/function.py", encoding="utf8").read()
                prompt = "Add comments to the following function. Return only the commented code.\n---\n" + file
                call_openai_model(prompt, model=azure_oai_model)
            elif command =='2':
                file = open(file="../sample-code/function/function.py", encoding="utf8").read()
                prompt = "Write four unit tests for the following function.\n---\n" + file
                call_openai_model(prompt, model=azure_oai_model)
            elif command =='3':
                file = open(file="../sample-code/go-fish/go-fish.py", encoding="utf8").read()
                prompt = "Fix the code below for an app to play Go Fish with the user. Return only the corrected code.\n---\n" + file
                call_openai_model(prompt, model=azure_oai_model)
            elif command.lower() == 'quit':
                print('Exiting program...')
                break
            else:
                print("Invalid input. Please try again.")

    except Exception as ex:
        print(ex)

def call_openai_model(prompt, model):
    # Provide a basic user message, and use the prompt content as the user message
    system_message = "You are a helpful AI assistant that helps programmers write code."
    user_message = prompt

    # Build the messages array
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message},
    ]

    # Call the Azure OpenAI model
    response = client.chat.completions.create(
        model=model,  # Use the model parameter passed
        messages=messages,
        temperature=0.7,
        max_tokens=1000
    )
    
    # Extract response content
    output = response.choices[0].message.content

    # Print the response to the console
    print("\n--- Response Start ---\n")
    print(output)
    print("\n--- Response End ---\n")

    # Write the response to a file
    with open("result/app.txt", "w", encoding="utf8") as results_file:
        results_file.write(output)
    
    print("Response written to result/app.txt\n")

if __name__ == '__main__': 
    main()
