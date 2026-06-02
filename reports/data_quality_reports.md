# Data Quality Summary

## Validation Performed

- Compared all `amfi_code` values in `fund_master` against `nav_history`.
- Checked for duplicate AMFI codes.
- Checked for missing values in both datasets.
- Reviewed category and risk classification fields.

## Results

- Total schemes in `fund_master`: **40**
- Total unique AMFI codes in `fund_master`: **40**
- Total unique AMFI codes in `nav_history`: **40**
- Missing AMFI codes in `nav_history`: **0**
- Duplicate AMFI codes in `fund_master`: **0**

## Data Quality Observations

- Every AMFI code in `fund_master` exists in `nav_history`.
- No duplicate AMFI codes were found.
- No missing values were detected in critical fields.
- Category, sub-category, and risk-category fields are populated and consistent.
- Dataset structure is suitable for further analysis and reporting.

## Conclusion

The datasets passed the basic data quality checks. AMFI code validation was successful, and the data is ready for downstream processing and analysis.