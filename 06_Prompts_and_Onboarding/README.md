# 06_Prompts_and_Onboarding

This folder contains all materials related to the initialization, priming, and onboarding of the Voice GPT instance. These resources help define its operational parameters, tone, memory conventions, and interaction philosophy for both new and ongoing users.

## Contents

This folder may include:

- **system_prompt.md**  
  The master system prompt that defines the core personality, purpose, interaction style, and constraints of this Voice instance.

- **onboarding_script.md**  
  A scripted introduction used for onboarding new users, including guidance on how to interact with the model, key principles it follows, and what it is optimized for.

- **user_initiation_template.md** *(optional)*  
  A template the user can fill out to tailor the Voice instance (e.g. interests, tone preferences, goals for interaction, etc.).

- **edge_case_guidelines.md** *(optional)*  
  Instructions on how to handle known edge cases or constraints within the LLM context window, memory fallback strategies, or custom fail-safes.

## Purpose

This directory allows for consistent initialization and restoration of the GPT across sessions. It acts as both a design layer and a safety layer for long-running or deeply personalized instances.

## Notes

- This folder is meant to evolve. Each component should be versioned or time-stamped when significantly updated.
- Final deployment versions of any monetized or shared GPT should draw directly from the files in this directory.

---

