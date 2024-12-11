import pyfiglet
print("""                    ____            __   __________ __ __
  _________  ____  / / /____  _____/ /_ |__  /__  // // /
 / ___/ __ \/ __ \/ / __/ _ \/ ___/ __ \ /_ < /_ </ // /_
/ /__/ /_/ / /_/ / / /_/  __/ /__/ / / /__/ /__/ /__  __/
\___/\____/\____/_/\__/\___/\___/_/ /_/____/____/  /_/   
                                                         """)

def text_to_ascii():
    print("Welcome to ezart!")
    print("We are not responsible for any \noffensive language created here.")
    print("If you are going to expand on this, please give me credit. -cooltech334")
    text = input("Enter the text you want to convert to ASCII art: ")
    
    # Choose an ASCII font style
    print("\nAvailable fonts:")
    print("1. Standard\n2. Slant\n3. Bubble\n4. Digital")
    font_choice = input("Choose a font (1-4): ")

    # Map font choices to pyfiglet fonts
    font_map = {
        "1": "standard",
        "2": "slant",
        "3": "bubble",
        "4": "digital"
    }
    font = font_map.get(font_choice, "standard")  # Default to "standard"

    # Generate ASCII art
    ascii_art = pyfiglet.figlet_format(text, font=font)
    print("\nHere is your ASCII art:\n")
    print(ascii_art)

if __name__ == "__main__":
    text_to_ascii()
