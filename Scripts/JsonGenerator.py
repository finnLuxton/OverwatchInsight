import json

## Please note that these rankings have 0 grounding apart from 5 seconds of thought each.

## Finished heroes in rankings
# "ana", "ashe", "baptiste", "bastion", "brigitte"

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
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "brigitte",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ashe"],
        "BadAgainst": ["bastion"]
    },
    {
        "HeroName": "cassidy",
        "StrongAgainst": [],
        "GoodAgainst": [],
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
        "StrongAgainst": ["baptiste"],
        "GoodAgainst": [],
        "WeakAgainst": ["ana", "bastion", "brigitte"],
        "BadAgainst": []
    },
    {
        "HeroName": "echo",
        "StrongAgainst": ["ana", "brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["bastion"],
        "BadAgainst": []
    },
    {
        "HeroName": "genji",
        "StrongAgainst": ["bastion"],
        "GoodAgainst": ["baptiste"],
        "WeakAgainst": ["ashe"],
        "BadAgainst": ["brigitte"]
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
        "GoodAgainst": ["ashe"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "lifeweaver",
        "StrongAgainst": [],
        "GoodAgainst": ["ashe"],
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
        "BadAgainst": ["ana", "baptiste", "bastion"]
    },
    {
        "HeroName": "mei",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
        {
        "HeroName": "mercy",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["baptiste", "bastion"],
        "BadAgainst": []
    },
    {
        "HeroName": "moira",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "orisa",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["baptiste", "bastion"],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "pharah",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["ana", "bastion"],
        "BadAgainst": ["ashe", "baptiste"]
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
        "GoodAgainst": ["brigitte"],
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
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["ashe"],
        "BadAgainst": ["ana", "bastion"]
    },
    {
        "HeroName": "sigma",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": ["bastion"]
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
        "StrongAgainst": ["ana", "ashe", "bastion"],
        "GoodAgainst": ["brigitte"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "symmetra",
        "StrongAgainst": [],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": [],
        "BadAgainst": []
    },
    {
        "HeroName": "torbjorn",
        "StrongAgainst": ["brigitte"],
        "GoodAgainst": [],
        "WeakAgainst": ["baptiste"],
        "BadAgainst": []
    },
    {
        "HeroName": "tracer",
        "StrongAgainst": ["ana", "ashe"],
        "GoodAgainst": ["bastion"],
        "WeakAgainst": [],
        "BadAgainst": ["brigitte"]
    },
    {
        "HeroName": "venture",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": []
    },
    {
        "HeroName": "widowmaker",
        "StrongAgainst": ["bastion", "brigitte"],
        "GoodAgainst": ["ana"],
        "WeakAgainst": [],
        "BadAgainst": ["baptiste"]
    },
    {
        "HeroName": "winston",
        "StrongAgainst": [],
        "GoodAgainst": ["brigitte"],
        "WeakAgainst": [],
        "BadAgainst": ["bastion"]
    },
    {
        "HeroName": "wrecking ball",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": ["brigitte"],
        "BadAgainst": ["ana"]
    },
    {
        "HeroName": "zarya",
        "StrongAgainst": ["ashe"],
        "GoodAgainst": [],
        "WeakAgainst": ["ana"],
        "BadAgainst": []
    },
    {
        "HeroName": "zenyatta",
        "StrongAgainst": [],
        "GoodAgainst": [],
        "WeakAgainst": [],
        "BadAgainst": ["ashe"]
    }
]

# Convert to JSON
json_data = json.dumps(hero_data, indent=4)

# Write to a file
with open('overwatch_heroes.json', 'w') as file:
    file.write(json_data)

print("jSON dataset created successfully.")