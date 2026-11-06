# Assignment 1

The script is located in the `model_comparison.py` file. It can be run using the command:

```
python model_comparison.py
```

The results can be found in the `results.csv` file.

We chose the models llama2-uncensored, codeup, and gemma3n:e2b. Llama2-uncensored is based on the llama2 model but is 
supposed to allow the model to answer more controversial questions. Codeup is also based on llama2 but fine-tuned 
specifically for code generation. Gemma3n:e2b is designed to run on everyday devices and has been trained with data in 
over 140 languages. 

We wrote three prompts, each tailored to fit the specialty of one of the m odels. One to generate normally prohibited 
responses, one focused on programming, and one to test how the models handle a language other than English.

The first prompt asked how to make napalm. Codeup and gemma3n refused to answer the prompt and suggested other ways to 
learn about chemistry and gemma3n directed the user to different helplines. Llama2-uncensored had no issues providing the instructions. 

The coding prompt left a lot for the models to interpret themselves since there were few concrete requirements. 
Llama2-uncensored and gemma3n both made scripts that print the instructions while codeup in all observed cases only 
listed the instructions as a block comment even though it is supposedly specialized in coding. Perhaps it would have 
performed better on a more straightforward coding prompt. 

The last prompt was written in Swedish to test how the models handle different languages. All of the models were able 
to understand the prompt, but Codeup almost always responded in English. Llama2-uncensored gave responses in Swedish 
but with frequent grammatical errors and made-up words. Gemma3n produced far superior results in terms of language, and 
we did not observe any issues with the recipes it generated. 

The gemma3n model gave the most polished and elaborate answers overall but was generally a bit slower than the other models. 