
import pandas as pd
import sys
import os
import glob

input_file = pd.read_csv(sys.argv[1])


clean_input_file = input_file[['First Name', 'Last Name', 'CKI District',
 'What CKI Position Do You Have?', 'Email Address','Phone Number', 
 'Year in School', 'Favorite Means of Communication', 
 'What are some of your hobbies?',
 'What music genres do you listen to? Any specific artists?',
 'What are your favorite movies and/or TV shows?',
 'What is your favorite service project?',
 'Any ideas on how to stay active in CKI during the COVID-19 pandemic? ',
 'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)',
 'Is a hot dog a sandwich?',
 'How often would you like to communicate with your buddy? ']]
dif = clean_input_file.groupby('What CKI Position Do You Have?')

#'First Name_2', 'Last Name_2', 'CKI District_1','What CKI Position Do You Have?_1', 'Email Address_1','Phone Number_1', 'Year in School_1', 'Favorite Means of Communication_1', 'What are some of your hobbies?_1','What types of music genre do you listen to? Any specific artists?_1','What are your favorite movies and/or TV shows?_1', 'Which are better: pancakes or waffles?_1', 'Any ideas on how to stay active in CKI over this social distancing time?_1', 'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)_1', 'Is a hot dog a sandwich?_1','How often would you like to communicate with your buddy? _1'})

Position_options = ('Lieutenant Governor', 'Club President', 'Club Vice President', 'Club Treasurer', 'Club Bulletin Editor', 'Club Recruitment and Retention Officer','Club Secretary', 'Club Committee Chair', 'District Chair', 'District Executive Officer', 'Member', 'Other')
for x in Position_options:
    hello = dif.get_group( x )
    hello = hello.sample(frac=1).reset_index(drop=True)
    hello.to_csv(x+"_pairing.csv")


all_files = glob.glob( "./*_pairing.csv")


empty = []
empty_2 = []
for x in all_files:
    df = pd.read_csv(x, index_col=None, header=0)
    print(df)
    df = df.rename(columns={'Unnamed: 0':'Partner Number'})
    for x,y in df.iterrows():
        if x == 0:
            df.set_value(x, 'Partner Number', 1)
            continue
        elif x % 2 == 0:
            y = x+1
            df.set_value(x, 'Partner Number', y)
            continue
        elif x % 2 != 0:
            df.set_value(x, 'Partner Number', x)
            continue
    df_2=df.copy()
    df = df.drop_duplicates(subset='Partner Number', keep="first")
    df_2 = df_2.drop_duplicates(subset='Partner Number', keep="last")
    empty.append(df)
    empty_2.append(df_2)


for x in Position_options:
    os.remove(x+"_pairing.csv")

final_2 = pd.concat(empty_2, axis=0, ignore_index=False, sort=False)

final = pd.concat(empty, axis=0, ignore_index=False, sort=False)

final = final.rename(columns={'First Name':'First Name_1', 'Last Name':'Last Name_1', 'CKI District':'CKI District_1',
 'What CKI Position Do You Have?':'What CKI Position Do You Have?', 'Email Address':'Email Address_1','Phone Number':'Phone Number_1', 
 'Year in School':'Year in School_1', 'Favorite Means of Communication':'Favorite Means of Communication_1', 
 'What are some of your hobbies?':'What are some of your hobbies?_1',
 'What music genres do you listen to? Any specific artists?':'What music genres do you listen to? Any specific artists?_1',
 'What are your favorite movies and/or TV shows?':'What are your favorite movies and/or TV shows?_1',
 'What is your favorite service project?':'What is your favorite service project?_1',
 'Any ideas on how to stay active in CKI during the COVID-19 pandemic? ':'Any ideas on how to stay active in CKI during the COVID-19 pandemic?_1',
 'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)':'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)_1',
 'Is a hot dog a sandwich?':'Is a hot dog a sandwich?_1',
 'How often would you like to communicate with your buddy? ':'How often would you like to communicate with your buddy?_1'})

final_2 = final_2.rename(columns={'First Name':'First Name_2', 'Last Name':'Last Name_2', 'CKI District':'CKI District_2',
 'What CKI Position Do You Have?':'What CKI Position Do You Have?', 'Email Address':'Email Address_2','Phone Number':'Phone Number_2', 
 'Year in School':'Year in School_2', 'Favorite Means of Communication':'Favorite Means of Communication_2', 
 'What are some of your hobbies?':'What are some of your hobbies?_2',
 'What music genres do you listen to? Any specific artists?':'What types of music genre do you listen to? Any specific artists?',
 'What are your favorite movies and/or TV shows?':'What are your favorite movies and/or TV shows?_2',
 'What is your favorite service project?':'What is your favorite service project?_2',
 'Any ideas on how to stay active in CKI during the COVID-19 pandemic? ':'Any ideas on how to stay active in CKI during the COVID-19 pandemic?_2',
 'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)':'Why are you applying? What do you hope to get out of this? (Your response will be shared with your partner)_2',
 'Is a hot dog a sandwich?':'Is a hot dog a sandwich?_2',
 'How often would you like to communicate with your buddy? ':'How often would you like to communicate with your buddy?_2'})

#final.to_csv("all_pairings.csv")

#final_2.to_csv("Test_all_pairings.csv")
final['Partner Number']=final['Partner Number'].astype(object)
final_2['Partner Number']=final_2['Partner Number'].astype(object)

final_final= pd.merge(left=final, right=final_2, on=['Partner Number','What CKI Position Do You Have?'])

final_final.to_csv('Output_pairings.csv')