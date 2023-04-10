import os
import time

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
    m4 = "Which do you want to clear:\n1. By section \n2. All"
    moving(m4, 0.1)
    choice = input("Which do you want to clear:")
    
    if choice == "1":

    if choice == "2":
      sure = "Are you sure? (y/n):"
      moving(sure, 0.01)
      input("")
      if sure.lower() == "y":
        with open("bookmarks.txt", "w") as f:
          f.write("")
          m5 = "All bookmarks Cleared"
          moving(m, 0.1)
          break
      else:
        break
    else:
      print("Invalid choice, Try again")

def by_sec():
  with open("bookmarks.txt","r") as f:
    bookmarks = f.read().splitlines()

  if len(bookmarks) == 0:
    m2 = "Sorry no bookmarks stored."
    moving(m2, 0.1)
  else:
    sections = ["Health", "Arabic", "History", "Math", "Bio", "English", "CSP", "ST"]
    for i, section in enumerate(sections):
      print(f"{i+1}. {section.capitalize()}")
      m3 = "Enter section number:"
      moving(m3, 0.2)
      choice = input("")
      sec_bkmrk = [bookmark for bookmark in bookmarks if bookmark.startswith(f"{sections[int(choice)-1]}\t")]
      if len(sec_bkmrk) > 0:
        print(f"\n{sections[int(choice)-1].capitalize()} bookmarks:")
            for bookmark in sec_bkmrk:
                _, topic, url, note = bookmark.split("\t")
                print(f"{topic} - {url}")
                if note:
                    print(f"  Note: {note}\n\n")
                else:
                    print("\n\n")
        else:
            print("No bookmarks found for the selected section.")
  
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
    if choice --"4":
      by_sec()
    if choice == "5":
      break
  
if __name__ == "__main__":
  main()