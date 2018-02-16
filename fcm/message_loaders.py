import random

class LocalFunnyLoader:
    jokes = [
        "This is where it all begins...",
        "This commit is a lie",
        "I'll explain when you're older!",
        "Batman! (this commit has no parents)",
        "The same thing we do every night, Pinky - try to take over the world!",
        "Version control is awful",
        "Lock S-foils in attack position",
        "Commit committed",
        "Just have the project 90% done and call it \"Initial import\"",
        "Whatever.",
        "A journey of a thousand miles begins with a single step",
        "I don't believe it.",
        "Future self, please forgive me and don't hit me with the baseball bat again!",
        "just shoot me",
        "I have no idea what I'm doing here.",
        "lolwhat?",
        "that coulda been bad",
        "It works! Just ship it! :boat:"
    ]

    def get_message(self):
        return random.choice(self.jokes)


class LocalMessageLoader:
    messages = [
        "Initial commit",
        "First commit",
        "added readme",
        "1st commit",
        "first commit, added files",
        "init"
    ]

    def get_message(self):
        return random.choice(self.messages)


class LocalHackLoader:
    messages = [
        "will be eventually fixed in the future, isn't that what we all tell ourselves",
        "did it to unblock business, just like everything else",
        "will fix this.. someday",
        "adding this commit now, so that there are jobs left for people in the future",
        "the important thing is - business is unblocked",
        "message to anyone who sees this in the future: THIS IS SPARTA",
        "for the love of God and all things holy - please fix this",
        "someone - someday - will recall stories of how they fixed this hack",
        "I am going to look back at this someday and scream at the dev who wrote it only to realize it was me",
        "I like to live dangerously"
    ]

    def get_message(self):
        return random.choice(self.messages)
