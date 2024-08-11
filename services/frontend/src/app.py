import os
import requests

def upload_file(url, file_path, content_type="application/pdf"):
    """
    Upload a file to the given URL.

    :param url: The URL to upload the file to.
    :param file_path: The path to the file to be uploaded.
    :param content_type: The MIME type of the file being uploaded.
    """
    # Extract the filename from the file path
    filename = os.path.basename(file_path)
    
    with open(file_path, "rb") as file:
        files = {"file": (filename, file, content_type)}
        response = requests.post(url, files=files)
        
        if response.status_code == 200:
            print("File uploaded successfully.")
            print("Response:", response.json())
        else:
            print("Failed to upload file.")
            print("Status code:", response.status_code)
            print("Response:", response.json())

# Example usage
upload_file("http://127.0.0.1:8000/notes/ETHUSD", r"C:/Users/AHEBIE/Downloads/Prescription_Lunettes-26785255.pdf")
