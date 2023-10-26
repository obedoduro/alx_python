import sys
def main():
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # Subtract 1 to exclude the script name

    # Print the number of argument(s)
    if num_args == 1:
        print(f"Number of argument: {num_args}")
    else:
        print(f"Number of arguments: {num_args}")

   # Print a colon or period depending on the number of arguments
    if num_args > 0:
        print(":")

   # Print the arguments and their positions
for i in range(num_args):
    print(f"{i + 1}: {sys.argv[i + 1]}")



if __name__ == "__main__":
    main()
