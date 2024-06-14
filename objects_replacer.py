from pathlib import Path

CWD: Path = Path(__file__).parent
OUTPUT: Path = CWD / "output"
EXTENSION: str = ".json"

OBJECTS: set[str] = {
    ...
}


def main() -> None:
    # Checks for any compatible file
    for file in CWD.glob(f'*{EXTENSION}'):
        file_full_name: str = file.name
        file_name: str = file.stem
        
        # Checks if file_name has a object_name in it
        for this_object in OBJECTS:
            if this_object in file_name:
                break
        else:
            continue
        
        # Asks user if file is correct
        if input(f"{file_full_name} was found. Do you want to use it? [Y/n]: ").casefold() != 'y':
            continue
                    
        break
    else:
        input("No compatible file(s) were found.")
        return
    
    # Makes output directory if absent
    if not Path.is_dir(OUTPUT):
        Path.mkdir(OUTPUT)
    
    # Read the content of the file
    with open(CWD / file_full_name, "r") as init_file:
        init_content: str = init_file.read()
        
        # Makes all the necessary copies
        for object in OBJECTS:
            if object == this_object:
                continue
            
            # This could have been a lambda, but eh.
            def replace(string: str) -> str:
                return string.replace(this_object, object)

            with open(OUTPUT / replace(file_full_name), 'wt') as file:
                content: str = replace(init_content)
                
                file.write(content)
                
    input("Everything should be done, for now. See ya!~")


if __name__ == '__main__': 
    main()
