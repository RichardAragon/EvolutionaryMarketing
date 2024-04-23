import random
import openai

def generate_ad_copy(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def generate_ad_image(description, api_key):
    openai.api_key = api_key
    response = openai.Image.create(
        engine="dall-e-2",
        prompt=description,
        n=1,
        size="256x256"
    )
    return response.data[0].url  # Assuming you want the URL of the generated image

def genetic_algorithm_with_ai(population, generations, api_key):
    for _ in range(generations):
        # Selection
        parent1, parent2 = selection(population)

        # Crossover
        child = {'id': len(population) + 1}
        if random.random() < 0.5:
            child['copy'] = generate_ad_copy(parent1['copy'], api_key)
        else:
            child['copy'] = generate_ad_copy(parent2['copy'], api_key)
        
        if random.random() < 0.5:
            child['image'] = generate_ad_image(parent1['image'], api_key)
        else:
            child['image'] = generate_ad_image(parent2['image'], api_key)

        # Mutation
        if random.random() < 0.1:
            child['copy'] = generate_ad_copy("Mutated Ad Copy", api_key)
        if random.random() < 0.1:
            child['image'] = generate_ad_image("Mutated Image", api_key)

        # Fitness evaluation
        child['score'] = fitness(child)

        # Replace the worst-performing variation
        population.sort(key=lambda x: x['score'])
        population[0] = child

    return population

# Example usage:
# optimized_variations = genetic_algorithm_with_ai(ad_variations, generations=10, api_key='YOUR_OPENAI_API_KEY')
# for variation in optimized_variations:
#     print(f"ID: {variation['id']}, Copy: {variation['copy']}, Image: {variation['image']}, Score: {variation['score']}")
