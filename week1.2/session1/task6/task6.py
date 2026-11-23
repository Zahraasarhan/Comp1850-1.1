# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)

Music_Database = {"Alona": ["21", "25", "30"],
                  "John": ["1080", "1995", "Red"],
                  "Lobi": ["Ghost Jo", "No"]
}


# Pretty-print the data structure
pprint(Music_Database)
# Display details of one album recorded by a specific artist
print(Music_Database["Alona"][1])