# qna_gpt3
Question answering using openAI GPT-3 model

## Background

GPT-3 ([Brown et al.](https://arxiv.org/abs/2005.14165)) is OpenAI's latest language model. It incrementally builds on model architectures designed in [previous](https://arxiv.org/abs/1706.03762) [research](https://arxiv.org/abs/1810.04805) studies, but its key advance is that it's extremely good at "few-shot" learning. There's a [lot](https://twitter.com/sharifshameem/status/1282676454690451457) [it](https://twitter.com/jsngr/status/1284511080715362304?s=20) [can](https://twitter.com/paraschopra/status/1284801028676653060?s=20) [do](https://www.gwern.net/GPT-3), but one of the biggest pain points is in "priming," or seeding, the model with some inputs such that the model can intelligently create new outputs. Many people have ideas for GPT-3 but struggle to make them work, since priming is a new paradigm of machine learning. Additionally, it takes a nontrivial amount of web development to spin up a demo to showcase a cool idea. We built this project to make our own idea generation easier to experiment with.

## Requirements

Coding-wise, you only need Python. But for the app to run, you will need:

* API key from the OpenAI API beta invite
* Python 3
* `yarn`

Instructions to install Python 3 are [here](https://realpython.com/installing-python/), and instructions to install `yarn` are [here](https://classic.yarnpkg.com/en/docs/install/#mac-stable).

## Setup

First, clone or fork this repository. Then to set up your virtual environment, do the following:

1. Create a virtual environment in the root directory: `python -m venv $ENV_NAME`
2. Activate the virtual environment: ` source $ENV_NAME/bin/activate` (for MacOS, Unix, or Linux users) or ` .\ENV_NAME\Scripts\activate` (for Windows users)
3. Install requirements: `pip install -r api/requirements.txt`
4. To add your secret key: create a file anywhere on your computer called `openai.cfg` with the contents `OPENAI_KEY=$YOUR_SECRET_KEY`, where `$YOUR_SECRET_KEY` looks something like `'sk-somerandomcharacters'` (including quotes). If you are unsure what your secret key is, navigate to the [API docs](https://beta.openai.com/developer-quickstart) and copy the token displayed next to the "secret" key type.
5. Set your environment variable to read the secret key: run `export OPENAI_CONFIG=/path/to/config/openai.cfg` (for MacOS, Unix, or Linux users) or `set OPENAI_CONFIG=/path/to/config/openai.cfg` (for Windows users)
6. Run `yarn install` in the root directory

If you are a Windows user, to run the demos, you will need to modify the following line inside `api/demo_web_app.py`:
`subprocess.Popen(["yarn", "start"])` to `subprocess.Popen(["yarn", "start"], shell=True)`

To verify that your environment is set up properly, run one of the 3 scripts in the `examples` directory:
`python examples/run_latex_app.py`

A new tab should pop up in your browser, and you should be able to interact with the UI! To stop this app, run ctrl-c or command-c in your terminal.

To create your own example, check out the ["getting started" docs](https://github.com/shreyashankar/gpt3-sandbox/blob/master/docs/getting-started.md).

## Authors

This project is built with help of the repository of shreya shankar et al. (https://github.com/shreyashankar/gpt3-sandbox)
