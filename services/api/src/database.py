from google.cloud import firestore, storage

# Initialize Firestore
db = firestore.Client(project="halogen-segment-241921")
# trades_ref = db.collection("ETHUSD").document('2024-07-22').collection("trades").offset(0).limit(1).stream()
# trades = []
# for trade in trades_ref:
#     trade_data = trade.to_dict()
#     trade_data['document_id'] = trade.id
#     trades.append(trade_data)
# print(trades)
# Initialize Google Cloud Storage
storage_client = storage.Client(project="halogen-segment-241921")
bucket_name = "fin-histobucket"
bucket = storage_client.bucket(bucket_name)



# trades_ref = db.collection('ETHUSD').document('2024-07-22').collection("trades").stream()
# trade_ids = [trade.id for trade in trades_ref]
# print(trade_ids)


