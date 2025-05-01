import pandas as pd

# Step 1: Load your Excel file into DataFrame clearly
df = pd.read_excel('/Users/tharun/Downloads/emotions.xlsx')

# Step 2: Define the analysis function clearly
def emotion_probability_analysis(df):
    results = []

    statements = set(col.rsplit(' - ', 1)[0] for col in df.columns)

    for stmt in statements:
        statement_result = {'Statement': stmt}
        
        for dimension in ['SADNESS-JOY', 'TRUST-DISGUST', 'FEAR-ANGER', 'SURPRISE-ANTICIPATION']:
            col_name = f'{stmt} - {dimension}'

            if col_name in df.columns:
                responses = df[col_name].dropna()
                total = len(responses)

                positive_side = (responses > 0).mean()
                negative_side = (responses < 0).mean()
                neutral_side = (responses == 0).mean()

                combined_probability = 1 - (1 - positive_side)*(1 - negative_side)

                statement_result[f'{dimension} Positive'] = positive_side
                statement_result[f'{dimension} Negative'] = negative_side
                statement_result[f'{dimension} Neutral'] = neutral_side
                statement_result[f'{dimension} Combined Probability'] = combined_probability

        results.append(statement_result)

    return pd.DataFrame(results)

emotional_summary_df = emotion_probability_analysis(df)

print(emotional_summary_df.head())

emotional_summary_df.to_excel('/Users/tharun/Downloads/emotional_summary_analysis.xlsx', index=False)
