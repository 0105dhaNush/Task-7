def read_text_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", e)