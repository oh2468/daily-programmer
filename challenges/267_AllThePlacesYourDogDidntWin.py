## https://old.reddit.com/r/dailyprogrammer/comments/4jom3a/20160516_challenge_267_easy_all_the_places_your/

num_map = {1: "st", 2: "nd", 3: "rd"}

def get_placements(place):
    return ", ".join([f"{i}{num_map.get(i % 10, 'th')}" for i in range(102) if i != place])

# bonus challenge 1, 2 and 3
def get_placements_b(place, num):
    get_text = lambda n: num_map.get(n % 10, 'th') if n % 100 not in [11, 12, 13] else "th"
    return ", ". join([f"{i}{get_text(i)}" for i in range(1, num + 1) if i != place])

assert get_placements(1) == "0th, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th, 10th, 11st, 12nd, 13rd, 14th, 15th, 16th, 17th, 18th, 19th, 20th, 21st, 22nd, 23rd, 24th, 25th, 26th, 27th, 28th, 29th, 30th, 31st, 32nd, 33rd, 34th, 35th, 36th, 37th, 38th, 39th, 40th, 41st, 42nd, 43rd, 44th, 45th, 46th, 47th, 48th, 49th, 50th, 51st, 52nd, 53rd, 54th, 55th, 56th, 57th, 58th, 59th, 60th, 61st, 62nd, 63rd, 64th, 65th, 66th, 67th, 68th, 69th, 70th, 71st, 72nd, 73rd, 74th, 75th, 76th, 77th, 78th, 79th, 80th, 81st, 82nd, 83rd, 84th, 85th, 86th, 87th, 88th, 89th, 90th, 91st, 92nd, 93rd, 94th, 95th, 96th, 97th, 98th, 99th, 100th, 101st"
print(get_placements_b(int(input("placement: ")), int(input("contestants: "))))
