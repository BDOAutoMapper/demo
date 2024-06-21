import pandas as pd
import re

def mapper(mapping: dict, to_discard: list, df:pd.DataFrame):
    # df = df.rename(columns=mapping).drop(columns=to_discard)
    # return df
    try:
        df = df.rename(columns=mapping)
        for col in to_discard:
            try:
                df = df.drop(columns=[col])
            except KeyError:
                print(f"Column '{col}' not found in the DataFrame and will be skipped.")
    except KeyError as e:
        print(f"Error: {e}")
        print("Please check the column names in the mapping dictionary and to_discard list.")
    return df

    
    

def extract_substrings(big_string, substring_list):
    substrings = []
    pattern = r"\b(" + "|".join(map(re.escape, substring_list)) + r")\b"
    for match in re.finditer(pattern, big_string):
        substrings.append(match.group())
    return substrings

def transform_nonstandard_SAP(df: pd.DataFrame, new_column_name: str):
    grouper_column = df.columns[0]
    grouper_values = df[grouper_column]
    # Drop the "grouper_column" we don't need it anymore.
    in_df = df.drop(columns=[grouper_column])
    group_defined_list = list(grouper_values.isna())
    index_rows_for_group = []
    keys = []
    results = {}

    # For each entry in our boolean array
    for index, is_group_defined in enumerate(group_defined_list):
        if is_group_defined is True:
            # Have we identified any keys?
            if len(keys) > 0:
                results[tuple(keys)] = index_rows_for_group
                keys = []
                index_rows_for_group = []
            index_rows_for_group.append(index)
        else:
            value = grouper_values[index]
            keys.append(value)
    
    # Iterate through the results
    # Building the df again with the subsets
    subset_dfs = []
    for value_key, df_indices in results.items():
        subset_df = in_df.loc[df_indices].copy()
        subset_df[new_column_name] = [value_key] * len(subset_df)
        subset_dfs.append(subset_df)
    sub_df = pd.concat(subset_dfs)
    return sub_df