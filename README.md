## Python-PDF-Table-Extraction
### Project Overview
The Portable Document Format (PDF), introduced by Adobe in 1992, revolutionized document presentation by ensuring independence from specific application software, hardware, and operating systems. With an estimated global count surpassing 3 trillion, PDFs play a vital role in storing text-formatted content and images. This project addresses the growing need to extract textual and tabular information from PDFs.

The task involves extracting over 100 tables of diverse formats from two specific PDF files. These files are sourced from the Department of Bangladesh Haor and Wetlands Development website (https://dbhwd.portal.gov.bd/).
### Tools
 - Language: Python
 - Libraries: tabula-py, pandas
### Learning Focus
This project offers an opportunity for a deeper understanding of Python functions and honing skills in data cleaning and transformation using the pandas library.


```python
def extract_table_second_page(pdf_path, start_page, end_page):
    all_tables = []
    for page in range(start_page, end_page + 1):
        current_page_tables = tabula.read_pdf(pdf_path, pages=page)
        all_tables.extend(current_page_tables)
   
    concatenated_df = pd.concat(all_tables, ignore_index=True)
    concatenated_df.drop(concatenated_df.columns[[0, 1, -1]], axis=1, inplace=True)
    return concatenated_df
```
This Python function, extract_table_second_page, systematically reads and extracts tables from specified pages within a PDF. It utilizes the tabula-py library for PDF parsing and pandas for subsequent data manipulation. The resulting concatenated dataframe undergoes column removal for cleaning and refinement.
