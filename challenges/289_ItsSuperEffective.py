## https://old.reddit.com/r/dailyprogrammer/comments/5961a5/20161024_challenge_289_easy_its_super_effective/

from urllib.request import Request, urlopen
import json


# bonus 1
api_type_url = "https://pokeapi.co/api/v2/type/{type}/"

def get_damage(api_json, typ):
    extract_names = lambda x: [o["name"] for o in api_json[x]]
    if typ in extract_names("double_damage_to"):
        return 2
    elif typ in extract_names("half_damage_to"):
        return 0.5
    elif typ in extract_names("no_damage_to"):
        return 0
    else:
        return 1

def calc_damage(hit, rec):
    dam = 1
    req = Request(api_type_url.format(type=hit))
    req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0")
    res = json.loads(urlopen(req).read())["damage_relations"]
    for r in rec.split():
        dam *= get_damage(res, r)
    return f"{dam}x"

assert calc_damage("fire", "grass") == "2x"
assert calc_damage("fighting", "ice rock") == "4x"
assert calc_damage("psychic", "poison dark") == "0x"
assert calc_damage("water", "normal") == "1x"
assert calc_damage("fire", "rock") == "0.5x"
