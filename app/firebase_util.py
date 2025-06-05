import firebase_admin
from firebase_admin import credentials, firestore
import os

cred_path = os.path.join(os.path.dirname(__file__), '../app-hospede-firebase-adminsdk-fbsvc-60dd1f5f36.json')
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
db = firestore.client()

def atualizar_link_hospede(document_id, link):
    try:
        doc_ref = db.collection("hospedes").document(document_id)
        doc_ref.update({"link": link})
        return True
    except Exception as e:
        print("Erro ao atualizar Firebase:", e)
        return False
