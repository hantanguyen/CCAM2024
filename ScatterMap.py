import pandas as pd
import plotly.express as px

file_path = '/mnt/c/Users/hanta/OneDrive/Desktop/CCAM/CCAM2024_DATA - Sheet3.csv'
df = pd.read_csv(file_path)

def categorize_provider(provider_name, transgender_friendly):
    if "CVS" in provider_name:
        return f"CVS - {'Yes' if transgender_friendly == 'Yes' else 'No'}"
    elif "Walgreens" in provider_name:
        return f"Walgreens - {'Yes' if transgender_friendly == 'Yes' else 'No'}"
    else:
        return f"Other - {'Yes' if transgender_friendly == 'Yes' else 'No'}"

df['ProviderCategoryStatus'] = df.apply(lambda row: categorize_provider(row['ProviderName'], row['TransgenderFriendly']), axis=1)

fig = px.scatter_mapbox(df,
                        lat="latitude",
                        lon="longitude",
                        hover_name="ProviderName",
                        hover_data={"Location": True, "PhoneNumber": True, "Review": True, "Specialty": True, "TransgenderFriendly": True},
                        color="ProviderCategoryStatus",
                        color_discrete_map={
                            "CVS - Yes": "lightblue",
                            "CVS - No": "orange",
                            "Walgreens - Yes": "blue",
                            "Walgreens - No": "red",
                            "Other - Yes": "green",
                            "Other - No": "gray"
                        },
                        zoom=10,
                        title="Transgender Friendly Providers Scatter Map",
                        mapbox_style="open-street-map")

fig.update_traces(marker=dict(size=12))

fig.write_html('/mnt/c/Users/hanta/OneDrive/Desktop/CCAM/scatter_map.html')
print(f"Scatter map saved as /mnt/c/Users/hanta/OneDrive/Desktop/CCAM/scatter_map.html")