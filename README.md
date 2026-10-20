LangChain Agents: Modern API

**Overview**

LangChain agents combine a language model (LLM) with tools to perform tasks dynamically. An agent can decide which tools to call, use their results, and generate a final response.

In newer LangChain versions (v1), create_agent provides a modern way to build agents without manually creating a classic ReAct agent and wrapping it in AgentExecutor.

**Understanding create_agent**

The agent manages the tool-calling loop, including invoking tools and using their results to produce an answer.

The modern create_agent API simplifies agent development by managing the tool-calling workflow. Debug mode, streaming, and LangSmith tracing provide different ways to inspect execution and troubleshoot issues.