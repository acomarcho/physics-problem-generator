from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from string_utility import StringUtility

class ChatGPTParaphraser:
  def __init__(self):
    self.tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
    self.model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to('cpu')
    self.string_utility = StringUtility()

  def paraphrase(self, text):
    sentences = self.string_utility.get_sentences(text)
    paraphrases = []

    for sentence in sentences:
      paraphrased_text = self._paraphrase(sentence)[0]
      paraphrases.append(paraphrased_text.strip('.'))

    combined_paraphrase = ". ".join(paraphrases)
    return combined_paraphrase

  def _paraphrase(
    self, 
    text,
    num_beams=5,
    num_beam_groups=5,
    num_return_sequences=5,
    repetition_penalty=10.0,
    diversity_penalty=3.0,
    no_repeat_ngram_size=2,
    temperature=0.7,
    max_length=500
  ):
    input_ids = self.tokenizer(
      f'paraphrase: {text}',
      return_tensors="pt", padding="longest",
      max_length=max_length,
      truncation=True,
    ).input_ids

    outputs = self.model.generate(
      input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
      num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
      num_beams=num_beams, num_beam_groups=num_beam_groups,
      max_length=max_length, diversity_penalty=diversity_penalty
    )

    res = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return res

if __name__ == "__main__":
  text = "As Sir Henry and I sat at breakfast, the sunlight flooded in through the high mullioned windows, throwing watery patches of color from the coats of arms which covered them. The dark panelling glowed like bronze in the golden rays, and it was hard to realize that this was indeed the chamber which had struck such a gloom into our souls upon the evening before. But the evening before, Sir Henry's nerves were still handled the stimulant of suspense, and he came to breakfast, his cheeks flushed in the exhilaration of the early chase."
  
  chatgpt_paraphraser = ChatGPTParaphraser()
  print(chatgpt_paraphraser.paraphrase(text))