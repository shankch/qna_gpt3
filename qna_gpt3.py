#This prompt creates a question + answer structure for answering questions based on existing knowledge.

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import demo_web_app
from api import GPT, Example, UIConfig


question_prefix = 'Q: '
question_suffix = "\n"
answer_prefix = "A: "
answer_suffix = "\n\n"


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100,
          input_prefix=question_prefix,
          input_suffix=question_suffix,
          output_prefix=answer_prefix,
          output_suffix=answer_suffix,
          append_output_prefix_to_query=True)

gpt.add_example(Example('Who invented three phase induction motor?',
                        'Nikola Tesla invented the three phase induction motor.'))
gpt.add_example(
    Example('Who was the chief executive officer of Tesla in 2018?', 'Elon Musk was the chief executive officer of Tesla in 2018.'))
gpt.add_example(Example(
    'Which country was he born in?', 'He was born in South Africa.'))
gpt.add_example(Example('Who was the chief executive office of Tesla before Elon Musk?',
                        'Martin Eberhard was the chief executive office of Tesla before Elon Musk'))
gpt.add_example(Example('In what year did the shares of tesla shot up by maximum pecentage?',
                        'The shares of tesla shot up by maximum pecentage in 2020.'))

# Define UI configuration
config = UIConfig(description="Question to Answer",
                  button_text="Answer",
                  placeholder="Who directed the movie 'Gladiator'?")

demo_web_app(gpt, config)
