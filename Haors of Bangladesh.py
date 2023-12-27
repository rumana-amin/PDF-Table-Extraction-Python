# Extracting Multiple tables from single page and all pages in pdf code.

import tabula
import pandas as pd

def process_pdf_page(pdf_path, page_number, columns_to_drop, column_names, Upazila):
    # Read PDF and extract tables
    dfs = tabula.read_pdf(pdf_path, pages=page_number, multiple_tables=True)
    
    # Initialize an empty DataFrame to store the combined tables
    combined_df = pd.DataFrame(columns=column_names)


    # Process each table on the page
    for i, df in enumerate(dfs):
      
        # Delete the first column of the dataframe
        df.drop(df.columns[0], axis=1, inplace=True)
        
        # Name the columns
        df.columns = column_names

        # Create a new column Upazila
        df['Upazila'] = Upazila

        # Concatenate the current table with the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    return combined_df


# File Paths
pdf_path = 'HaorBD.pdf'

# Process the first, second, third and so on ..... page
df0 = process_pdf_page(pdf_path, 46, 0, ['Haor_name', 'Area(ha)'], 'Chhatak')
df1 = process_pdf_page(pdf_path, 48, 0, ['Haor_name', 'Area(ha)'], 'Dakshin Sunamganj')
df2 = process_pdf_page(pdf_path, 50, 0, ['Haor_name', 'Area(ha)'], 'Derai')
df3 = process_pdf_page(pdf_path, 52, 0, ['Haor_name', 'Area(ha)'], 'Dharampasha')
df4 = process_pdf_page(pdf_path, 53, 0, ['Haor_name', 'Area(ha)'], 'Dharampasha')
df5 = process_pdf_page(pdf_path, 55, 0, ['Haor_name', 'Area(ha)'], 'Dowarabazar')
df6 = process_pdf_page(pdf_path, 57, 0, ['Haor_name', 'Area(ha)'], 'Jagannathpur')
df7 = process_pdf_page(pdf_path, 59, 0, ['Haor_name', 'Area(ha)'], 'Jamalganj')
df7 = process_pdf_page(pdf_path, 61, 0, ['Haor_name', 'Area(ha)'], 'Sulla')
df8 = process_pdf_page(pdf_path, 63, 0, ['Haor_name', 'Area(ha)'], 'Sunamganj Sadar')
df9 = process_pdf_page(pdf_path, 65, 0, ['Haor_name', 'Area(ha)'], 'Tahirpur')
df10 = process_pdf_page(pdf_path, 72, 0, ['Haor_name', 'Area(ha)'], 'Balaganj')
df11 = process_pdf_page(pdf_path, 74, 0, ['Haor_name', 'Area(ha)'], 'Beani Bazar')
df12 = process_pdf_page(pdf_path, 76, 0, ['Haor_name', 'Area(ha)'], 'Bishwanath')
df13 = process_pdf_page(pdf_path, 78, 0, ['Haor_name', 'Area(ha)'], 'Companiganj')
df14 = process_pdf_page(pdf_path, 80, 0, ['Haor_name', 'Area(ha)'], 'Dakshin Surma')
df15 = process_pdf_page(pdf_path, 82, 0, ['Haor_name', 'Area(ha)'], 'Fenchuganj')
df16 = process_pdf_page(pdf_path, 84, 0, ['Haor_name', 'Area(ha)'], 'Golapganj')
df17 = process_pdf_page(pdf_path, 86, 0, ['Haor_name', 'Area(ha)'], 'Gowainghat')
#df18 = process_pdf_page(pdf_path, 87, 0, ['Haor_name', 'Area(ha)'], 'Gowainghat') 
#this table has five columns due to text wrap in one column - Need to add function for this
df19 = process_pdf_page(pdf_path, 89, 0, ['Haor_name', 'Area(ha)'], 'Jaintiapur')
df20 = process_pdf_page(pdf_path, 91, 0, ['Haor_name', 'Area(ha)'], 'Kanaighat')
df21 = process_pdf_page(pdf_path, 93, 0, ['Haor_name', 'Area(ha)'], 'Sylhet Sadar')
df22 = process_pdf_page(pdf_path, 95, 0, ['Haor_name', 'Area(ha)'], 'Zakiganj')
df23 = process_pdf_page(pdf_path, 102, 0, ['Haor_name', 'Area(ha)'], 'Ajmiriganj')
df24 = process_pdf_page(pdf_path, 104, 0, ['Haor_name', 'Area(ha)'], 'Bahubal')
df25 = process_pdf_page(pdf_path, 106, 0, ['Haor_name', 'Area(ha)'], 'Baniachong')
df26 = process_pdf_page(pdf_path, 108, 0, ['Haor_name', 'Area(ha)'], 'Habiganj Sadar')
df27 = process_pdf_page(pdf_path, 110, 0, ['Haor_name', 'Area(ha)'], 'Lakhai')  # Two tables in a page
df28 = process_pdf_page(pdf_path, 110, 0, ['Haor_name', 'Area(ha)'], 'Lakhai')
df29 = process_pdf_page(pdf_path, 112, 0, ['Haor_name', 'Area(ha)'], 'Nabiganj')
df30 = process_pdf_page(pdf_path, 120, 0, ['Haor_name', 'Area(ha)'], 'Barlekha')
df31 = process_pdf_page(pdf_path, 122, 0, ['Haor_name', 'Area(ha)'], 'Juri')
df32 = process_pdf_page(pdf_path, 124, 0, ['Haor_name', 'Area(ha)'], 'Kulaura')
df33 = process_pdf_page(pdf_path, 126, 0, ['Haor_name', 'Area(ha)'], 'Maulvibazar Sadar')
df34 = process_pdf_page(pdf_path, 128, 0, ['Haor_name', 'Area(ha)'], 'Rajnagar')
df35 = process_pdf_page(pdf_path, 130, 0, ['Haor_name', 'Area(ha)'], 'Sreemangal')
df36 = process_pdf_page(pdf_path, 138, 0, ['Haor_name', 'Area(ha)'], 'Atpara')
df37 = process_pdf_page(pdf_path, 140, 0, ['Haor_name', 'Area(ha)'], 'Barhatta')
df38 = process_pdf_page(pdf_path, 142, 0, ['Haor_name', 'Area(ha)'], 'Kalmakanda')
#df39 = process_pdf_page(pdf_path, 144, 0, ['Haor_name', 'Area(ha)'], 'Khaliajuri')
# In this table column 1 and column two are merged as one column in the dataframe. - Need to add function for this.
df40 = process_pdf_page(pdf_path, 146, 0, ['Haor_name', 'Area(ha)'], 'Madan')
df41 = process_pdf_page(pdf_path, 148, 0, ['Haor_name', 'Area(ha)'], 'Mohanganj')
df42 = process_pdf_page(pdf_path, 156, 0, ['Haor_name', 'Area(ha)'], 'Austagram')
df43 = process_pdf_page(pdf_path, 158, 0, ['Haor_name', 'Area(ha)'], 'Bajitpur')
df44 = process_pdf_page(pdf_path, 160, 0, ['Haor_name', 'Area(ha)'], 'Itna')
df45 = process_pdf_page(pdf_path, 162, 0, ['Haor_name', 'Area(ha)'], 'Karimganj')
df46 = process_pdf_page(pdf_path, 164, 0, ['Haor_name', 'Area(ha)'], 'Katiadi')
df47 = process_pdf_page(pdf_path, 166, 0, ['Haor_name', 'Area(ha)'], 'Kishoreganj Sadar') # Two tables in a page
df48 = process_pdf_page(pdf_path, 166, 0, ['Haor_name', 'Area(ha)'], 'Kuliar char')
df49 = process_pdf_page(pdf_path, 167, 0, ['Haor_name', 'Area(ha)'], 'Mithamain')
df50 = process_pdf_page(pdf_path, 168, 0, ['Haor_name', 'Area(ha)'], 'Nikli')
df51 = process_pdf_page(pdf_path, 169, 0, ['Haor_name', 'Area(ha)'], 'Pakundia')
df52 = process_pdf_page(pdf_path, 170, 0, ['Haor_name', 'Area(ha)'], 'Tarail')
df53= process_pdf_page(pdf_path, 178, 0, ['Haor_name', 'Area(ha)'], 'Akhaura') # Multiple Tables
df54 = process_pdf_page(pdf_path, 178, 0, ['Haor_name', 'Area(ha)'], 'Brahmanbaria Sadar')
df55 = process_pdf_page(pdf_path, 180, 0, ['Haor_name', 'Area(ha)'], 'Nasirnagar')
df56 = process_pdf_page(pdf_path, 182, 0, ['Haor_name', 'Area(ha)'], 'Sarail')



# Combine the DataFrames
combined_df = pd.concat([df0, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, 
                         df13, df14, df15, df16, df17, df19, df20, df21, df22, df23, df24, df25, df26, 
                         df27, df28, df29, df30, df32, df32, df33, df34, df35,df36, df37, df38, 
                          df40, df41, df42, df43, df44, df45, df46, df47, df48, df49, df50,
                         df51, df52, df53, df54, df55, df56], ignore_index=True)

# Deleting rows where either column value is 'NaN'
combined_df.dropna(subset=['Haor_name', 'Area(ha)'], inplace=True)

# Deleting rows where 'Haor_name' column value is 'Total'
combined_df = combined_df[combined_df['Haor_name'] != 'Total']


#print(combined_df)

combined_df.to_csv("combined_haor_area.csv", index=False )