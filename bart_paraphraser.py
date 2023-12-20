from transformers import BartForConditionalGeneration, BartTokenizer
from string_utility import StringUtility

class BartParaphraser:
  def __init__(self):
    self.model = BartForConditionalGeneration.from_pretrained('eugenesiow/bart-paraphrase')
    self.model = self.model.to('cpu')
    self.tokenizer = BartTokenizer.from_pretrained('eugenesiow/bart-paraphrase')
    self.string_utility = StringUtility()

  def paraphrase(self, text):
    sentences = self.string_utility.get_sentences(text)
    paraphrases = []

    for sentence in sentences:
      batch = self.tokenizer(sentence, return_tensors='pt', truncation=False)
      generated_ids = self.model.generate(batch['input_ids'], max_length=500)
      paraphrased_text = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

      paraphrases.append(paraphrased_text.strip("."))

    combined_paraphrase = ". ".join(paraphrases)
    return combined_paraphrase

if __name__ == "__main__":
  text = "As Sir Henry and I sat at breakfast, the sunlight flooded in through the high mullioned windows, throwing watery patches of color from the coats of arms which covered them. The dark panelling glowed like bronze in the golden rays, and it was hard to realize that this was indeed the chamber which had struck such a gloom into our souls upon the evening before. But the evening before, Sir Henry's nerves were still handled the stimulant of suspense, and he came to breakfast, his cheeks flushed in the exhilaration of the early chase."
  
  bart_paraphraser = BartParaphraser()
  print(bart_paraphraser.paraphrase(text))