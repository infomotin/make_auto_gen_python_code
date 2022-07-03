from transformers import AutoTokenizer,AutoModelForCausalLM
import torch
# device = "cuda:0" if torch.cuda.is_available() else "cpu"
device = "cpu"
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-mono") # nl normal text,mono is for pythoncode,multi is for all languages
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-350M-mono")
# nl: Pre-trained on the Pile
# multi: Initialized with nl, then further pre-trained on multiple programming languages data
# mono: Initialized with multi, then further pre-trained on Python data
# Salesforce/codegen-{size}-{data}
# doc https: // huggingface.co/docs/transformers/main/en/model_doc/codegen

find_code_text = input("Enter the text to find the code: ")
find_code_text = find_code_text.lower()
input_ids = tokenizer(find_code_text, return_tensors="pt").to(device).input_ids
model = model.to(device)  # gpu
generated_ids = model.generate(input_ids, max_length=1024)
generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print("The generated code is: ", generated_text)



