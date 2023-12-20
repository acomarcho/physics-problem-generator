from parrot import Parrot

import warnings
warnings.filterwarnings("ignore")

class ParrotParaphraser:
  def __init__(self):
    self.parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

  def paraphrase(self, phrase):
    paraphrases = self.parrot.augment(input_phrase=phrase, max_return_phrases=10, adequacy_threshold=0.95)

    if paraphrases == None:
      return "Parrot Paraphraser could not generate a phrase with enough adequacy."
    
    return paraphrases[0][0]

if __name__ == "__main__":
  parrot_paraphraser = ParrotParaphraser()
  print(parrot_paraphraser.paraphrase('Can you recommend some upscale restaurants in Newyork?'))