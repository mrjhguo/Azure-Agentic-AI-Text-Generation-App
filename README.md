# Azure Agentic AI Text Generation App

_A practical project from the Microsoft Generative and Agentic AI Basics Specialization_

A Python text-generation application powered by Azure AI Foundry / Azure OpenAI (gpt-5.4-mini). This repository includes both a command-line script (text_gen.py) for quick prompt execution and a full-featured Streamlit web interface (user_interface.py) for interactive chat, system prompt customization, and parameter tuning.

## Features

* CLI Text Generation (text_gen.py): Uses the OpenAI Python SDK configured for Azure's /openai/v1 endpoint to generate non-cliché, uplifting motivational quotes.

* Interactive Web UI (user_interface.py): Built with Streamlit and the azure-ai-inference SDK, supporting:
	* Live Configuration: Update your API key, endpoint URL, model name, and API version directly from the sidebar.
	
    * Custom System Prompts: Define and modify the AI's persona and behavior on the fly.
	
    * Model Parameter Controls: Toggle and adjust Temperature (0.0–1.0) and Top P (0.01–1.0) with built-in greedy-sampling validation.
	
    * Conversation Management: Multi-turn chat history, one-click history reset, and downloadable Markdown (.md) conversation exports.
	
    * Flexible Endpoint Support: Automatically handles both Azure /openai/v1 endpoints (via a custom RemoveApiVersionPolicy) and standard /openai/deployments/<model> endpoints.