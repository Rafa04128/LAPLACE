import random
import string

def generate_password(length):
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

def main():
    sample_password = input("Enter a sample password (optional): ")
    if sample_password:
        length = int(input("Enter the desired length of the password: "))
    else:
        length = len(sample_password)
        print("Sample password length:", length)
        print("Sample password:", sample_password)

    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
