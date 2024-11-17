import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("auth.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

async def echo(update: Update, context):
    user_input = update.message.text
    user_id = update.message.from_user.id

    # Save data to Firestore
    db.collection("users").document(str(user_id)).set({"input": user_input})

    await update.message.reply_text(f"Saved: {user_input}")
