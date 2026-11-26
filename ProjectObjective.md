## Overview

In this hands-on project, you will design the core logic for a simple text generation application. This activity focuses on prompt engineering using the Python SDK to send clear requests to an AI model deployed in Microsoft Foundry. By creating and testing prompts, you will make your model generate specific and well-formatted output. This is a key skill for building any application that uses generative AI. At the end of this activity, you can review an example solution to help you work through the steps as needed. 

### Activity goals

By the end of this project, you will be able to:

* Use a system message to define an AI's role and purpose.

* Write effective prompts to guide the AI to generate specific text.

* Use prompt engineering to control the format of the AI's output.

* Use the Python SDK for Azure AI Inference to call a deployed model in Microsoft Foundry.

* Utilize backend model components connected to a prebuilt user interface.

_Practice Mode: this practice is designed to provide you with feedback to guide your learning and prepare you for graded assignments._

### Scenario

You are an AI engineer at a wellness technology company. Your team wants to create a new mobile app that gives users a daily motivational quote. Your task is to design the “brain” of this feature. You need to use Microsoft Foundry tools to create a system that can generate inspiring messages on different themes, like “perseverance,” “creativity,” or “success.” 

#### What You'll Need
This lab takes place entirely within Microsoft Foundry and Visual Studio Code (VS Code). Before you start:

* Install Visual Studio Code — a free code editor — if you don't already have it.

* Install Python if you don't already have it. Both installs take just a few minutes from their official download pages.

* Download the Application Framework Construction zip file and extract the Text-Generation-App folder from it —you'll open this folder in VS Code in Step 3.

You'll also create a new Microsoft Foundry project and resource specifically for this lab, which the first step walks through.

Then, you will create a new AI Foundry project and resource specifically for this lab.
