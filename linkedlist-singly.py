class Node:
    def __init__(self, data):
        self.data = data  # Store the song data
        self.next = None  # Initialize the next pointer to None

class Playlist:
    def __init__(self):
        self.head = None  # Initialize the head of the playlist to None

    def add_song(self, song):
        new_node = Node(song)  # Create a new node with the song data
        if not self.head:  # If the playlist is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head  # Start from the head
        while last.next:  # Traverse to the end of the playlist
            last = last.next
        last.next = new_node  # Set the next pointer of the last node to the new node

    def add_song_to_start(self, song):
        new_node = Node(song)  # Create a new node with the song data
        new_node.next = self.head  # Set the next pointer of the new node to the current head
        self.head = new_node  # Set the new node as the head

    def remove_song(self, song):
        if not self.head:  # If the playlist is empty
            print("Playlist is empty.")
            return
        if self.head.data == song:  # If the head node contains the song to be removed
            self.head = self.head.next  # Set the head to the next node
            return
        current = self.head  # Start from the head
        while current.next and current.next.data != song:  # Traverse the playlist to find the song to be removed
            current = current.next
        if current.next:  # If the song to be removed is found
            current.next = current.next.next  # Set the next pointer of the previous node to skip the node to be removed
        else:
            print("Song not found in the playlist.")

    def display_playlist(self):
        current = self.head  # Start from the head
        if not current:
            print("Playlist is empty.")
            return
        while current:  # Traverse the playlist
            print(current.data)  # Print the song data of each node
            current = current.next  # Move to the next node

    def play_next_song(self):
        if not self.head:  # If the playlist is empty
            print("Playlist is empty.")
            return
        print(f"Playing: {self.head.data}")  # Print the song data of the head node
        self.head = self.head.next  # Move the head to the next node

# Example usage
playlist = Playlist()

# Add songs to the playlist
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

# Display the playlist
print("Playlist:")
playlist.display_playlist()

# Play the next song
print("\nPlaying next song:")
playlist.play_next_song()

# Display the playlist after playing a song
print("\nPlaylist after playing a song:")
playlist.display_playlist()

# Add a song to the start of the playlist
playlist.add_song_to_start("Song 0")

# Display the playlist after adding a song to the start
print("\nPlaylist after adding a song to the start:")
playlist.display_playlist()

# Remove a song from the playlist
playlist.remove_song("Song 2")

# Display the playlist after removing a song
print("\nPlaylist after removing a song:")
playlist.display_playlist()