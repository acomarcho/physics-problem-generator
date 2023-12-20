import random
import re

# TODO: Refactor this code. This is more of a proof of concept.

problems = [
  {
    "text": "John is driving a car at the speed of {{A}} m/s. {{B}} meters in front of him, lies an obstacle. He brakes for {{C}} seconds and the car stops exactly in front of the obstacle. If the deceleration is constant, what is the car's deceleration (in m/s^2)?",
    "rules": {
      "A": {
        "min": 4,
        "max": 10
      },
      "B": {
        "min": 2,
        "max": 10,
        "mul": 100
      },
      "C": {
        "min": 2,
        "max": 10,
      }
    },
    "answer": "2*({{B}}-({{A}}*{{C}}))/({{C}}**2)",
    "explanation": """From the equation s = v*t + (1/2)*a*(t^2), plug in the values for s, v, and t and solve for a.
    a = 2*(s - v*t)/(t^2),
    a = 2*({{B}} - {{A}}*{{C}})/({{C}}^2)
    a = {{answer}} m/s^2
    """
  }
]

def generate_problem(problem):
  pattern = r"\{\{(.+?)\}\}"
  matches = re.findall(pattern, problem['text'])

  variables = {}

  for m in matches:
    rule = problem['rules'][m]

    variables[m] = random.randint(rule['min'], rule['max'])
    if 'mul' in rule:
      variables[m] *= rule['mul']

  generated_problem = replace_variables_in_string(problem['text'], variables)

  answer_to_evaluate = replace_variables_in_string(problem['answer'], variables)
  answer = eval(answer_to_evaluate)
  variables['answer'] = answer

  explanation = replace_variables_in_string(problem['explanation'], variables)

  return (generated_problem, answer, explanation)

def replace_variables_in_string(string, variables):
  def replace_variables(match):
    var = match.group(1)
    return str(variables[var])

  pattern = r"\{\{(.+?)\}\}"
  result_string = re.sub(pattern, replace_variables, string)

  return result_string

if __name__ == "__main__":
  generated_problem, answer, explanation = generate_problem(problems[0])

  print(f"Question: {generated_problem}")
  print(f"Answer: {answer}")
  print(f"Explanation: {explanation}")