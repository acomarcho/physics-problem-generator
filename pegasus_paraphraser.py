from transformers import PegasusForConditionalGeneration, PegasusTokenizer

class PegasusParaphraser:
  def __init__(self):
    model_name = "tuner007/pegasus_paraphrase"
    self.tokenizer = PegasusTokenizer.from_pretrained(model_name)
    self.model = PegasusForConditionalGeneration.from_pretrained(model_name)

  def paraphrase(self, text):
    sentences = text.split(".")
    paraphrases = []

    for sentence in sentences:
      sentence = sentence.strip()

      if len(sentence) == 0:
          continue

      inputs = self.tokenizer.encode_plus(sentence, return_tensors="pt", truncation=True, max_length=512)

      input_ids = inputs["input_ids"]
      attention_mask = inputs["attention_mask"]

      paraphrase = self.model.generate(
          input_ids=input_ids,
          attention_mask=attention_mask,
          num_beams=4,
          max_length=100,
          early_stopping=True
      )[0]
      paraphrased_text = self.tokenizer.decode(paraphrase, skip_special_tokens=True)

      paraphrases.append(paraphrased_text)

      combined_paraphrase = " ".join(paraphrases)

    return combined_paraphrase
    

if __name__ == "__main__":
  text = "As Sir Henry and I sat at breakfast, the sunlight flooded in through the high mullioned windows, throwing watery patches of color from the coats of arms which covered them. The dark panelling glowed like bronze in the golden rays, and it was hard to realize that this was indeed the chamber which had struck such a gloom into our souls upon the evening before. But the evening before, Sir Henry's nerves were still handled the stimulant of suspense, and he came to breakfast, his cheeks flushed in the exhilaration of the early chase."
  
  pegasus_paraphraser = PegasusParaphraser()
  print(pegasus_paraphraser.paraphrase(text))