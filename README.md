# Kahoot Bot GPT

 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a bot I created to automatically answer Kahoot questions faster than any person possibly could. It was coded in Python, and works by using [Selenium](https://www.selenium.dev/) for web automation in order to scrape the question and answer choices, and then select the correct answer. The (likely) correct answer is determined by feeding the question and answer choices into the [GPT-4 API](https://openai.com/gpt-4) which then outputs whatever it thinks is the most probable answer

## Demo:

https://www.youtube.com/watch?v=A3wYRQk4m9E

# Drawbacks:

- Sometimes GPT-4 is wrong. It isn't magic
- Questions that are specific to something that wouldn't be a part of GPT-4's traning data will most likely be answered incorrectly. 
- Currently for multiple choice questions only one option is selected
	- This is under development and will hopefully be fixed soon

This project is still heavily under development, so expect there to be updates and changes in the coming days.

If you like my work please consider donating:

<a href="https://www.buymeacoffee.com/seaborg1" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Getting Started

These are some basic instructions to help you get started.

### Disclaimer

Don't be a jerk who cheats in games where something is actually at stake. This code was made to learn about web automation, OpenAI's API, and to have fun. Using the software in casual games to earn bragging rights is one thing, but cheating isn't cool. 

By choosing to use this code, you agree to do so at your own risk. I expressly disclaim any responsibility for its use or the consequences thereof. Your use of the code signifies your understanding of this disclaimer and your agreement to these terms. Play fair, and have fun!

### Prerequisites

What you need to install:

* [OpenAI API](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBDdGt4b2tMS2VHRzU4SXhNd1lZZHJxR0xsS0F5Wk53QqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE56aWJ3cWJ1NEZLb05HSHdoMnpBZzk5SVAwcGs4b2ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) - ChatGPT API
* [Selenium](https://www.selenium.dev/) - Tool for automating web applications

You need to make an account through OpenAI, and obtain an API key in order to use the GPT models with this software; otherwise it won't work. You can follow the link above to setup an account

### Installing

A step by step series of examples that tell you how to get everything up and running

Install OpenAI API (After Obtaining an API key from the website)

```html
pip install openai
```

Install selenium

```html
pip install selenium
```

Paste your OpenAI API key in setup.py:

```python
user_key = "Paste your API Key HERE!"
```

In setup.py, you can also specify which model you'd like to use. (defaults to GPT-4)

```python
model_select = "gpt-4"
```

### Usage

To run the program simply open your Terminal and go to the directory in which the files are located.

Then run:

```html
python3 start.py
```

This starts the program using your provided configuration. 

When the program starts, you will be prompted to input the Kahoot Pin:

```
Kahoot Pin: 
```

If will say the following if the login was successful:

```
Login successful
```

You will then be prompted to input a username (If it doesn't meet the [Kahoot Guidelines](https://support.kahoot.com/hc/en-us/articles/115002201267-How-to-handle-inappropriate-nicknames), then the program may fail):

```
Username?: 
```

If everything was successful, you'll see:

```
Bot created at XXXXXXX with username: 'Username'

Waiting for next question...
```

### Answering Questions

The program works by using [Selenium](https://www.selenium.dev/) to constantly scrape the website until it sees that a question is being asked. Upon seeing that something was asked, it will print the question and answer choices to the terminal. 

Example Output:

```
Question: How long does it take for sunlight to reach the Earth?
Possible Answers: 1. 8 minutes, 2. 1 minute, 3. 36 minutes, 4. 15 seconds
```

After outputting the question and answer choices, the program will send this data to the GPT model of your choice, and wait for its response. 

After getting a response, it will click the answer that the GPT model selected, and print out the answer that was selected. 

Example Output:

```
Clicked on 1
```

## Built With

* [OpenAI API](https://auth0.openai.com/u/signup/identifier?state=hKFo2SBDdGt4b2tMS2VHRzU4SXhNd1lZZHJxR0xsS0F5Wk53QqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE56aWJ3cWJ1NEZLb05HSHdoMnpBZzk5SVAwcGs4b2ZJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q) - ChatGPT API
* [Selenium](https://www.selenium.dev/) - Tool for automating web applications
* [Python](https://www.python.org/) - Language of the gods

## Contributing

Please read [CONTRIBUTING.md](https://github.com/seaborg1/kahoot-bot-gpt/blob/main/CONTRIBUTING.md) for details on the code of conduct, and the process for submitting pull requests to us. Follow the general guidelines outlined in the link. 

## Author

**[Franco](https://franco-lopez.com/me) (Seaborg1)** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/seaborg1/kahoot-bot-gpt/blob/main/LICENSE) file for details

## Acknowledgments

- [Kahoot](https://kahoot.com/) -  Intense trivia where perceptions of intelligence are won and lost
* [OpenAI](https://openai.com/) - If you're reading this article you know what [ChatGPT](https://chat.openai.com/) is
* Shoutout to [PurpleBooth](https://gist.github.com/PurpleBooth) - for putting this README template together
