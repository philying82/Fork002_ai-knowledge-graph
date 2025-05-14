MAIN_SYSTEM_PROMPT = """
You are an advanced contract assistant working for Robert Half Inc. and specialized in entity and high-risk clause extraction from third-party contract.
Your expertise includes identifying counterparty entity information, services provided by the counterparty and high-risk clause in the contract.
"""


MAIN_USER_PROMPT_V1 = """ 
Your task: you will be provided third-party vendor contracts (delimited by triple backticks) chunks for the Rober Half Inc. Your task is to identify import entities (described below) from the contract.

Follow these rules and steps carefully:
- Entity Specification: Only extract specific entities fields mentioned below.
 
Steps:
- Set Robert Half to be the primary entity
- The possible subsidiaries for Robert Half are Protiviti and Accountemps Inc (**note can be updated later)
- Scan the document to see who the contract is between. Set the entity that is providing the services as the counterparty.
- Extract these entity fields if found in the contract and place N/A if not found:  counterparty description, service name, service description, term effective date, term start date, term end date, term short description
- If there are multiple services found then itemize them and add them to the JSON
- Populate the entities provided above into the JSON below mapping the fields to their corresponding place with the appropriate subsidiary or primary entity. If the contract is directly with Robert Half, assign the counterparty to them.
 
- Entity Consistency: Use consistent names for entities throughout company legal contract document. For example, if "LinkedIn Coporate" is mentioned as "LinkedIn", use a single consistent form (preferably the most complete one).
- Atomic Terms: Identify distinct key terms (e.g., companies, locations, acronyms). Avoid merging multiple ideas into one term (they should be as "atomistic" as possible).
- Unified References: Replace any pronouns (e.g., "it," "they," etc.) with the actual referenced entity, if identifiable.
 
Output Format:
- Do not include any text or commentary outside of the JSON.
- Return only the JSON array.
- Make sure the JSON is valid and properly formatted. See provided example below.
Example of the desired output structure:

{
      "primaryEntity": {
        "id": "pe-001",
        "name": "Robert Half Inc.",
        "description": "Parent company",       

        "counterparties": 
        [
          {
            "id": "cp-001",
            "name": "LinkedIn",
            "description": "Talent Repository",
            "contractDates": {
                "effectiveDate": "2025-01-22",
                "endDate": "2025-04-10"
                },
            
            "services": [                
                    {
                      "id": "svc-001",
                      "name": "Talent Management ",
                      "description": "Provides talent validation"
                      }
                    ]

           
            }
        ]	         
      }
    }
            

      
Text to analyze (between triple backticks):

 """



MAIN_USER_PROMPT_V2 = """ 
Your task: you will be provided third-party vendor contracts (delimited by triple backticks) chunks for the Rober Half Inc. Your task is to identify import entities (described below) from the contract.

Follow these rules and steps carefully:
- Entity Specification: Only extract specific entities fields mentioned below.
 
Steps:
- Set Robert Half to be the primary entity
- The possible subsidiaries for Robert Half are Protiviti and Accountemps Inc (**note can be updated later)
- Scan the document to see who the contract is between. Set the entity that is providing the services as the counterparty.
- Extract these entity fields if found in the contract and place N/A if not found:  counterparty description, service name, service description, term effective date, term start date, term end date, term short description
- If there are multiple services found then itemize them and add them to the JSON
- Populate the entities provided above into the JSON below mapping the fields to their corresponding place with the appropriate subsidiary or primary entity. If the contract is directly with Robert Half, assign the counterparty to them.
 
- Entity Consistency: Use consistent names for entities throughout company legal contract document. For example, if "LinkedIn Coporate" is mentioned as "LinkedIn", use a single consistent form (preferably the most complete one).
- Atomic Terms: Identify distinct key terms (e.g., companies, locations, acronyms). Avoid merging multiple ideas into one term (they should be as "atomistic" as possible).
- Unified References: Replace any pronouns (e.g., "it," "they," etc.) with the actual referenced entity, if identifiable.
 
Output Format:
- Do not include any text or commentary outside of the JSON.
- Return only the JSON array.
- Make sure the JSON is valid and properly formatted. See provided example below.
Example of the desired output structure:

{{
      "primaryEntity": {{
        "id": "pe-001",
        "name": "Robert Half Inc.",
        "description": "Parent company",       

        "counterparties": 
        [
          {{
            "id": "cp-001",
            "name": "LinkedIn",
            "description": "Talent Repository",
            "contractDates": {{
                "effectiveDate": "2025-01-22",
                "endDate": "2025-04-10"
                }},
            
            "services": [                
                    {{
                      "id": "svc-001",
                      "name": "Talent Management ",
                      "description": "Provides talent validation"
                      }}
                    ]

           
            }}
        ]	         
      }}
    }}

            

      
Text to analyze (between triple backticks): {input_text}

 """


MAIN_USER_PROMPT_HIGH_RISK_CLAUSE_V1 = """ 

Your task: you will be provided third-party vendor contracts chunks for the Rober Half Inc. 
Read the contract text chunk below (delimited by triple backticks) and identify any high-risk or non-standard clauses from the contract. 

Follow these rules and steps carefully:
 
Steps:
- 
- Based on the service specified in the contract, identify and extract high-risk or non-standard clauses from the contract.
- Populate the result in LIST format below.
 
Output Format:
- Do not include any text or commentary outside of the LIST.
- Make sure the LIST is valid and properly formatted. See provided example below.

Example of the desired output structure:                    
  [some clause, 
   some clause,
   some clause]           


Text to analyze (between triple backticks):

"""

MAIN_USER_PROMPT_HIGH_RISK_CLAUSE_V2 = """ 

Your task: you will be provided third-party vendor contracts chunks for the Rober Half Inc. 
Read the contract text chunk below (delimited by triple backticks) and identify any high-risk or non-standard clauses from the contract. 

Follow these rules and steps carefully:
 
Steps:
- 
- Based on the service specified in the contract, identify and extract high-risk or non-standard clauses from the contract.
- Populate the result in LIST format below.
 
Output Format:
- Do not include any text or commentary outside of the JSON.
- Return only the JSON array.
- Make sure the JSON is valid and properly formatted. See provided example below.
- 
Example of the desired output structure:

Example of the desired output structure:  

{{ "high-risk clauses": [
            "some high-risk clause", 
            "some high-risk clause", 
            "some high-risk clause",
            "some high-risk clause",
            ]           

}}  

Text to analyze (between triple backticks):{input_text}

"""