import random
import string
import subprocess

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Error: No character types selected!")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(text):
    """Copy text to clipboard using Windows PowerShell"""
    try:
        subprocess.run(["powershell", "-command", f"Set-Clipboard -Value '{text}'"], check=True)
        return True
    except:
        return False

def main():
    print("=== Password Generator v2 ===")
    
    length = int(input("Enter password length: "))
    
    print("\nChoose character types:")
    print("1. Letters only")
    print("2. Numbers only")
    print("3. Letters + Numbers")
    print("4. Letters + Numbers + Symbols (default)")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        password = generate_password(length, use_letters=True, use_numbers=False, use_symbols=False)
    elif choice == "2":
        password = generate_password(length, use_letters=False, use_numbers=True, use_symbols=False)
    elif choice == "3":
        password = generate_password(length, use_letters=True, use_numbers=True, use_symbols=False)
    else:
        password = generate_password(length, use_letters=True, use_numbers=True, use_symbols=True)
    
    if password:
        print(f"\nGenerated Password: {password}")
        
        # Copy to clipboard
        if copy_to_clipboard(password):
            print("✅ Password copied to clipboard!")
        else:
            print("⚠️  Could not copy to clipboard.")

if __name__ == "__main__":
    main()