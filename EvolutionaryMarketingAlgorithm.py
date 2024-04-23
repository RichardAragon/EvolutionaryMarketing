import random
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up Google Analytics API credentials
credentials = Credentials.from_authorized_user_file('path/to/credentials.json', ['https://www.googleapis.com/auth/analytics.readonly'])
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Define the ad variations and their initial performance scores
ad_variations = [
    {'id': 1, 'copy': 'Ad Copy 1', 'image': 'Image 1', 'score': 0.0},
    {'id': 2, 'copy': 'Ad Copy 2', 'image': 'Image 2', 'score': 0.0},
    {'id': 3, 'copy': 'Ad Copy 3', 'image': 'Image 3', 'score': 0.0},
    {'id': 4, 'copy': 'Ad Copy 4', 'image': 'Image 4', 'score': 0.0},
]

def get_cpa_from_analytics(variation_id):
    # Make a request to the Google Analytics API to fetch CPA data for the given variation ID
    report_request = {
        'reportRequests': [
            {
                'viewId': 'YOUR_VIEW_ID',
                'dateRanges': [{'startDate': '7daysAgo', 'endDate': 'today'}],
                'metrics': [{'expression': 'ga:costPerConversion'}],
                'dimensions': [{'name': 'ga:adContent'}],
                'dimensionFilterClauses': [
                    {
                        'filters': [
                            {
                                'dimensionName': 'ga:adContent',
                                'operator': 'EXACT',
                                'expressions': [f'Variation {variation_id}']
                            }
                        ]
                    }
                ]
            }
        ]
    }
    response = analytics.reports().batchGet(body=report_request).execute()
    rows = response['reports'][0]['data'].get('rows', [])
    if rows:
        cpa = float(rows[0]['metrics'][0]['values'][0])
    else:
        cpa = 0.0
    return cpa

def fitness(variation):
    # Calculate the fitness score based on the CPA from Google Analytics
    cpa = get_cpa_from_analytics(variation['id'])
    variation['score'] = 1 / cpa if cpa > 0 else 0.0
    return variation['score']

def selection(population):
    # Select two parent variations based on their fitness scores
    parent1 = max(random.sample(population, 2), key=fitness)
    parent2 = max(random.sample(population, 2), key=fitness)
    return parent1, parent2

def crossover(parent1, parent2):
    # Perform crossover to create a new child variation
    child = {'id': len(ad_variations) + 1}
    child['copy'] = parent1['copy'] if random.random() < 0.5 else parent2['copy']
    child['image'] = parent1['image'] if random.random() < 0.5 else parent2['image']
    return child

def mutation(variation):
    # Perform mutation on the ad copy or image with a small probability
    if random.random() < 0.1:
        variation['copy'] = 'Mutated Ad Copy'
    if random.random() < 0.1:
        variation['image'] = 'Mutated Image'
    return variation

def genetic_algorithm(population, generations):
    for _ in range(generations):
        # Select parents and create a new child variation
        parent1, parent2 = selection(population)
        child = crossover(parent1, parent2)
        child = mutation(child)
        
        # Get the CPA for the new child variation from Google Analytics
        child['score'] = fitness(child)
        
        # Replace the worst-performing variation with the new child
        population.sort(key=fitness)
        population[0] = child
    
    return population

# Run the genetic algorithm for 10 generations
optimized_variations = genetic_algorithm(ad_variations, generations=10)

# Print the optimized ad variations
for variation in optimized_variations:
    print(f"ID: {variation['id']}, Copy: {variation['copy']}, Image: {variation['image']}, Score: {variation['score']}")
