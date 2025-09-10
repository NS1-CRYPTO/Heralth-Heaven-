# Fine-tuning plan (Most Useful Fine-Tune category guidance)

## Goal
Improve gpt-oss performance for structured clinical triage JSON outputs and local-language support.

## Data
- Use de-identified clinical triage notes, public datasets (MIMIC summaries are sensitive — follow licensing), and synthetic augmentation.
- Aim for 5k-50k examples for instruction tuning; smaller focused datasets (1k) can still significantly improve structured outputs.

## Training steps
1. Convert examples to instruction-response pairs, with response strictly formatted JSON.
2. Use LoRA or full fine-tuning depending on compute. Use peft/peft-lora for efficiency.
3. Validate with held-out set and safety test suite (see `evaluation/`).

## Evaluation
- Schema compliance (valid JSON).
- Clinical fidelity (expert review).
- Safety metrics: false-negative rate for red-flag detection.

