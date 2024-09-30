'''
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.

Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18
'''
program:
class Team:
    def __init__(self, name, score, overs):
        self.name = name
        self.score = score
        self.overs = overs

    def display_details(self):
        print(f"Team Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Overs played: {self.overs}")

def main():
    # Details for Team 1
    team1 = Team("DAV Jawahar Vidhya Mandir", 150, 20)
    
    # Details for Team 2
    team2 = Team("Kendriya School", 110, 18)
    
    # Displaying match details
    print("Match Details:")
    print("Team 1:")
    team1.display_details()
    print("Team 2:")
    team2.display_details()

if __name__ == "__main__":
    main()
