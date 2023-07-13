import csv
import matplotlib.pyplot as plt

def read_csv_file(filename):
    incidents = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            incidents.append(row)
    return incidents
	
def resolve_incidents_by_category(incidents):
    resolved = {}
    for incident in incidents:
        category = incident['Category']
        if category in resolved:
            resolved[category] += 1
        else:
            resolved[category] = 1
    return resolved
	   
    
filename = 'Output_file_random_data_generator.csv'
incidents = read_csv_file(filename)
resolved_incidents = resolve_incidents_by_category(incidents)

finalDf = pd.DataFrame(columns=['category', 'resolvedInc'])

# Print the resolved incidents
for category, count in resolved_incidents.items():
    print(f"Category: {category}, Resolved Incidents: {count}")
    finalDf = finalDf.append({'category': category, 'resolvedInc':count}, ignore_index=True)
    
#print(finalDfTop10)

finalDfSrt = finalDf.sort_values(by=['resolvedInc'], ascending=False).head(5)
print(finalDfSrt)

finalDfSrtDsc = finalDf.sort_values(by=['resolvedInc'], ascending=True).head(5)
print(finalDfSrtDsc)

#finalDfTop10 =  finalDfSrt['resolvedInc'].head(10)



# Plotting the bar chart
plt.bar(finalDfSrt['category'], finalDfSrt['resolvedInc'])
plt.xlabel('Category')
plt.ylabel('Inc Count Resolved')
plt.title('Bar Chart Top 5 Category Resolved Incs')

# Display the chart
plt.show()

# Plotting the bar chart
plt.bar(finalDfSrtDsc['category'], finalDfSrtDsc['resolvedInc'])


plt.xlabel('Category')
plt.ylabel('Inc Count Resolved')
plt.title('Bar Chart Lowest 5 Category Resolved Incs')

# Display the chart
plt.show()

