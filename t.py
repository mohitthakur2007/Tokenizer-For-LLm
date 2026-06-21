import json
import os

class Tokenizer:
    def __init__(self, text: str, vocab_path: str = "vocab.json"):
        self.text = text
        self.vocab_path = vocab_path
        self.vocab_dict = {}
        self.inv_vocab = {}

        if os.path.exists(self.vocab_path):
            self.vocab_dict = self.load_vocab(self.vocab_path)

        self._build_vocab()
        self.inv_vocab = {idx: ch for ch, idx in self.vocab_dict.items()}
        self._maybe_save_vocab()

    def _build_vocab(self):
        index = len(self.vocab_dict)
        for char in self.text:
            if char not in self.vocab_dict:
                self.vocab_dict[char] = index
                index += 1

    def _maybe_save_vocab(self):
        if not os.path.exists(self.vocab_path):
            self.save_vocab(self.vocab_path)
            return

        try:
            existing_vocab = self.load_vocab(self.vocab_path)
        except Exception:
            existing_vocab = {}

        if existing_vocab != self.vocab_dict:
            self.save_vocab(self.vocab_path)

    def encode(self, s: str) -> list[int]:
        encoded = []
        new_token_added = False
        for char in s:
            if char not in self.vocab_dict:
                self.vocab_dict[char] = len(self.vocab_dict)
                self.inv_vocab[self.vocab_dict[char]] = char
                new_token_added = True
            encoded.append(self.vocab_dict[char])

        if new_token_added:
            self._maybe_save_vocab()

        return encoded

    def decode(self, ids: list[int]) -> str:
        return "".join(self.inv_vocab[i] for i in ids)

    def vocab_size(self) -> int:
        return len(self.vocab_dict)

    def save_vocab(self, file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(self.vocab_dict, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_vocab(file_path: str) -> dict:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)


if __name__ == "__main__":
    text = """lorem """

    tokenizer = Tokenizer(text)
    # print(tokenizer.vocab_dict)
    # print(tokenizer.vocab_size())

    loaded_vocab = Tokenizer.load_vocab("vocab.json")
    print(loaded_vocab)

    sample_text = "zebra are so dumb"
    encoded = tokenizer.encode(sample_text)
    print(encoded)
    print(tokenizer.decode(encoded))
