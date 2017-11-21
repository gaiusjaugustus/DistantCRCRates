# Document to separate out Races and save different files

import pandas as pd


file = 'K:/SEER_DataTables/wStandardPops/SEER_2000-2014_StageDistribution_StageAgeRace.txt'
StageAgeRace = pd.read_csv(file, sep='\t')

print(StageAgeRace.head())

StageAgeRace_filt = StageAgeRace[StageAgeRace['Summary stage 2000 (1998+)'].isin(['Localized','Regional','Distant'])]
StageAgeRace_filt = StageAgeRace_filt[StageAgeRace_filt['Year of diagnosis'] != '2000-2014']
StageAgeRace_filt = StageAgeRace_filt[StageAgeRace_filt['Age recode with <1 year olds'] != 'Unknown']
print(StageAgeRace_filt.head())


AA = StageAgeRace_filt[StageAgeRace_filt['Race recode (W, B, AI, API)'] == 'Black']
White = StageAgeRace_filt[StageAgeRace_filt['Race recode (W, B, AI, API)'] == 'White']
AI = StageAgeRace_filt[StageAgeRace_filt['Race recode (W, B, AI, API)'] == 'American Indian/Alaska Native']
API = StageAgeRace_filt[StageAgeRace_filt['Race recode (W, B, AI, API)'] == 'Asian or Pacific Islander']

AA.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeBlack_forJoinpoint.txt', sep='\t', index=False)
White.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeWhite_forJoinpoint.txt', sep='\t', index=False)
AI.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeAmericanIndian_forJoinpoint.txt', sep='\t', index=False)
API.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeAsian_forJoinpoint.txt', sep='\t', index=False)

# Separate Sex and save different files
file = 'K:/SEER_DataTables/wStandardPops/SEER_2000-2014_StageDistribution_StageAgeSex.txt'
StageAgeSex = pd.read_csv(file, sep='\t')

print(StageAgeSex.head())

StageAgeSex_filt = StageAgeSex[StageAgeSex['Summary stage 2000 (1998+)'].isin(['Localized','Regional','Distant'])]
StageAgeSex_filt = StageAgeSex_filt[StageAgeSex_filt['Year of diagnosis'] != '2000-2014']
StageAgeSex_filt = StageAgeSex_filt[StageAgeSex_filt['Age recode with <1 year olds'] != 'Unknown']
print(StageAgeSex_filt.head())


Male = StageAgeSex_filt[StageAgeSex_filt['Sex'] == 'Male']
Female = StageAgeSex_filt[StageAgeSex_filt['Sex'] == 'Female']

Male.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeMale_forJoinpoint.txt', sep='\t', index=False)
Female.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeFemale_forJoinpoint.txt', sep='\t', index=False)



# Assign Age and then create separate files for age categories.
StageAge = pd.read_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeAgecat_forJoinpoint.txt', sep="\t")
print(StageAge.head())

Early = StageAge[StageAge['Age Category'] == 1]
Middle = StageAge[StageAge['Age Category'] == 2]
Late = StageAge[StageAge['Age Category'] == 3]

Early.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeEarly_forJoinpoint.txt', sep='\t', index=False)
Middle.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeMiddle_forJoinpoint.txt', sep='\t', index=False)
Late.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeLate_forJoinpoint.txt', sep='\t', index=False)

# Tumor Locations
StageSite = pd.read_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeSite_forJoinpoint.txt', sep='\t')

Distal = StageSite[StageSite['Colorectal Sidedness (Right,Left)'] == "Distal Colorectal Cancer"]
Proximal = StageSite[StageSite['Colorectal Sidedness (Right,Left)'] == "Proximal Colorectal Cancer"]

Distal.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeDistal_forJoinpoint.txt', sep='\t', index=False)
Proximal.to_csv('U:/Box Sync/ProjectDocs/2017_DistantCRC/ProcessedTables/Rate_StageAgeProximal_forJoinpoint.txt', sep='\t', index=False)