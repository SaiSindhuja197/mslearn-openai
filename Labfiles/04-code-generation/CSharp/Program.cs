// Implicit using statements are included
using System.Text;
using System.Text.Json;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Configuration.Json;
using Azure;
using Azure.AI.OpenAI;
// Add Azure OpenAI package


// Build a config object and retrieve user settings.
IConfiguration config = new ConfigurationBuilder()
    .AddJsonFile("appsettings.json")
    .Build();
string? oaiEndpoint = config["AzureOAIEndpoint"];
string? oaiKey = config["AzureOAIKey"];
string? oaiModelName = config["AzureOAIDeploymentName"];

string command;
bool printFullResponse = false;

do {
    Console.WriteLine("\n1: Add comments to my function\n" +
    "2: Write unit tests for my function\n" +
    "3: Fix my Go Fish game\n" +
    "\"quit\" to exit the program\n\n" + 
    "Enter a number to select a task:");

    command = Console.ReadLine() ?? "";
    
    switch (command) {
        case "1":
            string functionFile = System.IO.File.ReadAllText("../sample-code/function/function.cs");
            string ChatCompletionsOptions = "Add comments to the following function. Return only the commented code.\n---\n" + functionFile;
            
            await GetResponseFromOpenAI(ChatCompletionsOptions);
            break;
        case "2":
            functionFile = System.IO.File.ReadAllText("../sample-code/function/function.cs");
            string unitTestPrompt = "Write four unit tests for the following function.\n---\n" + functionFile;
            
            await GetResponseFromOpenAI(unitTestPrompt);
            break;
        case "3":
            string goFishFile = System.IO.File.ReadAllText("../sample-code/go-fish/go-fish.cs");
            string goFishPrompt = "Fix the code below for an app to play Go Fish with the user. Return only the corrected code.\n---\n" + goFishFile;
            
            await GetResponseFromOpenAI(goFishPrompt);
            break;
        case "quit":
            Console.WriteLine("Exiting program...");
            break;
        default:
            Console.WriteLine("Invalid input. Please try again.");
            break;
    }
} while (command != "quit");

async Task GetResponseFromOpenAI(string prompt)  
{   
    Console.WriteLine("\nCalling Azure OpenAI to generate code...\n\n");

    if(string.IsNullOrEmpty(oaiEndpoint) || string.IsNullOrEmpty(oaiKey) || string.IsNullOrEmpty(oaiModelName))
    {
        Console.WriteLine("Please check your appsettings.json file for missing or incorrect values.");
        return;
    }

    var credentials = new AzureKeyCredential(oaiKey);
    var chatClient = new OpenAIClient(new Uri(oaiEndpoint), credentials);

    string systemPrompt = "You are a helpful AI assistant that helps programmers write code.";
    string userPrompt = prompt;

    var chatOptions = new ChatCompletionsOptions()
    {
        Temperature = 0.7f,
        MaxTokens = 800
    };

    chatOptions.Messages.Add(new ChatMessage(ChatRole.System, systemPrompt));
    chatOptions.Messages.Add(new ChatMessage(ChatRole.User, userPrompt));

    Response<ChatCompletions> completions = await chatClient.GetChatCompletionsAsync(oaiModelName, chatOptions);

    string resultText = completions.Value.Choices[0].Message.Content;
    
    if (printFullResponse)
    {
        Console.WriteLine($"\nFull response: {JsonSerializer.Serialize(completions.Value, new JsonSerializerOptions { WriteIndented = true })}\n\n");
    }

    Console.WriteLine($"\nResponse:\n{resultText}\n");

    System.IO.File.WriteAllText("result/app.txt", resultText);
    Console.WriteLine($"\nResponse written to results/app.txt\n\n");
}
