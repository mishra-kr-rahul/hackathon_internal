import pandas as pd

def search_and_keep_words(csv_file, word_list):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Create a new column to store the matching words
    df['matching_words'] = ''

    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        description = row['Description'].lower()
        matching_words = [word for word in word_list if word in description]
        df.at[index, 'matching_labels'] = ','.join(matching_words)
    print(df)
    # Save the updated DataFrame back to the CSV file
    df.to_csv('output.csv', index=False)
    

# Example usage:
csv_file = 'Output_file_random_data_generator.csv'
word_list = ['hive', 'impala', 'hadoop', 'resource','yarn','oozie','server','cm','hdfs','spark','webhdfs','queue','ranger','encryption','cdp','java','outofmemory','dr','uat','prod','dev','memory','unix','hms','hs2','tez','control-m','abort','connect','tableau','killed','ldap','cdh','down','service','pyspark','packages','execution','unbound','grant','authentication','scheduler','block','terminal','memory','hue','corruption','gateway','installation','operation','publisher','python','abruptly','network','admin']


search_and_keep_words(csv_file, word_list)