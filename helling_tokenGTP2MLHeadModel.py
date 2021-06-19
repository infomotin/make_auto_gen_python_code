from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config,GPT2LMHeadModel,GPT2Tokenizer


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
