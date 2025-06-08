class Component():
    """Base Component Interface which defines CalculateSize method
    """
    def CalculateSize(self):
        """CalculateSize method to be overriden by children classes
        """
        pass

class File(Component):
    """File Component Class to represent a file with a size
    """
    def __init__(self, size):
        """Initialise component with a size

        Args:
            size (float): Arbitrary size
        """
        super().__init__()  # Call parent 'Component' class __init__ to preserve parent initialisation (even though it is currently empty)
        self._size = size   # Assign size to private variable

    def CalculateSize(self):
        """Returns the size of the file

        Returns:
            float: Arbitrary size of the file defined at instantiation
        """
        return self._size       # Return private size variable

class Folder(Component):
    """Folder Component Class to represent a folder to contain other components
    """
    def __init__(self):
        """ Initialise component with empty children array
        """
        super().__init__()      # Call parent 'Component' class __init__ to preserve parent initialisation (even though it is currently empty)
        self._children = []     # Initialise empty private children array
    
    def AddChild(self, component):
        """Add component to folder

        Args:
            component (Component): Component to be added to folder
        """
        self._children.append(component)                            # Append child component to private children array
        print(f'Added {str(component)} to folder {str(self)}')      # Print feedback to console

    def RemoveChild(self, component):
        """Remove component from folder

        Args:
            component (Component): Component to be removed from folder
        """
        self._children.remove(component)                            # Remove child component from private children array
        print(f'Removed {str(component)} from folder {str(self)}')  # Print feedback to console
    
    def CalculateSize(self):
        """Calculate the size of the folder

        Returns:
            float: Calculated size based on recursive search.
        """
        size = 0                                # Set intial size to 0
        for child in self._children:            # Loop through all children
            size += child.CalculateSize()       # Calculate size of children and add to total size
        return size                             # return total calculated size

""" Client """
if __name__ == "__main__":
    """ Create Folders """
    root_folder = Folder()
    folder1 = Folder()
    folder2 = Folder()

    """ Create Files """
    root_file = File(10)
    file2 = File(20)
    file3 = File(30)
    file4 = File(40)
    file5 = File(50)

    """ Empty Nested Folders """
    root_folder.AddChild(folder1)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Adding Files to Folders """
    root_folder.AddChild(root_file)
    folder1.AddChild(file2)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Independent Folder 2 """
    folder2.AddChild(file3)
    folder2.AddChild(file4)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Incorporating Folder 2 into the tree """
    folder1.AddChild(folder2)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Adding file to root folder """
    root_folder.AddChild(file5)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Removing files from folders """
    folder2.RemoveChild(file3)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')
    """ Removing whole folders from folders """
    root_folder.RemoveChild(folder1)
    print(f'Root Folder Size: {root_folder.CalculateSize()}')
    print(f'folder1 Folder Size: {folder1.CalculateSize()}')
    print(f'folder2 Folder Size: {folder2.CalculateSize()}\n')