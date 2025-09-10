# ClinicAgent: orchestrates prompts, local model, and parsing
import os, json
from typing import Dict, Any

MODEL_PATH = os.environ.get('CLINIC_MODEL_PATH', 'models/gpt-oss')

class ClinicAgent:
    def __init__(self):
        # Placeholder: Load local gpt-oss model here (PyTorch / ggml / custom runtime)
        # Example (pseudocode):
        # from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
        # self.tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        # self.model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, device_map='auto')
        # self.generator = pipeline('text-generation', model=self.model, tokenizer=self.tokenizer)
        self.model_loaded = False
        self._load_model_stub()

    def _load_model_stub(self):
        # For the scaffold we only simulate a model response.
        self.model_loaded = True

    def _format_prompt(self, case: Dict[str, Any]) -> str:
        # load template from prompt_templates/triage_templates.md
        template = open('prompt_templates/triage_templates.md','r',encoding='utf-8').read()
        prompt = template + "\n\nPatient case (json):\n" + json.dumps(case, indent=2)
        return prompt

    def _call_model(self, prompt: str) -> str:
        # Replace this with actual model call to local gpt-oss
        # e.g., output = self.generator(prompt, max_length=512)[0]['generated_text']
        # For scaffold, return a deterministic placeholder
        return "SIMULATED MODEL OUTPUT: Urgency=Moderate; Differential=[Cellulitis, Deep Tissue Infection]; Recommendations=[Start oral antibiotics, refer to clinic for dressing]"

    def triage_from_text(self, case: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._format_prompt(case)
        raw = self._call_model(prompt)
        return {"prompt": prompt, "raw_model": raw, "parsed": self._parse(raw)}

    def triage_with_image(self, case: Dict[str, Any]) -> Dict[str, Any]:
        # In a real build: run local image model or simple heuristics (open-source vision model),
        # extract features, and append to prompt. Here we put a placeholder.
        case_copy = case.copy()
        case_copy['image_note'] = 'photo_received (not analyzed in scaffold)'
        return self.triage_from_text(case_copy)

    def _parse(self, raw: str) -> Dict[str, Any]:
        # Very simple parser for scaffold. Replace with robust JSON output parsing using
        # model-instructed JSON formats and schema validators.
        return {"urgency": "moderate", "differential": ["Cellulitis", "Deep Tissue Infection"], "recommendations": ["Start oral antibiotics", "Refer to clinic for dressing"]}
