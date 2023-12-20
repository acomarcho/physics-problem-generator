from parrot import Parrot
from string_utility import StringUtility

import warnings
warnings.filterwarnings("ignore")

class ParrotParaphraser:
  def __init__(self):
    self.parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")
    self.string_utility = StringUtility()

  def paraphrase(self, text):
    sentences = self.string_utility.get_sentences(text)
    paraphrases = []

    for sentence in sentences:
      generated_paraphrases = self.parrot.augment(input_phrase=sentence, max_return_phrases=10, adequacy_threshold=0.95)

      if generated_paraphrases == None:
        return "Parrot Paraphraser could not generate a phrase with enough adequacy."
      
      paraphrases.append(generated_paraphrases[0][0])

    combined_paraphrase = ". ".join(paraphrases)
    return combined_paraphrase

if __name__ == "__main__":
  text = "As Sir Henry and I sat at breakfast, the sunlight flooded in through the high mullioned windows, throwing watery patches of color from the coats of arms which covered them. The dark panelling glowed like bronze in the golden rays, and it was hard to realize that this was indeed the chamber which had struck such a gloom into our souls upon the evening before. But the evening before, Sir Henry's nerves were still handled the stimulant of suspense, and he came to breakfast, his cheeks flushed in the exhilaration of the early chase."

  parrot_paraphraser = ParrotParaphraser()
  print(parrot_paraphraser.paraphrase(text))