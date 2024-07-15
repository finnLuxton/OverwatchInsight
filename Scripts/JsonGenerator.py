import json

## Finished heroes in rankings
# Ana, 

# List of Overwatch 2 heros
hero_data = [
    {
        "HeroName": "ana",
        "StrongAgainst": ["bastion", "ashe"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "ashe",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "baptiste",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "bastion",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "brigitte",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "cassidy",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "d.va",
        "StrongAgainst": [],
        "GoodAgainst": ["ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "doomfist",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "echo",
        "StrongAgainst": ["ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "genji",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "hanzo",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "illari",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "junker queen",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "junkrat",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "kiriko",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "lifeweaver",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "lucio",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "mauga",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "mei",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
        {
        "HeroName": "mercy",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "moira",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "orisa",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "pharah",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "ramattra",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "reaper",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "reinhardt",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "roadhog",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "sigma",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "sojourn",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "soldier: 76",
        "StrongAgainst": [],
        "GoodAgainst": ["ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "sombra",
        "StrongAgainst": ["ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "symmetra",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "torbjorn",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "tracer",
        "StrongAgainst": ["ana"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "venture",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "widowmaker",
        "StrongAgainst": [],
        "GoodAgainst": ["ana"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "winston",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "wrecking ball",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "zarya",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "zenyatta",
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

print("jSON dataset created successfully.")