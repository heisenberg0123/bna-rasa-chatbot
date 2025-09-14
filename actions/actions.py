from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from datetime import datetime

class ActionCountEntities(Action):
    def name(self):
        return "action_count_entities"

    def run(self, dispatcher, tracker, domain):
        entity_type = tracker.get_slot("entity_type")
        try:
            if entity_type == "employees":
                count = requests.get("http://localhost:8091/api/count/employees").json()["count"]
            elif entity_type == "materials":
                count = requests.get("http://localhost:8091/api/count/materials").json()["count"]
            elif entity_type == "transactions":
                count = requests.get("http://localhost:8091/api/count/transactions").json()["count"]
            else:
                count = 0
            dispatcher.utter_message(text=f"Let me check... {count} {entity_type} found.")
        except Exception as e:
            dispatcher.utter_message(text=f"Sorry, I couldn't fetch the {entity_type} count. Please try again.")
        return []

class ActionExplainType(Action):
    def name(self):
        return "action_explain_type"

    def run(self, dispatcher, tracker, domain):
        type_value = tracker.get_slot("type")
        explanations = {
            "urgent": "a transaction needing immediate attention, often due to high priority.",
            "standard": "a typical transaction with no special urgency.",
            "high_value": "a transaction with significant financial importance."
        }
        explanation = explanations.get(type_value, "I don’t know that type yet.")
        dispatcher.utter_message(text=f"The '{type_value}' type means {explanation}.")
        return []

class ActionGetDate(Action):
    def name(self):
        return "action_get_date"

    def run(self, dispatcher, tracker, domain):
        try:
            response = requests.get("http://worldtimeapi.org/api/timezone/Europe/Paris", timeout=5)
            response.raise_for_status()
            date = response.json()["datetime"].split("T")[0]
            dispatcher.utter_message(text=f"Today is {date}.")
        except Exception as e:
            # Fallback to local system date
            date = datetime.now().strftime("%Y-%m-%d")
            dispatcher.utter_message(text=f"Today is {date} (using local system date).")
        return []
