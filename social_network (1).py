class Person: 
    ''' 
    A class representing a person in a social network. 
    Attributes: 
        name (str): The name of the person. 
        friends (list): A list of friends (Person objects). 
    Methods: 
        add_friend(friend): Adds a friend to the person's friend list. 
    ''' 
     
    def __init__(self, name): 
        self.name = name 
        self.friends = []  # List to store Person objects 

    def add_friend(self, friend): 
        """Adds a friend if not already in the friend list""" 
        if friend not in self.friends: 
            self.friends.append(friend) 

 
class SocialNetwork: 
    ''' 
    A class representing a social network. 
    Attributes: 
        people (dict): A dictionary mapping names to Person objects. 
    Methods: 
        add_person(name): Adds a new person to the network. 
        add_friendship(person1_name, person2_name): Creates a friendship between two people. 
        print_network(): Prints the names of all people and their friends. 
    ''' 

    def __init__(self): 
        self.people = {}  
     
    def add_person(self, name): 
        """Adds a new person to the network""" 
        if name not in self.people: 
            self.people[name] = Person(name) 
        else: 
            print(f"{name} already exists in the network.") 

     
    def add_friendship(self, person1_name, person2_name): 
        """Creates a friendship between two people""" 
        if person1_name not in self.people or person2_name not in self.people: 
            print(f"Friendship not created. One or both people do not exist!") 
            return 
         
        person1 = self.people[person1_name] 
        person2 = self.people[person2_name] 
         
        # Add each other as friends (bidirectional) 
        person1.add_friend(person2) 
        person2.add_friend(person1) 
     

    def print_network(self): 
        """Prints each person and their friends""" 
        for name, person in self.people.items(): 
            friend_names = [friend.name for friend in person.friends] 
            print(f"{name} is friends with: {', '.join(friend_names)}") 

# Test your code here

network = SocialNetwork() 

# Add people 
network.add_person("Alex") 
network.add_person("Jordan") 
network.add_person("Morgan") 
network.add_person("Taylor") 
network.add_person("Casey") 
network.add_person("Riley") 
 

# Add friendships 
network.add_friendship("Alex", "Jordan") 
network.add_friendship("Alex", "Morgan") 
network.add_friendship("Jordan", "Taylor") 
network.add_friendship("Morgan", "Casey") 
network.add_friendship("Taylor", "Riley") 
network.add_friendship("Casey", "Riley") 
network.add_friendship("Morgan", "Riley") 
network.add_friendship("Alex", "Taylor") 

# Test if people were added 
assert "Alex" in network.people 
assert "Jordan" in network.people 
assert "Taylor" in network.people 

# Test if friendships were created correctly 
alex = network.people["Alex"] 
jordan = network.people["Jordan"] 
morgan = network.people["Morgan"] 
taylor = network.people["Taylor"] 

assert jordan in alex.friends 
assert alex in jordan.friends 
assert morgan in alex.friends 
assert alex in morgan.friends 
assert taylor in alex.friends 
assert alex in taylor.friends 

# Test if friendship was not created for missing person 
network.add_friendship("Jordan", "Johnny")

# Check number of friends 
assert len(alex.friends) == 3  # Jordan, Morgan, Taylor 
assert len(morgan.friends) == 3  # Alex, Casey, Riley 
assert len(taylor.friends) == 3  # Jordan, Riley, Alex  

network.print_network() 
print("✅ All test cases passed!")
 

''' 
Design Memo:

A graph is the best structure for representing a social network because it models relationships that are 
bidirectional and dynamic. In this project, each person acts as a node, and each friendship acts as an 
edge connecting two nodes. Unlike lists or trees, a graph allows every person to be connected to many 
others without a clear hierarchy or order. This makes it ideal for showing how friendships work in real 
life, where relationships form in all directions. 
 
A list would not work well because it can only store elements in sequence, so it cannot represent multiple 
mutual connections. A tree structure would also fail because it requires a top-level root and one-way 
parent-child relationships, while a social network has no single "root" person. People are peers, not 
subordinates, and friendships are mutual rather than one-directional. 
 
When building and printing the network, I noticed that adding friendships was simple because each connection 
only required updating two lists. However, the trade-off is that when printing, we need to loop through 
each person and their friends, which can become slower as the network grows. Still, the adjacency list 
representation (a dictionary of people with lists of friends) is memory-efficient and easy to expand. This 
structure allows for flexible connections, making it perfect for modeling social platforms like Instagram. 
''' 