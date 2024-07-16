import json

## Please note that these rankings have 0 grounding apart from 5 seconds of thought each.

## Finished heroes in rankings
# "ana", "ashe", "baptiste", "bastion", "brigitte", "cassidy", "d.va", "doomfist"

# List of Overwatch 2 heros
hero_data = [
    {
        "HeroName": "ana",
        "StrongAgainst": ["bastion", "ashe", "doomfist"],
        "GoodAgainst": [],
        "WeakAgainst": ["d.va"],
        "BadAgainst": []
    },
    {
        "HeroName": "ashe",
        "StrongAgainst": [],
        "GoodAgainst": ["cassidy"],
        "WeakAgainst": ["d.va"],
        "BadAgainst": ["ana", "doomfist"]
    },
    {
        "HeroName": "baptiste",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["doomfist"],
        "BadAgainst": []
    },
    {
        "HeroName": "bastion",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["d.va"],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "brigitte",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ashe", "d.va"],
        "BadAgainst": ["bastion"]
    },
    {
        "HeroName": "cassidy",
        "StrongAgainst": [],
        "GoodAgainst": ["d.va", "doomfist"],
        "WeakAgainst": ["ana", "baptiste"],
        "BadAgainst": []
    },
    {
        "HeroName": "d.va",
        "StrongAgainst": ["bastion"],
        "GoodAgainst": ["ana", "ashe"],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": []
    },
    {
        "HeroName": "doomfist",
        "StrongAgainst": [],
        "GoodAgainst": ["baptiste"],
        "WeakAgainst": ["ana", "bastion", "brigitte", "cassidy"],
        "BadAgainst": []
    },
    {
        "HeroName": "echo",
        "StrongAgainst": ["ana", "brigitte"],
        "GoodAgainst": ["d.va", "doomfist"],
        "WeakAgainst": ["bastion"],
        "BadAgainst": ["cassidy"]
    },
    {
        "HeroName": "genji",
        "StrongAgainst": ["bastion"],
        "GoodAgainst": ["baptiste"],
        "WeakAgainst": ["ashe", "doomfist"],
        "BadAgainst": ["brigitte", "cassidy", "d.va"]
    },
    {
        "HeroName": "hanzo",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["d.va"],
        "BadAgainst": []
    },
    {
        "HeroName": "illari",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion"],
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
        "GoodAgainst": ["brigitte"],
        "WeakAgainst": [],
        "BadAgainst": ["baptiste"]
    },
    {
        "HeroName": "kiriko",
        "StrongAgainst": [],
        "GoodAgainst": ["ashe", "d.va"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "lifeweaver",
        "StrongAgainst": [],
        "GoodAgainst": ["ashe", "doomfist"],
        "WeakAgainst": ["d.va"],
        "BadAgainst": []
    },
    {
        "HeroName": "lucio",
        "StrongAgainst": [],
        "GoodAgainst": ["doomfist"],
        "WeakAgainst": [],
        "BadAgainst": ["cassidy"]
    },
    {
        "HeroName": "mauga",
        "StrongAgainst": ["d.va"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana", "baptiste", "bastion"]
    },
    {
        "HeroName": "mei",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion", "d.va"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
        {
        "HeroName": "mercy",
        "StrongAgainst": ["brigitte", "doomfist"],
        "GoodAgainst": [],
        "WeakAgainst": ["baptiste", "bastion"],
        "BadAgainst": ["cassidy"]
    },
    {
        "HeroName": "moira",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": ["cassidy"],
        "BadAgainst": ["d.va"]
    },
    {
        "HeroName": "orisa",
        "StrongAgainst": [],
        "GoodAgainst": ["doomfist"],
        "WeakAgainst": ["baptiste", "bastion"],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "pharah",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": ["doomfist"],
        "WeakAgainst": ["ana", "bastion", "d.va"],
        "BadAgainst": ["ashe", "baptiste", "cassidy"]
    },
    {
        "HeroName": "ramattra",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["bastion"],
        "BadAgainst": []
    },
    {
        "HeroName": "reaper",
        "StrongAgainst": [],
        "GoodAgainst": ["brigitte", "cassidy"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "reinhardt",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": ["bastion"]
    },
    {
        "HeroName": "roadhog",
        "StrongAgainst": ["doomfist"],
        "GoodAgainst": [],
        "WeakAgainst": ["ashe", "d.va"],
        "BadAgainst": ["ana", "bastion"]
    },
    {
        "HeroName": "sigma",
        "StrongAgainst": [],
        "GoodAgainst": ["d.va", "doomfist"],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": ["bastion"]
    },
    {
        "HeroName": "sojourn",
        "StrongAgainst": [],
        "GoodAgainst": ["doomfist"],
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
        "StrongAgainst": ["ana", "ashe", "bastion", "doomfist"],
        "GoodAgainst": ["brigitte"],
        "WeakAgainst": ["cassidy"],
        "BadAgainst": []
    },
    {
        "HeroName": "symmetra",
        "StrongAgainst": ["d.va"],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": ["doomfist"],
        "BadAgainst": []
    },
    {
        "HeroName": "torbjorn",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["baptiste", "doomfist"],
        "BadAgainst": []
    },
    {
        "HeroName": "tracer",
        "StrongAgainst": ["ana", "ashe"],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": [],
        "BadAgainst": ["brigitte", "cassidy", "d.va"]
    },
    {
        "HeroName": "venture",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["brigitte", "doomfist"],
        "BadAgainst": ["cassidy"]
    },
    {
        "HeroName": "widowmaker",
        "StrongAgainst": ["bastion", "brigitte"],
        "GoodAgainst": ["ana", "cassidy"],
        "WeakAgainst": [],
        "BadAgainst": ["baptiste", "doomfist"]
    },
    {
        "HeroName": "winston",
        "StrongAgainst": [],
        "GoodAgainst": ["brigitte"],
        "WeakAgainst": ["cassidy"],
        "BadAgainst": ["bastion", "d.va", "doomfist"]
    },
    {
        "HeroName": "wrecking ball",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": ["ana", "cassidy"]
    },
    {
        "HeroName": "zarya",
        "StrongAgainst": ["ashe", "d.va"],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "zenyatta",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["doomfist"],
        "BadAgainst": ["ashe"]
    }
]

# Convert to JSON
json_data = json.dumps(hero_data, indent=4)

# Write to a file
with open('overwatch_heroes.json', 'w') as file:
    file.write(json_data)

print("jSON dataset created successfully.")