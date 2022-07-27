from google.colab import files

#bukhsh
#os.chdir('datasets/helpdesk/processed')

df_train_remaining_time = pd.read_csv('remaining_time_train.csv')
df_test_remaining_time = pd.read_csv('remaining_time_test.csv')

print(len(df_train_remaining_time['case_id'].unique()), 
      len(df_test_remaining_time['case_id'].unique()))

bk_train_cases = df_train_remaining_time['case_id'].unique()
bk_test_cases = df_test_remaining_time['case_id'].unique()

set(bk_test_cases).intersection(set(bk_train_cases))


#files.download('remaining_time_train.csv') 
#files.download('remaining_time_test.csv') 