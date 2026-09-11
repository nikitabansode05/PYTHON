def write(filename,content):
    """Multiline Comment"""
    with open(filename,'w') as file:
        file.write(content)
    print(f"Content written to {filename}.")
    
def read(filename):
    try:
        with open(filename,'r') as file:
            content=file.read()
        print(f"Content red from {filename}:\n{content}")
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        
if __name__ == "__main__":
    filename='tfl.txt'
    content="""Welcome to Transflower !! Transflower Acceleration Program.Mentor as a service!!!"""
    write(filename,content)
    read(filename)
    