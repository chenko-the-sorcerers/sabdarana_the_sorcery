# Sabdarana_The_Sorcery

# 🪶 Sabdarana: A Learn-to-Earn Web3 Platform for Cultural Preservation

[![Watch Demo](https://img.shields.io/badge/Watch%20Demo-YouTube-red?logo=youtube)](https://youtu.be/MMIeTGbBE7Y?si=JA9axjGihclyc_GO)
[![Figma Design](https://img.shields.io/badge/Design-Figma-blue?logo=figma)](https://www.figma.com/proto/TwZDDw8kTXUPz6MHLN1Kc6/Sabdarana-%7C-Garudahacks-6.0?page-id=8%3A5&node-id=23-763&viewport=-1768%2C328%2C0.29&t=cyDOjSNQvteulVn1-1&scaling=scale-down&content-scaling=fixed&starting-point-node-id=23%3A763)

> _“Learn, Preserve, Earn.”_  
> Sabdarana is a Web3-powered learning platform designed to **preserve Indonesian Local Language scripts** and **reward cultural engagement** through **Widya Coin**, our native token.

---

## 🚀 Project Overview

Sabdarana bridges the gap between cultural heritage and modern digital ecosystems. By combining **edtech**, **Web3**, and **gamified learning**, we allow users to:
- Learn local scripts (aksara) interactively.
- Earn Widya Coin through a _learn-to-earn_ mechanism.
- Collect NFTs for cultural artifacts and script mastery.
- Trade coins, contribute to DAO voting, or redeem for perks.

This project was built during **[GarudaHacks 6.0](https://garudahacks.com)** and represents a culturally meaningful use case for blockchain.

---

## 🧠 What We Learned

Throughout the development of Sabdarana and Widya Coin, we explored how to fuse **blockchain mechanics** with **cultural education** in a way that’s **accessible, fun, and economically rewarding**. We learned to navigate smart contracts, NFT systems, and tokenomics—all while staying rooted in a mission to preserve local identity. The biggest insight? **Culture and tech don’t have to be at odds—they can uplift each other.**

---

## 🌐 Live Demo & Resources

- 🎥 [YouTube Demo](https://youtu.be/MMIeTGbBE7Y?si=JA9axjGihclyc_GO)
- 🎨 [Figma Prototype](https://www.figma.com/proto/TwZDDw8kTXUPz6MHLN1Kc6/Sabdarana-%7C-Garudahacks-6.0?page-id=8%3A5&node-id=23-763)
- 📂 [Pitch Deck (Google Drive)](https://drive.google.com/file/d/1YOURajZPSKu3VKjWf-gyqoM1QAUvrHlT/view?usp=sharing)

---

## 📦 Tech Stack

| Frontend | Backend | Blockchain | AI/ML |
|----------|---------|------------|-------|
| Next.js  | Node.js | Solidity / Ethereum | Python (LLM & CV) |
| TailwindCSS | Firebase | Web3.js / Ethers.js | Custom OCR for Aksara Jawa |
| Figma (UI/UX) | Express | IPFS (NFT Storage) | HuggingFace Transformers |

---

## 💰 Widya Coin & Tokenomics

Widya Coin is a reward token inspired by **Bitcoin halving mechanics**, tailored to educational milestones.  
We simulate a **limited supply** and **periodic halving**, making early learning more rewarding—just like mining BTC in its early days.

ROI is calculated as:

\[
ROI = \frac{\text{Price}_{\text{end}} - \text{Price}_{\text{start}}}{\text{Price}_{\text{start}}} \times 100\%
\]

> 📈 See the full ROI analysis & simulation in the `bitcoin_model/` directory.

---

## 🔮 What's Next for SABDARANA

We envision **Widya Coin** evolving into a **cultural digital commodity** that represents more than value—it represents knowledge, heritage, and social contribution. Imagine earning tokens not just for learning, but for preserving culture, joining DAO votes, and unlocking real-world cultural events and products.

> **Let’s make culture rewarding again.**

---

## 🏆 Accomplishments

✅ Built full-stack Web3 + EdTech platform  
✅ Simulated Bitcoin-style tokenomics  
✅ Designed Local Language Script OCR system  
✅ Integrated NFT-based learning collectibles  

---

## 🤝 Team Sabdarana


---

## 📁 Repository Structure

```bash
sabdarana_the_sorcery/
├── .env.example                  # Environment configuration template
├── .gitignore                   # Git ignored files
├── .npmrc                       # npm registry config
├── .prettierignore              # Prettier ignore rules
├── .prettierrc                  # Prettier formatting configuration
├── README.md                    # Project documentation
├── eslint.config.js            # Linting rules
├── package.json                 # Project metadata & dependencies
├── pnpm-lock.yaml               # Dependency lock file
├── svelte.config.js             # Svelte configuration
├── tsconfig.json                # TypeScript configuration
├── vite.config.ts               # Vite bundler configuration
├── vitest-setup-client.ts       # Vitest client setup
├── verify-supabase.js           # Supabase token verification
├── static/                      # Static assets (frontend)
│   └── ...
└── src/                         # Main frontend source code
    ├── lib/
    ├── routes/
    ├── app.html
    └── ...
