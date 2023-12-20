import re

class StringUtility:
  def __init__(self):
    pass

  def get_sentences(self, paragraph):
    sentences = re.split(r'(?<!\d\.\d)(?<!\d\.)\s*(?<!\w\.\w)(?<!\w\.)\s*[.?!]\s', paragraph)

    new_sentences = []
    for sentence in sentences:
        new_sentences.append(sentence.rstrip(".") + ".")

    return new_sentences
  
if __name__ == "__main__":
   string_utility = StringUtility()

   print(string_utility.get_sentences("I am riding a car with a speed of 50.2m/s. How long will it take me to Jakarta?"))