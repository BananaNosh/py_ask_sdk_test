# py_ask_sdk_test

This is a framework for testing **Alexa Skills** developed in **Python** with the [alexa-skills-kit-sdk-for-python](https://github.com/alexa/alexa-skills-kit-sdk-for-python), which is mostly a translation of taimos' [Alexa Skill Test Framework](https://github.com/taimos/ask-sdk-test) in **Typescript**, which itself is based on the [alexa-skill-test-framework](https://github.com/BrianMacIntosh/alexa-skill-test-framework) by Brian MacIntosh.

The framework uses **assert** to check the expected behaviour. So the best way to go is using it with [pytest](https://docs.pytest.org/en/latest/index.html).

The ask-sdk version it is based on is `ask-sdk-core=1.10`, `ask-sdk-runtime=1.10` and `ask-sdk-model=1.11`.

### Install:
For the moment you have to clone the project and use it as a submodule in your project.
```bash
cd path/to/your/project
git init # if your project is not a git repository so far
git submodule add git@github.com:BananaNosh/py_ask_sdk_test.git py_ask_sdk_test
```
### Example:
You can see an example for using the framework in the following and in the framework's [test-files](https://github.com/BananaNosh/py_ask_sdk_test/tree/master/tests):

```python
from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem, SkillSettings, SupportedInterfaces
from request_builders.launch_request_builder import LaunchRequestBuilder
from request_builders.intent_request_builder import IntentRequestBuilder
from pseudo_handler import handler


skill_settings = SkillSettings(app_id="<Your skill's id>",
                               user_id="<Your user id>",
                               device_id="<Your device id>",
                               locale="<The locale of your skill>",
                               interfaces=SupportedInterfaces())  # interfaces your skill supports (audio, video etc.)


def test_launch_request():
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                LaunchRequestBuilder(skill_settings).build(),
                expected_speech="Salve, gaudeo te videre!",
                expected_repromt="Vin aliquid dicere?",
                check_question=False
            ),
            TestItem(
                IntentRequestBuilder("DeiIntent", skill_settings).build(),
                expected_speech=(r"Jupiter.+", True),
                expected_repromt="",
                check_question=False
            )
        ]
    )

```

