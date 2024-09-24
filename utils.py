import face_recognition
import cv2
import sqlite3
import stripe
import json
import random


# Database initialization (if not exists)
def initialize_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                face_encoding TEXT NOT NULL,
                payment_info TEXT NOT NULL
            )
        ''')
        conn.commit()


# Capture the face from the webcam
def capture_face():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    return frame if ret else None


# Get the face encoding from the captured image
def get_face_encoding(image):
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    return face_encodings[0] if face_encodings else None


# Store face embedding in the database
def store_face_in_db(username, face_encoding, payment_info):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        # Convert face_encoding (a NumPy array) to a list, then to JSON string
        face_encoding_list = face_encoding.tolist()
        cursor.execute('INSERT INTO users (username, face_encoding, payment_info) VALUES (?, ?, ?)',
                       (username, json.dumps(face_encoding_list), payment_info))
        conn.commit()


# Match current face with stored face embeddings
def match_face(current_face_encoding):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, face_encoding, payment_info FROM users')
        users = cursor.fetchall()

        for user in users:
            stored_face_encoding = json.loads(user[1])  # Safely parse the stored face encoding
            match = face_recognition.compare_faces([stored_face_encoding], current_face_encoding)
            if match[0]:  # If there's a match
                return user[2], user[0]  # Return payment_info and username
    return None


# Process payment using Stripe
def process_payment(payment_info, amount):
    stripe.api_key = 'API_KEY'
    try:
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            source=payment_info,
            description='Payment for XYZ'
        )
        return charge
    except stripe.error.StripeError as e:
        return str(e)


# Mock process payment
def mock_process_payment(username, amount, payment_info):
    print(f"Hello {username}! Your payment of {amount} USD with payment info of {payment_info} is being processed!")

    # Simulate success or failure
    if random.choice([True, False]):
        return {
            'id': 'mock_charge_id',
            'amount': amount,
            'currency': 'usd',
            'description': 'Mock payment for XYZ',
            'status': 'succeeded'
        }
    else:
        return {
            'error': 'Payment failed due to insufficient funds or another issue.'
        }