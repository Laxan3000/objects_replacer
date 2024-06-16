# Objects Replacer
Tool for duplicating an existing file multiple times when only changing a single name between the many is needed.
Python 3.10+ is needed.

**Use case**:
If you have a JSON file (e.g. 'berry.json') and inside of it you have all the information about that object (like size or taste), but then want to replicate that file for different objects (like 'strawberry.json', 'blueberry.json', ...) changing only the name of the file and all the instances of that file name (in this case, 'berry' would be all over 'berry.txt', but you want to have a 'strawberry.json' with all the 'berry' repaced to 'strawberry'), all you would need is to execute this script once.

**How to use:**
This program requires knowledge of how to use strings and lists in Python; You can edit each constant variable at will.
1. Edit the constant variable 'OBJECTS' to include all the names you need, including the one you have at the moment. From the example above:
```python
OBJECTS: set[str] = {
    "berry",
    "strawberry",
    "blueberry"
    # You can add many more, just remember the comma after each element.
}
```
2. Once done, locate the script at the same location your file to duplicate is located;
3. Run the script by double clicking. The first step taken by the script will be to locate the main file (in that example, 'berry.json').
This means you could use the script with any of those files instead of just one. Isn't it comfy?
4. Once the main file is located, type 'y' and press enter to start generating the duplicates;
5. Once each duplicate is done, it will be saved in a new folder named 'output' inside the work directory.
