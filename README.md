# Face Recognition Payment System

## Overview

This project is a face recognition-based payment system that allows users to make payments using facial recognition. It leverages OpenCV and the `face_recognition` library for face detection and Stripe/PayPal for payment processing. The system matches a captured face to a stored face encoding and processes the corresponding payment information.

## Features

- **Face Recognition**: Capture and encode faces using a webcam.
- **Face Matching**: Matches the captured face with existing entries in the database.
- **Payment Processing**: Integrates with Stripe and PayPal for payment processing.
- **Database Storage**: Stores user face encodings and payment details in a local SQLite database.

## Requirements

To install the necessary dependencies, run:

bash
```pip install -r requirements.txt```

- opencv-python~=4.10.0.84: For capturing and processing webcam images.
- face_recognition: For face detection and encoding.
- Flask: For web integration (future updates).
- paypalrestsdk: PayPal SDK for payment processing (optional).
- stripe~=10.12.0: Stripe SDK for payment processing.

### How It Works
- Capture Face: The system captures an image from the user's webcam.
- Face Encoding: The captured image is analyzed and encoded into a unique numerical representation.
- Face Matching: The encoded face is compared to stored face encodings in a local SQLite database.
- Payment Processing:
- If a matching face is found, the user's payment information is retrieved and processed.
- If no match is found, the user is prompted to register their face and payment info.
- Mock Payment Option: A mock payment function is included for demonstration purposes.

### Code Walkthrough
## utils.py
Contains the core logic of the application:

- Database Initialization: initialize_db() sets up a local SQLite database if it does not exist.
- Face Capture: capture_face() captures an image from the webcam.
- Face Encoding: get_face_encoding(image) returns a unique encoding for the detected face.
- Face Matching: match_face(current_face_encoding) checks if the current face encoding matches any existing entries in the database.
- Payment Processing:
- process_payment(payment_info, amount): Processes a payment using the Stripe API.
- mock_process_payment(username, amount, payment_info): A mock function simulating the payment process.

## main.py
Contains the main entry point of the application:

- Initialize the Database: Calls utils.initialize_db() to ensure the database is ready.
- Face Capture and Matching: Captures an image, retrieves the face encoding, and attempts to match it with the stored data.
- Payment Processing: If a match is found, it processes the payment; otherwise, it registers the user and stores their face encoding and payment information.
- Stripe Integration
- To use Stripe for actual payments, replace API_KEY in utils.process_payment with your Stripe secret key. You can set up a test Stripe account at stripe.com.

### Running the Application
Clone the repository and navigate to the project directory:

bash
Copy code
```git clone https://github.com/yourusername/face-recognition-payment.git```
```cd face-recognition-payment```

## Install the required dependencies:

bash
Copy code
```pip install -r requirements.txt```

## Run the application:

bash
Copy code
```python main.py```

## Follow the on-screen prompts to register new users or make a payment.

## Future Enhancements
Web Integration: Adding a Flask web interface to handle registration, payments, and face recognition directly through the browser.
PayPal Integration: Enable payments using PayPal through paypalrestsdk.
Improved Security: Encrypt sensitive payment information before storing it in the database.
Limitations
The current version does not have encryption for sensitive user data such as payment information.
The system is designed for single-face recognition per image.
Mock payment processing is used for demonstration purposes, so ensure to replace it with actual Stripe or PayPal payment logic for production use.
Contributing
If you wish to contribute to this project, feel free to submit a pull request or file an issue.
