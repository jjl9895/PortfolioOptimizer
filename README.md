# Portfolio Optimizer

For the Cloudera Evolve24 Hackathon, this project focuses on optimizing Large Language Models (LLMs) through Retrieval-Augmented Generation (RAG) and advanced prompt engineering. The goal is to gather financial news headline data and, based on this data, recommend actions to perform on a simulated trading account via the Alpaca API (in paper trading mode). By combining user information with vectorized headline data, processed through Pinecone, and integrating it into the ChatGPT API, the system provides tailored financial recommendations for enhanced decision-making.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [License](#license)

## Features
 
- Grabs Latest Headline Data using Perplexity AI.
- Vectorization Storing with Pinecone.
- Alpaca trading simulation with Alpaca API.
- ChatGPT API integration for recommendations.

## Cloudera Workbench
- This project utilized the Cloudera CML workbench, jobs for raw data ingestion, sessions for easy coding and optimizations, AMPs for usecases, and it's app deployment to host our application

## Prerequisites

- Language/Platform version (e.g., Python 3.8 or higher)
- Accounts and API keys for:
  - [OpenAI](https://platform.openai.com/docs/overview)
  - [AlpacaAPI](https://alpaca.markets/)
  - [PerplexityAPI](https://docs.perplexity.ai/home)

## Installation
**Clone the Repository**

   ```bash
   git clone https://github.com/jjl9895/PortfolioOptimizer.git
   cd PortfolioOptimizer
  ```
## License
This project is licensed under the MIT License.
