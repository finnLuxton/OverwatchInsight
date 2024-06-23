import json

## Finished heroes in rankings
# Ana, 

# List of Overwatch 2 heros
hero_data = [
    {
        "HeroName": "Ana",
        "StrongAgainst": ["Bastion", "Ashe"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Ashe",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Baptiste",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Bastion",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Brigitte",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Cassidy",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["Ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "D.va",
        "StrongAgainst": [],
        "GoodAgainst": ["Ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Doomfist",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["Ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "Echo",
        "StrongAgainst": ["Ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Genji",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Hanzo",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Illari",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Junker Queen",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Junkrat",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Kiriko",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Lifeweaver",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Lucio",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Mauga",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Mei",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
        {
        "HeroName": "Mercy",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Moira",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Orisa",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Pharah",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["Ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "Ramattra",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Reaper",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Reinhardt",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["Ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "Roadhog",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Sigma",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Sojourn",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Soldier: 76",
        "StrongAgainst": [],
        "GoodAgainst": ["Ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Sombra",
        "StrongAgainst": ["Ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Symmetra",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Torbjorn",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Tracer",
        "StrongAgainst": ["Ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Venture",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Widowmaker",
        "StrongAgainst": [],
        "GoodAgainst": ["Ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Winston",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "Wrecking Ball",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["Ana"]
    },
    {
        "HeroName": "Zarya",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["Ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "Zenyatta",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    }
]

# Convert to JSON
json_data = json.dumps(hero_data, indent=4)

# Write to a file
with open('overwatch_heroes.json', 'w') as file:
    file.write(json_data)

print("JSON dataset created successfully.")