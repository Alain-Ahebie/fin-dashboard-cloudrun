from google.cloud import firestore, storage

# Initialize Firestore
db = firestore.Client(project="halogen-segment-241921")

# Initialize Google Cloud Storage
storage_client = storage.Client(project="halogen-segment-241921")
bucket_name = "fin-histobucket"
bucket = storage_client.bucket(bucket_name)




# from google.cloud import firestore, storage

# # Initialize Firestore
# db = firestore.Client(project="halogen-segment-241921")

# # Example function to read trades
# def read_trades():
#     doc_ref = db.collection("BTCUSD").document("2024-07-11").collection("trades").document("trade1")
#     doc = doc_ref.get()
#     if doc.exists:
#         print("Trade details:", doc.to_dict())
#     else:
#         print("No trade found")

# read_trades()