# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json


class ActionShowAccountBalance(Action):

    def name(self) -> Text:
        return "action_show_account_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sentence_for_account = "Your card Number {card_number} has an account balance of Rs.{account_balance}"
        dispatcher.utter_message(sentence_for_account.format(card_number=tracker.slots['card_number'][0].split(":")[1],
                                                             account_balance=random.randint(10 ** 4, 10 ** 5)))
        return []
