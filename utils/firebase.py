import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import logging

logger = logging.getLogger(__file__)

cred = credentials.Certificate(os.environ['FIREBASE_CREDENTIALS'])

firebase_admin.initialize_app(cred)
db = firestore.client()


def create_doc(collection_name, doc_name, data):
    doc_ref = db.collection(collection_name).document(doc_name)
    doc_ref.set(data)
    logger.debug(f"{data} created successfully")


def read_doc(collection_name, doc_name):
    doc_ref = db.collection(collection_name).document(doc_name)
    doc = doc_ref.get()
    if doc.exists:
        logger.debug(f"Document data: {doc.to_dict()}")
        return doc
    else:
        logger.info("No such document!")
        return None


def update_doc(collection_name, doc_name, data):
    doc_ref = db.collection(collection_name).document(doc_name)
    doc_ref.update(data)
    logger.debug(f"{collection_name}'s {doc_name} deleted successfully")


def delete_doc(collection_name, doc_name):
    doc_ref = db.collection(collection_name).document(doc_name)
    doc_ref.delete()
    logger.debug(f"{collection_name}'s {doc_name} deleted successfully")
