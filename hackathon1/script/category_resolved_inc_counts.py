import csv

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

# Print the resolved incidents
for category, count in resolved_incidents.items():
    print(f"Category: {category}, Resolved Incidents: {count}")
    
    
'''
Category: Configuration, Resolved Incidents: 13490
Category: Data Related, Resolved Incidents: 257
Category: Account Administration, Resolved Incidents: 1265
Category: User Access, Resolved Incidents: 4714
Category: Capacity, Resolved Incidents: 7660
Category: Miscategorised, Resolved Incidents: 3116
Category: Known Error, Resolved Incidents: 509
Category: Access, Resolved Incidents: 544
Category: Hardware, Resolved Incidents: 270
Category: Data, Resolved Incidents: 796
Category: Transaction Data, Resolved Incidents: 261
Category: Security, Resolved Incidents: 532
Category: Troubleshooting Fix, Resolved Incidents: 273
Category: No Fault Found, Resolved Incidents: 2586
Category: Technical Failure, Resolved Incidents: 250
Category: User Error, Resolved Incidents: 267
Category: Dependent System, Resolved Incidents: 1355
Category: Troubleshooting, Resolved Incidents: 250
'''