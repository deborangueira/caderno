# Comparison

| Aspect       | Structured Data | Unstructured Data |
|--------------|-----------------|-------------------|
| **Format**   | Has a strict, predefined data model. | Does not have a predefined format. |
| **Storage**  | Storage systems have rigid schemas, such as those in relational databases or data warehouses. | Often stored in its native format in nonrelational databases or data lakes. |
| **Use cases**| often applied in machine learning (ML) and drives ML algorithms. | Used in natural language processing (NLP) and is a rich, diverse data source for generative AI (gen AI) models. |
| **Complexity** | Easier to manipulate and analyze for general business users with traditional tools. | More complex and requires specialized skills and tools to parse and analyze. |

# Structured data

- can include both quantitative data (such as prices or revenue figures) and qualitative data (such as dates, names and addresses)
- stored in tabular formats, such as Excel spreadsheets and relational databases (or SQL databases)

**Advantages**

1. Esy access
2. Useful for machine learning
3. Simple data mining
4. Secure data management
5. Easy integration

**Disadvantages**

1. Limited flexibility
2. Limited storage data

**Tools**

1. spreadsheet
2. MySQL

# Semi-structured data

 - Uses metadata (for example, tags and semantic markers) to identify specific data characteristics
 - ex.: JavaScript Object Notation (JSON) and email (where some data sections have a standardized format (such as headers and subject lines) but unstructured data content within those sections)

# Unstructured data

**Advantages**

1. Acepts data in its **native format** as this type of data doesn't need to fit particular requires
2. Fast data collection
3. Great source of good insights
4. Easy scalability: as it doesn't need to update a particular database structure if new information is added
5. On-demand access (cheaper to store)

**Disadvantages**

1. Hard to analyse
2. Lack of specialized tools

# Concepts

1. Database: 
    - Design to store data and do transactions
    - Flexible schema
    - data is always updated
    - Work slowly for querying large amounts of data
2. Data Warehouse: 
    - created to analyse huge amount of data
    - Righd schema.
    - data is refreshed periodically
    - Fast
3. Data lake
    - Capture any type of data
    - Used for ML and AI

### Fonte

https://www.ibm.com/think/topics/structured-vs-unstructured-data\

https://www.youtube.com/watch?v=aIkTMkP1eto\

https://www.youtube.com/watch?v=-bSkREem8dM