def main():
    try:
        file = open("main_program/text.txt", "r")
        lines = [line.strip() for line in file]
        print(lines)
        return True
    except:
        return Exception

main()
