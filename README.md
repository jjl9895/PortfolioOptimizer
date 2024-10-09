# Portfolio Optimizer

For the Cloudera Evolve24 Hackathon, this project focuses on optimizing Large Language Models (LLMs) through Retrieval-Augmented Generation (RAG) and advanced prompt engineering. The goal is to gather financial news headline data and, based on this data, recommend actions to perform on a simulated trading account via the Alpaca API (in paper trading mode). By combining user information with vectorized headline data, processed through Pinecone, and integrating it into the ChatGPT API, the system provides tailored financial recommendations for enhanced decision-making.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [License](#license)
- [Cloudera Workbench](#cloudera-workbench)

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
  - [NvidiaAPI](https://www.nvidia.com/en-us/ai/#referrer=ai-subdomain?ncid=pa-srch-goog-772333&_bt=697697685508&_bk=nvidia%20api&_bm=e&_bn=g&_bg=165151891361&gad_source=1&gclid=EAIaIQobChMI37H2or-CiQMV3lxHAR1GAwRHEAAYASAAEgJfB_D_BwE)
  - [PineconeAPI](https://www.pinecone.io/?utm_term=pinecone%20serverless&utm_campaign=brand-us-p&utm_source=adwords&utm_medium=ppc&hsa_acc=3111363649&hsa_cam=16223687665&hsa_grp=133738612775&hsa_ad=582256510975&hsa_src=g&hsa_tgt=kwd-2270491656216&hsa_kw=pinecone%20serverless&hsa_mt=p&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=EAIaIQobChMIvbmTrr-CiQMVClFHAR0uxAaCEAAYASAAEgKpbfD_BwE)

## Installation
**Clone the Repository**

   ```bash
   git clone https://github.com/jjl9895/PortfolioOptimizer.git
   cd PortfolioOptimizer
  ```
## License
This project is licensed under the MIT License.
