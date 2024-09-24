import utils


def main():
    # Initialize the database at the start
    utils.initialize_db()

    # Capture an image from the webcam
    image = utils.capture_face()
    if image is None:
        print("Failed to capture image.")
        return

    # Get the face encoding from the captured image
    face_encoding = utils.get_face_encoding(image)
    if face_encoding is None:
        print("No face detected.")
        return

    # Retrieve payment info and username based on face encoding
    payment_info, username = utils.match_face(face_encoding)

    if payment_info:
        # Process payment if the user is found
        charge = utils.mock_process_payment(username, 420, payment_info)
        print(f"{username}! Your payment  has been processed: {charge}")
    else:
        print("No matching user found. Registration required.")

        # If no match, store new user data in the database
        current_user = input("Enter your username: ")
        payment_info = input("Enter your payment info: ")

        utils.store_face_in_db(current_user, face_encoding, payment_info)
        print("user registered and face data stored successfully.")
        charge = utils.mock_process_payment(current_user, 420, payment_info)
        print(f"{current_user}! Your payment  has been processed: {charge}")


if __name__ == '__main__':
    main()
