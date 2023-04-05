import os
import time #to use history tracked on a doc

#abstracting moving text
def moving(message, speed):
  for char in message:
    print(char, end='', flush = True)
    time.sleep(speed)
#create history file
def create_file():
  if not os.path.exists("bookmarks.txt"):
    with open("bookmarks.txt", "w") as f:
      f.write("")

#add bookmark function
def add_bookmark():
  while True:
    section = input("Enter a Section:")
    topic = input("Enter topic:")
    url = input("Enter Url:")
    note = input("Enter a note:")

    #append the new bookmark to the file
    with open("bookmarks.txt", "a") as f:
      f.write(f"{section}\t{topic}\t{url}\t{note}\n")

    print(f"Added {section}: {topic}")
    break

#Display bookmarks
def display_bookmarks():
  with open("bookmarks.txt", "r") as f:
    bookmarks = f.read().splitlines()
  
  #checking if it has any bookmarks
  if len(bookmarks) == 0:
    print("You dont have any stored bookmarks")
  else:
    for bookmark in bookmarks:
      section, topic, url, note = bookmark.split("\t")
      print(f"{section.capitalize()}: {topic} {url} {note}\n")

#delete all bookmarks
def clear():
  while True:
    print("Which do you want to clear:\n1. By section \n2. All")
    choice = input("Which do you want to clear:")
    
    if choice == "2":
      sure = "Are you sure? (y/n):"
      moving(sure, 0.01)
      input("")
      if sure.lower() == "y":
        with open("bookmarks.txt", "w") as f:
          f.write("")
          print("All bookmarks Cleared")
          break
      else:
        break
    else:
      print("Invalid choice, Try again")
  
def main():
  # creates file if not there
  create_file()

  while True:
    time.sleep(1)
    # Moving message
    m1 = "1. Add Bookmark\n2. Diplay Bookmarks\n3. Clear Bookmarks\n4. Display by secton\n5. Exit\n\nOption:"
    moving(m1, 0.01)

    choice = input("")

    if choice == "1":
      add_bookmark()
    if choice == "2":
      display_bookmarks()
    if choice == "3":
      clear()

    if choice == "5":
      break
  
if __name__ == "__main__":
  main()