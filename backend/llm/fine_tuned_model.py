# Placeholder for fine-tuned model loadingfrom transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel, PeftConfig
import torch

MODEL_ID = "NousResearch/Llama-2-7b-chat-hf"
ADAPTER_PATH = "data/fine_tune_dataset/lora_adapter"

def load_lora_model():
    config = PeftConfig.from_pretrained(ADAPTER_PATH)
    base_model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path,
        return_dict=True,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
    return model, tokenizer

def generate_lora_response(prompt: str):
    model, tokenizer = load_lora_model()
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.cuda()
    with torch.no_grad():
        output = model.generate(input_ids=input_ids, max_new_tokens=100)
    return tokenizer.decode(output[0], skip_special_tokens=True)