import os #to use history tracked on a doc

#create history file
def create_file():
  if not os.path.exists("Bookmarks.txt")

#add bookmark function
def add_bookmark():


#Display bookmarks
def display_bookmarks():

#delete bookmarks
def clear():

#main function
def main():
  create_file()

  while True:
    print("1. Add Bookmark")
    print("2. Display Bookmarks")
    print("3. Clear Bookmarks")
    print("4. Exit")
    choice = input("option:")

    if choice == "1":
      add_bookmark()
    if choice == "2":
      display_bookmarks()
    if choice == "3":
      clear()
    if choice == "4":
      break
  
if __name__ == "__main__":
  main()