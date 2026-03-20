import pandas as pd

print("Select Report Type:")
print("1 - NBS-1 Report")
print("2 - ALM Report")

choice = input("Enter choice (1/2): ")
# for NBS
if choice == "1":
    input_df = pd.read_excel("input_data.xlsx")
    mapping_df = pd.read_excel("mapping.xlsx")

    mapping_dict = dict(zip(mapping_df['Input_Field'], mapping_df['Output_Field']))

    output_rows = []

    for _, row in input_df.iterrows():
        if row['Category'] in mapping_dict:
            output_rows.append({
                "Particulars": mapping_dict[row['Category']],
                "Amount": row['Value']
            })

    output_df = pd.DataFrame(output_rows)
    output_df = output_df.sort_values(by="Particulars")

    output_df.to_excel("NBS1_Output.xlsx", index=False)

    print("NBS-1 Report Generated!")

#for Alm
elif choice == "2":
    df = pd.read_excel("alm_input.xlsx")

    output_df = df.pivot_table(
        index="Bucket",
        columns="Type",
        values="Amount",
        aggfunc="sum"
    ).reset_index()

    output_df.columns.name = None
    output_df = output_df.rename(columns={"Bucket": "Time Bucket"})
    output_df = output_df.fillna(0)

    output_df.to_excel("ALM_Output.xlsx", index=False)

    print("ALM Report Generated!")


#  INVALID 
else:
    print("Invalid choice. Please select from 1 or 2.")