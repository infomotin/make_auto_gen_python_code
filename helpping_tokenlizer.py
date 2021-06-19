from tokenizers import ByteLevelBPETokenizer


TRAIN_BASE = True
file_paths = ["./test1.txt"]

# Initialize a tokenizer
if TRAIN_BASE:
    tokenizer = ByteLevelBPETokenizer()

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


inp = "print('hello world!')"

t = tokenizer.encode(inp)

print(t.ids)
print(t.tokens)
