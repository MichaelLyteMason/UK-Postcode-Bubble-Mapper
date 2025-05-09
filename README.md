# UK-Postcode-Bubble-Mapper
Plot occurrences as diameter of bubbles with scalability anywhere in the UK using postcodes.

## Libraries:
- pandas
- pgeocode
- geopandas
- matplotlib
- contextily

## Instructions For Use
1. Create a csv file named "data.csv" where cell A1 contains the text "Postcode" and cell B1 contains the text "Frequency".
2. Populate each column with their respective data eg:

| Postcode    | Frequency |
| -------- | ------- |
| AA1 1AA  | 50    |
| AA2 2AA | 200     |
| AA3 3AA    | 156    |

3. These will then be plotted on a map that covers all the postcodes included in the plotted region and will also group many of them.

It is worth noting that adjusting the "scale_factor" in "heatmapValue.py" is useful for reaching the desired appearance and scaling of bubbles.
This project was made with the use of LLMs.
