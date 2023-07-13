import pandas as pd
import matplotlib.pyplot as plt

def plot_resolved_incidents(data):
    resolved_counts = data[data['Status'] == 'Resolved']['SolvedBy'].value_counts()
    resolved_counts_top5 = resolved_counts.tail(20)
    resolved_counts_top5.plot(kind='bar')
    plt.xlabel('User')
    plt.ylabel('Number of Incidents Resolved')
    plt.title('Number of Incidents Resolved by Each User')
    plt.show()

# Read CSV file
data = pd.read_csv('Output_file_random_data_generator.csv')

# Call the function to plot the graph
plot_resolved_incidents(data)