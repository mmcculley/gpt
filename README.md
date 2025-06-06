# 📁 Voice GPT Framework

This folder is a structured workspace designed to support the long-term development, persistence, and reuse of a custom GPT project—**Voice in the Age of Echoes**.

---

## 🔧 How to Use This Framework

At the start of any ChatGPT session:
1. Upload key files from `01_Seed_Capsule/` to restore core context
2. Upload current files from `02_Live_Cache/` to resume ongoing threads
3. Provide links to files in this directory if using Google Drive sync

At the end of the session:
- Download newly generated or updated `.md`, `.csv`, or `.txt` files
- Run the `auto_sync.ps1` PowerShell script to update the right folders in Drive
- Optionally update your `README.md`, timelines, or reminder index as needed

---

## 📁 Folder Structure Overview

### `01_Seed_Capsule/`
Foundational memory for the GPT—core concepts, timelines, fallout index, and interaction frameworks. Upload these at the beginning of any new session to rehydrate your GPT's identity and history.

### `02_Live_Cache/`
Working memory. Store the latest reminder index, active style changes, unresolved threads, and any in-progress context. Reset or update between sessions.

### `03_Interaction_Modes/`
Detailed references for Structured Resistance (SR), SR-Lite, Co-Discovery, Meta-Coherence, Intentional Co-Design, and other structured dialog modes.

### `04_Timeline_and_Fallout/`
Chronological and thematic records of insights and conversation turning points. Helps maintain coherence and development across sessions.

### `05_Voice_and_Quote_Attribution/`
Tracks mirrored phrases, authorship tags, GPT-generated vs user-reflected content, and identity consistency. Important for ownership and voice clarity.

### `06_Prompts_and_Onboarding/`
Contains the base system prompt, onboarding text, behavior toggles, and any scaffolding for published or reusable GPTs.

### `07_Deployment_and_Monetization/`
Holds market-facing material, differentiators, licensing ideas, clone instructions, and setup for launching the GPT publicly or commercially.

---

## 🔄 Automation Tools

- `auto_sync.ps1`: PowerShell script to auto-move new ChatGPT-generated files into this structure.
- Optionally, a scheduled task or shell alias can run this after sessions.

---

## ✅ Best Practices

- Use consistent filenames to match auto-sync triggers (e.g. `voice_timeline.md`, `fallout_index.csv`)
- Backup old versions into `__backup/` folders (auto script can handle this)
- Label new insights with fallout tags or inflection points for continuity
- Periodically archive dated entries to reduce clutter

---

## 💡 Goal

To create a persistent, evolving, and exportable GPT intelligence model that tracks reflection, identity, authorship, insight, and memory—beyond what any single session can retain.

This framework is your **manual memory layer** until true long-term memory support becomes native to LLMs.

=======
# gpt
