def caesar_cipher_file(input_file_path, output_file_path, shift, direction='right'):
    """
    Encrypts or decrypts the content of a file using Caesar Cipher and outputs to another file.
    
    :param input_file_path: The path to the input file.
    :param output_file_path: The path to the output file.
    :param shift: The number of positions to shift the alphabet.
    :param direction: The direction to shift ('right' for encryption, 'left' for decryption).
    """
    def shift_byte(byte):
        return (byte + shift) % 256

    if direction == 'left':
        shift = -shift

    with open(input_file_path, 'rb') as file:
        file_data = file.read()

    processed_data = bytearray(shift_byte(byte) for byte in file_data)

    with open(output_file_path, 'wb') as file:
        file.write(processed_data)

# Example usage:
input_file = input("Enter the input file: ")
output_file = input("Enter the output file: ")
shift_value = int(input("Enter the shift value: "))
direction = input("Enter the direction ('right' for encryption, 'left' for decryption): ")

# Encrypting or decrypting the content of the input file
caesar_cipher_file(input_file, output_file, shift_value, direction)
print(f"Processed data written to {output_file}")
