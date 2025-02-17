# using if else condition
import os
import shutil

def list_directory_content(directory): # you have to pass the directory you want to list the files of
	contents = os.listdir(directory)  # gives all the files as a list in the given  directory and storeing the list in files
	if not contents:
		print(f"Error: No Files/Folders Found In The Directory: {directory}")
	else:
		for content in contents :
			print(content)

    
def rename_file(directory, old_name, new_name):
	old_path = os.path.join(directory,old_name) # creating the entire path of the older file
	new_path = os.path.join(directory,new_name) # creating the entire path of the new file
	os.rename(old_path, new_path) # renaming the file
	
	print(f"File {old_name} Renamed To {old_name} Successfully")
	print(f"Your File Is Ready In This Location: {new_path}")


# 3
# Delete the file/folder
def delete_path(directory, name):
	path = os.path.join(directory, name)

	# check if it is file or folder
	if os.path.isfile(path):
		os.remove(path) # delete the file
		print(f"Success: File {path} Deleted Successfully!")
	
	elif os.path.isdir(path):
		shutil.rmtree(path)
		print(f"Success: Directory {path} Deleted Successfully")

	else:
		print(f"Cannot Remove '{path}': No Such File or Directory")

# Create a directory
def create_directory(directory, folder_name):
	path = os.path.join(directory, folder_name)
	
	os.makedirs(path, exist_ok=True)
	print(f"Directory: '{path}' created Successfully")


def main():
	while True:	
		print("\nFile Management System")
		print("1. List Directory Content")
		print("2. Rename File")
		print("3. Delete File/Directory")
		print("4. Create Directory")
		print("5. Exit")
        
		

		choice = input("Enter your choice: ")

		if choice == "1":
			directory = input("enter directory path: ")
			list_directory_content(directory)
		
		elif choice == "2":
			directory = input("enter directory path: ")

			print(f"Listing All The Avaible files in {directory} Directory")
			if os.path.isdir(directory): # check the directory exists or not
				files = os.listdir(directory) # listing all the contents of the directory
				for file in files:
					if os.path.isfile(os.path.join(directory, file)): # filter out the files only, not the folders
						print(file)
			
			print("Select From Above")

			old_name = input("enter old file name: ")
			new_name = input("enter new file name: ")
			rename_file(directory,old_name,new_name)
        
		elif choice == "3": 
			directory = input("enter directory path: ")
			list_directory_content(directory)
			
			print("Select from Above")

			name = input("Enter file or directory name to delete: ")
			delete_path(directory, name)

		elif choice == "4":
			directory = input("enter directory path: ")
			folder_name = input("enter new folder name: ")
			create_directory(directory, folder_name)
		
		elif choice == "5":
			print("Exiting.......")
			break
		
		else: 
			print("Select a valid option")
			
if __name__ == "__main__":
	main()
	