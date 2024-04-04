#
# def commands():
# 	return """Voice Command                       Action
# -------------------------------------------------------------------
# -> open <filename>                  opens file
# -> create <filename>                creates and write to a new file
# -> read <filename>                  reads out file contents
# -------------------------------------------------------------------
# -------------------------------------------------------------------"""
#
# if __name__ == "__main__":
# 	print(commands())

def main():
    # Open the file in write mode
    with open("user_input.txt", "w") as file:
        while True:
            # Take user input
            user_input = input("Enter text (press Enter on an empty line to finish): ")

            # Check if user wants to exit
            if not user_input:
                break

            # Write the input to the file
            file.write(user_input + "\n")

    print("Data saved to 'user_input.txt'.")

if __name__ == "__main__":
    main()
