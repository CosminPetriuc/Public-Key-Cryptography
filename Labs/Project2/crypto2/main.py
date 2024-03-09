import numpy as np

# Function to calculate the modulo inverse of a 2x2 matrix under a given modulus
def matrix_modulo_inverse(matrix, modulus):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    # Calculate the modular multiplicative inverse of the determinant
    det_inverse = pow(det, -1, modulus)
    # Create the inverse matrix using the modular inverse of the determinant
    matrix_inverse = np.array([[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]])
    matrix_inverse *= det_inverse
    matrix_inverse %= modulus
    return matrix_inverse

# Function to encrypt plaintext using the Hill cipher with a given key matrix
def hill_cipher_encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 != 0: # If the length of the plain text is odd, append 'X' to make it even
        plain_text += 'X'

    encrypted_text = ""
    for i in range(0, len(plain_text), 2):  # Process the plaintext two characters at a time
        char1 = plain_text[i]
        char2 = plain_text[i + 1]
        # Create a 2x1 vector from the character pair
        vec = np.array([[ord(char1) - ord('A')], [ord(char2) - ord('A')]])
        # Multiply the vector by the key matrix and apply modulo 26
        encrypted_vec = np.dot(key_matrix, vec) % 26
        encrypted_char1 = chr(encrypted_vec[0][0] + ord('A'))
        encrypted_char2 = chr(encrypted_vec[1][0] + ord('A'))
        encrypted_text += encrypted_char1 + encrypted_char2

    return encrypted_text

# Function to get a 2x2 key matrix from user input
def get_key_matrix():
    print("Enter the 2x2 Key Matrix (e.g., for '6 24 13 16' input '6 24' on one line and '13 16' on the next):")
    key_matrix = []
    for i in range(2):
        # Read user input, split it into integers, and remove leading/trailing spaces
        row = input().strip().split()
        if len(row) != 2:
            print("Please provide a valid 2x2 matrix.")
            return get_key_matrix()
        key_matrix.append([int(row[0]), int(row[1])])
    return np.array(key_matrix)

#Menu
def main():
    print("Hill Cipher Encryption")
    print("1. Enter your own key matrix")
    print("2. Use the default key matrix(6 24 13 16)")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        key_matrix = get_key_matrix()
    elif choice == "2":
        key_matrix = np.array([[6, 24], [13, 16]])  # Example key matrix for m = 2
    else:
        print("Invalid choice. Please choose 1 or 2.")
        return

    plain_text = input("Enter the plaintext to encrypt: ")
    encrypted_text = hill_cipher_encrypt(plain_text, key_matrix)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()