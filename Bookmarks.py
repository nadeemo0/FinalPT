import os #to use history tracked on a doc

#create history file
def create_file():
  if not os.path.exists("bookmarks.txt"):
    with open("bookmarks.txt", "w") as f:
      f.write("")

#add bookmark function
def add_bookmark():
  while True:
    topic = input("Enter topic:")
    url = input("Enter Url:")
    note = input("Enter a note:")

    #append the new bookmark to the file
    with open("bookmarks.txt", "a") as f:
      f.write(f"{topic}\t{url}\t{note}")

    print(f"Added {topic}")

#Display bookmarks
def display_bookmarks():
  with open("bookmarks.txt", "r") as f:
    bookmarks = f.read().splitlines()
  
  #checking if it has any bookmarks
  if len(bookmarks) == 0:
    print("You dont have any stored bookmarks")
  else:
    for bookmark in bookmarks:
      topic, url, note = bookmarks.split("\t")
      print(f"{topic.capitalize()}: {url} - {note}\n")

#delete bookmarks
def clear():


def main():
  # creates file if not there
  create_file()

  while True:
    print("1. Add Bookmark")
    print("2. Display Bookmarks")
    print("3. Clear Bookmarks")
    print("4. Exit")
    choice = input("Option:")

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