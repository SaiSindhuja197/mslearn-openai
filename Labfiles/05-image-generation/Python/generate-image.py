import requests
import time
import os
from dotenv import load_dotenv

def main(): 
    try:
        # Load environment variables
        load_dotenv()
        api_base = os.getenv("AZURE_OAI_ENDPOINT")
        api_key = os.getenv("AZURE_OAI_KEY")
        deployment = os.getenv("AZURE_OAI_DEPLOYMENT")  # e.g., Dalle3
        api_version = '2025-04-01-preview'

        # Ensure the endpoint ends without a trailing slash
        if api_base.endswith('/'):
            api_base = api_base[:-1]

        # Get prompt for image to be generated
        os.system('clear' if os.name == 'posix' else 'cls')
        prompt = input("Enter a prompt to request an image: ")

        # Construct the request URL
        url = f"{api_base}/openai/deployments/{deployment}/images/generations?api-version={api_version}"
        headers = {
            "api-key": api_key,
            "Content-Type": "application/json"
        }
        body = {
            "prompt": prompt,
            "model": deployment,  # required for DALL·E 3
            "n": 1,
            "size": "1024x1024",  # valid sizes: 1024x1024, 1024x1792, 1792x1024
            "quality": "standard",  # optional: "standard" or "hd"
            "style": "vivid",       # optional: "vivid" or "natural"
            "response_format": "url"
        }

        # Debug: print the request URL and body
        print("Calling URL:", url)
        print("Request Body:", body)

        # Submit the image generation job
        submission = requests.post(url, headers=headers, json=body)

        # Check if the request was accepted
        if submission.status_code != 202:
            print("Failed to submit image generation job.")
            print("Status Code:", submission.status_code)
            print("Response:", submission.text)
            return

        # Get the operation-location URL for polling
        operation_location = submission.headers.get('Operation-Location')
        if not operation_location:
            print("Operation-Location header not found in response.")
            print("Response Headers:", submission.headers)
            return

        # Poll the callback URL until the job has succeeded
        status = ""
        while status != "succeeded":
            time.sleep(3)
            response = requests.get(operation_location, headers=headers)
            status = response.json().get('status')
            print("Current status:", status)

        # Get the results
        image_url = response.json()['result']['data'][0]['url']
        print("Generated Image URL:", image_url)

    except Exception as ex:
        print("An error occurred:", ex)

if __name__ == '__main__': 
    main()
