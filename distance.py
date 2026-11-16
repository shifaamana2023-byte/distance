import sys

# Fixed distance in kilometres (example: 5 km)
distance_km = 5.0  # You can change this value as needed

# Convert to metres and miles
metres = distance_km * 1000
miles = distance_km * 0.621371

# Display results
print("Distance in metres =", metres)
print("Distance in miles =", miles)

# Exit program
sys.exit()
