import obaid
import os
if __name__ == "__main__":
    obaid.welcome()

def main():
    print("This is the main function of the program.")
    print("You can add more code here to perform various tasks.")
main()

# File writing and reading operations
with open("file1.txt", "w") as file:
    file.write("This is elon musk\n")
    file.write("You and I\n")

with open("file1.txt", "r") as file:
    code = file.read()
    print(code)

# Create directory safely
if not os.path.exists("folder"):
    os.mkdir("folder")

if os.path.exists("folder"):
    for i in range(5):
        file_name = f"file_{i}.txt"
        file_path = os.path.join("folder", file_name)
        with open(file_path, "w") as file:
            file.write(f"This is {file_name}\n")