# Assignment 2

We used `7_llm_as_judge.py` from tutorialLLM to test LLMs using the `ask_capital`
function We added a consistency test for Australia with the expected answer
Canberra using simple string matching.

- Tested model (`ask_capital`): **llama2-uncensored**
- Judge model (`llm_as_a_judge_agrees`): **gemma4**

## How to run

```bash
for i in 1 2 3 4 5; do .venv/bin/python 7_llm_as_judge.py; done
```

## Results

We ran all 6 tests 5 times, every test passed in every run. However looking
at the answers llama2-uncensored answered "Sydney" 4 times in total out of
the 30 answers about Australia.The judge which used gemma4 gave the correct
verdict on all the answers it gave YES for every Canberra and NO for the
"Sydney" ones.

Example from our run;

```text
answer Sydney is the capital of Australia. | verdict NO
answer The capital of Australia is Canberra. | verdict YES
answer The capital of Australia is Canberra. | verdict YES
answer The capital of Bealandia is Bea City. | verdict NO
answer Sydney is the capital city of Australia.
answer The capital of Australia is Canberra.
answer The capital of Australia is Canberra.
```

## Reflection

All tests were green but the model still hallucinated, this was caused by
our consistency tests only required 2 correct answers out of the 3 in a run.
The threshold makes the test tolerant of the models "non-determinism" but that
also hides the real errors. Looking at the printed answers was necessary to
notice the errors.

Since we print both the answer and the verdict we could trace every mistake
made by both tested model and the judge. All 4 wrong answers came from the
tested model (llama2-uncensored) and the judge caught the once it judged.
We used a different model as judge that the teste model which reduces the
risk of using the same model with the same "blind" spots. A model that answers
that the capital of Australia is Sydney will also judge that it is right.

Checking for "Canberra" in the answer is a cheap and deterministic approach
but it has its downsides. Say the LLM answered "It's Canberra, not Sydney" it
would pass, while if answers were phrased differently but still correct could
fail when a LLM tries to figure out what its saying.

Capital cities are well known facts with one clear answer, and llama2-uncensored
still got Australia wrong 4 out of 30 times. Harder questions would probably generate
even more mistakes which makes it even more important to run tests
multiple times and confirm actual answers rather than just the tests passing.
