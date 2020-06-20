## happy path
* greet
  - utter_greet

##card generic path
* card_inquiry{"card":"card"}
    - utter_card_type
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance

##card product path
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance
    
##card generic path1
* card_inquiry{"card":"card"}
    - utter_card_type
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance

##card generic path2
* card_inquiry{"card":"card"}
    - utter_card_type
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance

##card product path1
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance

##card product path2
* card_inquiry_type{"card_type":"debit","card":"card"}
    - utter_ask_card_no
* card_information{"card_number":"id_cardnumber:123456789101112"}
    - utter_ask_cnn_no
* card_information{"cvv":"id_cvv:123"}
    - utter_ask_otp
* card_information{"otp":"id_otp:123456"}
    - action_show_account_balance