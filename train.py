from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config,GPT2LMHeadModel,GPT2Tokenizer,DataCollatorForLanguageModeling
from datasets import load_dataset
# from transformers.data import data_collator
from transformers import Trainer,TrainingArguments


TRAIN_BASE = False
file_paths = ["./test1.txt"]

# Initialize a tokenizer
if TRAIN_BASE:
    # tokenizer = ByteLevelBPETokenizer()
    tokenizer = GPT2Tokenizer()

    # url https://suay.site/?p=735
    # iconv - f utf-8 - t utf-8 - c FILE.txt - o NEW_FILE.txt
    # iconv - f utf-8 - t utf-8 - c FILE.txt > NEW_FILE.txt
    # Examples:


    # 1
    # 2
    # iconv - f utf-8 - t utf-8 - c ~/rockyou.txt > ~/rockyou_clean.txt
    # iconv - f utf-8 - t utf-8 - c ~/rockyou.txt - o ~/rockyou_clean.txt

    # Customize training
    tokenizer.train(files=file_paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])

    # Save files to disk
    tokenizer.save_model("tokenlizer")


# inp = "print('hello world!')"

# t = tokenizer.encode(inp)

# print(t.ids)
# print(t.tokens)
tokenizer = GPT2Tokenizer.from_pretrained('./tokenlizer')
# Customize training
tokenizer.add_special_tokens({
    "eos_token":"<s>",
    "bos_token":"<pad>",
    "unk_token":"</s>",
    "pad_token":"<unk>",
    "mask_token":"<mask>"
    })

inp = "print('hello world!')"

t = tokenizer.encode(inp)

# print(t.ids)
print(t)
print(tokenizer.decode(t))

config = GPT2Config(
    vocab_size=tokenizer.vocab_size,
    bos_token = tokenizer.bos_token_id,
    eos_token = tokenizer.eos_token_id,
    # max_position_embeddings=514,
    # num_attention_heads=12,
    # num_hidden_layers=6,
    # type_vocab_size=1,
)

# define a model to train up 

model = GPT2LMHeadModel(config)
dataset = load_dataset("text", data_file=file_paths)

def encode(lines):
    return tokenizer(lines['text'],add_special_tokens=True,truncation=True,max_length=512)

dataset.set_transform(encode)
dataset = dataset['train']

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer,mlm=True,mlm_probability=0.15)

training_args = TrainingArguments(
    output_dir="./GPyT",
    overwrite_output_dir=True,
    num_train_epochs=1,
    per_device_train_batch_size=10,
    save_steps=100,
    save_total_limit=2,
    prediction_loss_only=True,
    remove_unused_columns=False,
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=dataset,
)
trainer.train()
trainer.save_model("./GPyT")
