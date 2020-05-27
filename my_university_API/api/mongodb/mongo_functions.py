from api.mongodb.db import *
from datetime import datetime

def send_message(id_conversation,
                 matricola_mittente,
                 matricola_destinatario,
                 messaggio
                ):
    try:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        db.db.message.insert_one({"id_conversation": id_conversation,
                                     "matricola_mittente": matricola_mittente,
                                     "matricola_destinatario": matricola_destinatario,
                                     "messaggio": messaggio,
                                     "data_invio": dt_string})
    except :
        print(f"Failed send message, check your connection!")
    finally:
        print("Message sendend correctly")

def create_conversation(matricola1,
                        matricola2
                        ):
    try:
        id_conversation = str(db.db.conversation.count() + 1)
        db.db.conversation.insert_one({
            "id_conversation": id_conversation,
             "matricola1": matricola1,
             "matricola2": matricola2
        })

    except :
        print(f"Failed create new conversation, check your connection!")
    finally:
        print("Conversation created correctly")
        return dict({"id_conversation": id_conversation, })

def get_all_conversations(matricola):
    conversations_list = []
    try:
        multiple_param = {"$or": [{"matricola1": matricola}, {"matricola2": matricola}]}
        conversations_list = list(db.db.conversation.find(multiple_param))

        for index, item in enumerate(conversations_list):
            conversations_list[index]["messages"] = list(db.db.message.find({"id_conversation": item["id_conversation"]}))

    except :
        print('Error reading data ')
    finally:
        print('MySQL connection is closed')
        return conversations_list