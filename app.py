from data import foods

print("Welcome to Food Recommender System ")

# Take user input
food_type = input("Enter food type (fast food / dessert / indian / healthy): ").lower()
taste = input("Enter taste (sweet / spicy / savory / fresh): ").lower()

print("\n Finding best matches...\n")

# Recommendation logic
recommendations = []

for food in foods:
    score = 0
    
    if food["type"] == food_type:
        score += 1
        
    if food["taste"] == taste:
        score += 1
    
    if score > 0:
        recommendations.append((food["name"], score))

# Sort by best match
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
if recommendations:
    print(" Recommended for you:")
    for item in recommendations:
        print(f"- {item[0]} (match score: {item[1]})")
else:
    print(" No matching food found")