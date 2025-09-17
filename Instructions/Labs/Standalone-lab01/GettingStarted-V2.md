# Lunch and Learn: Get started with Azure OpenAI Service

### Overall Estimated Duration: 60 Minutes

## Overview

This lab introduces you to Azure OpenAI Service, a powerful platform that integrates OpenAI's generative AI models with the Azure cloud environment. Designed to introduce you to its core concepts and capabilities, this lab will guide you through provisioning a resource, deploying models, and interacting with various features. Learn to set up and configure an Azure OpenAI resource, deploy models, experiment with the Completions and Chat playgrounds, and acquire foundational skills in utilizing Azure's infrastructure for developing and refining AI-powered applications.

## Objective

Understand how to deploy Azure OpenAI Service, enabling you to integrate and explore OpenAI's advanced models within the secure and scalable Azure platform. By the end of this lab, you will be able to:

- **Get started with Azure OpenAI Service:** Gain experience in provisioning and configuring an Azure OpenAI resource, deploying an AI model (e.g., gpt-4o-mini, gpt-3.5-turbo-instruct), exploring model interactions in the Completions and Chat playgrounds, experimenting with prompts and parameters for fine-tuning, and leveraging the model's capabilities for code generation.

## Pre-Requisites

Participants should have basic knowledge and understanding of the following :

- **Azure Portal:** For managing and provisioning Azure resources.
- **Azure AI Foundry:** For deploying models, configuring and experimenting with their capabilities, including features such as the Completions and Chat playgrounds.

## Architecture

This architecture allows users to leverage Azure's cloud infrastructure to deploy and interact with advanced AI models.
The flow of the lab will be to use an existing Resource Group, then create and deploy an OpenAI model in Azure. Next, explore the model in the playground and generate code using AI. Through the Azure Portal, users manage their resources, while Azure AI Foundry provides the tools needed to deploy and test these models. The Completions and Chat playgrounds within Azure AI Foundry enable hands-on experimentation and refinement, facilitating the development of robust AI-powered applications.

## Architecture Diagram:

![](./media/archdiagram.png)

## Explanation of Components

- **Azure Portal:** Central interface for provisioning and managing Azure OpenAI resources, including model deployment settings and resource configuration.

- **Resource Group:** This is a container in Azure that holds related resources for your project. It helps us organize and manage services like your OpenAI model in one place.

- **Azure OpenAI Service:** Hosts and manages OpenAI models like GPT-4o-mini, providing scalable access for tasks such as text completion and code generation.

- **Azure AI Foundry:** Interactive environment to explore by deploying and experimenting with AI models. It includes the Completions Playground for generating text and the Chat Playground for simulating conversational interactions.

## Getting Started with the Lab

Welcome to your Get Started with Azure OpenAI Service Workshop! We've prepared a seamless environment for you to explore and learn about Azure services. Let's begin by making the most of this experience.
 
## Accessing Your Lab Environment
 
Once you're ready to dive in, your virtual machine and the **Guide** will be right at your fingertips within your web browser.
 
![Access Your VM and Lab Guide](./media/ll1.png)

## Virtual Machine & Lab Guide
 
Your virtual machine is your workhorse throughout the workshop. The lab guide is your roadmap to success.
 
## Lab Guide Zoom In/Zoom Out

To adjust the zoom level for the environment page, click the **A↕ : 100%** icon located next to the timer in the lab environment.

   ![Manage Your Virtual Machine](./media/zoominout.png)

## Exploring Your Lab Resources
 
To get a better understanding of your lab resources and credentials, navigate to the **Environment** tab.
 
![Explore Lab Resources](./media/envtab.png)
 
## Utilizing the Split Window Feature
 
For your convenience, you can open the lab guide in a separate window by selecting the **Split Window** button from the top right corner.
 
![Use the Split Window Feature](./media/splittab.png)
 
## Managing Your Virtual Machine
 
Feel free to **Start, Restart, or Stop (2)** your virtual machine as needed from the **Resources (1)** tab. Your experience is in your hands!
 
![Manage Your Virtual Machine](./media/resourcetab.png)

## Let's Get Started with Azure Portal
 
1. On your virtual machine, click on the **Azure Portal** icon as shown below:
 
      ![Launch Azure Portal](./media/sc900-image(1).png)
    
2. You'll see the **Sign in to continue to Microsoft Azure** tab. Here, enter your credentials:
 
   - **Email/Username:** <inject key="AzureAdUserEmail"></inject>
 
       ![Enter Your Username](./media/sc900-image-1.png)
 
3. Next, provide your password:
 
   - **Password:** <inject key="AzureAdUserPassword"></inject>
 
       ![Enter Your Password](./media/sc900-image-2.png)

      > **Note:** If prompted with MFA, please follow the steps highlighted under - [Steps to Proceed with MFA Setup if Ask Later Option is Not Visible](#steps-to-proceed-with-mfa-setup-if-ask-later-option-is-not-visible)
 
4. In the **Stay signed in?** pop-up, click **No**.

   ![](./media/2025-07-08(1).png)
 
5. In the **Welcome to Microsoft Azure** window, click **Cancel** to skip the tour.

   ![](./media/2025-07-08(2).png)

## Steps to Proceed with MFA Setup if Ask Later Option is Not Visible

   > **Note:** Continue with the exercises if MFA is already enabled or the option is unavailable.

1. At the **"More information required"** prompt, select **Next**.

1. On the **"Keep your account secure"** page, select **Next** twice.

1. **Note:** If you don’t have the Microsoft Authenticator app installed on your mobile device:

   - Open **Google Play Store** (Android) or **App Store** (iOS).
   - Search for **Microsoft Authenticator** and tap **Install**.
   - Open the **Microsoft Authenticator** app, select **Add account**, then choose **Work or school account**.

1. A **QR code** will be displayed on your computer screen.

1. In the Authenticator app, select **Scan a QR code** and scan the code displayed on your screen.

1. After scanning, click **Next** to proceed.

1. On your phone, enter the number shown on your computer screen in the Authenticator app and select **Next**.
       
1. If prompted to stay signed in, you can click **No**.

1. If a **Welcome to Microsoft Azure** popup window appears, click **Cancel** to skip the tour.
 
## Support Contact

The CloudLabs support team is available 24/7, 365 days a year, via email and live chat to ensure seamless assistance at any time. We offer dedicated support channels tailored specifically for both learners and instructors, ensuring that all your needs are promptly and efficiently addressed.

Learner Support Contacts:

- Email Support: cloudlabs-support@spektrasystems.com

- Live Chat Support: https://cloudlabs.ai/labs-support

Now, click on **Next** from the lower right corner to move on to the next page.

![Start Your Azure Journey](./media/nextpage.png)

## Happy Learning!!
