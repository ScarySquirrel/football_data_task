import requests
import sys



URL = "https://api.football-data.org/v2/competitions/"
r = requests.get(url = URL)
data = r.json()

count = data['count']
filters  = data['filters']
competitions = data['competitions']

print("You are accessing the football competetion dataset")
val = input("Please provide which tier competition data u want to access from (1,2,3,4): ")

tier_map = {1:'TIER_ONE',2:'TIER_TWO',3:'TIER_THREE',4:'TIER_FOUR'}
tier = tier_map[int(val)]
print(f"Providing the results for tier {val} competitions")

original_stdout = sys.stdout # Save a reference to the original standard output
with open('output.csv', 'w') as f:
	sys.stdout = f
	print(f"id,Name,Area/Country,Available Seasons,Tier")
	for competition in competitions:
		if(tier == competition['plan']):
			filtered_data = f"{competition['id']},{competition['name']},{competition['area']['name']},{competition['numberOfAvailableSeasons']},{competition['plan']}"
			print(filtered_data)
	sys.stdout = original_stdout