# Population-Weighted Lorenz Curve Analysis of Universal Health Coverage (UHC-SCI)

Author:** Atiq Kainan Ahmed  
Email:** atiqka@yahoo.com

---

## Overview

This repository provides a Python-based workflow for assessing inequality in the **Universal Health Coverage Service Coverage Index (UHC-SCI)** using **population-weighted Lorenz curves** and **Gini coefficients**. The analysis is designed to move beyond national averages and explore how equitably health service coverage is distributed across populations within different World Bank income groups.

By incorporating population weights, the methodology reflects the experience of people rather than simply comparing countries as equal units. This approach provides a more meaningful assessment of equity in health coverage and can support evidence-based policy discussions on universal health coverage and health system performance.

---

## Why This Analysis Matters

Global averages often conceal large disparities in health service coverage. Two countries may contribute equally to a statistical average despite having vastly different population sizes. As a result, traditional analyses may underestimate or misrepresent inequality experienced by people.

This repository addresses this challenge by:

- Incorporating population weights into inequality calculations.
- Measuring disparities in UHC service coverage within income groups.
- Providing visual and quantitative evidence of equity gaps.
- Supporting global health, development, and policy research.

The resulting Lorenz curves and Gini coefficients help answer a fundamental question:

> How equally are UHC services distributed among populations within different income groups?

---

## Objectives

The script aims to:

- Quantify inequality in UHC-SCI among countries.
- Calculate population-weighted Lorenz curves.
- Estimate population-weighted Gini coefficients.
- Compare UHC coverage distributions across income groups.
- Generate publication-ready visualizations.
- Provide a reproducible framework for equity-focused analyses.

---

## Data Requirements

The input dataset should contain the following variables:

| Variable | Description |
|-----------|-------------|
| `countryname` | Country name |
| `uhc_sci` | Universal Health Coverage Service Coverage Index |
| `inc_grp` | World Bank income group classification |
| `pop` | Population used as analytical weights |

Example structure:

```text
countryname,uhc_sci,inc_grp,pop
Bangladesh,67,Lower middle income,171186372
Thailand,81,Upper middle income,71801279
Germany,86,High income,84369500
```

The script automatically removes observations with missing values before conducting the analysis.

---

## Methodology

The analytical workflow follows standard inequality measurement approaches commonly used in economics and development studies.

### Step 1: Data Preparation

The script imports the dataset and retains the following variables:

- Country name
- UHC-SCI score
- Income group
- Population

Observations with missing data are removed.

### Step 2: Income Group Classification

Countries are divided into four World Bank income categories:

1. High income
2. Upper middle income
3. Lower middle income
4. Low income

### Step 3: Population-Weighted Lorenz Curves

For each income group, the script computes a Lorenz curve using the `ineqpy` package.

The Lorenz curve plots:

- Cumulative share of population (x-axis)
- Cumulative share of UHC-SCI coverage (y-axis)

### Step 4: Population-Weighted Gini Coefficients

The script calculates a population-weighted Gini coefficient for each income group.

Interpretation:

- **0** = Perfect equality
- **1** = Perfect inequality

Higher values indicate larger disparities in UHC service coverage.

### Step 5: Visualization

Results are displayed in a 2×2 faceted figure showing:

- Lorenz curves
- Line of perfect equality
- Shaded inequality areas
- Population-weighted Gini coefficients

---

## Output

The analysis generates a high-resolution PNG figure:

```text
lorenz_facets_uhc_ordered.png
```

The output contains four panels corresponding to:

- High income countries
- Upper middle income countries
- Lower middle income countries
- Low income countries

Each figure presents both graphical and numerical measures of inequality.

---

## Interpreting the Results

### Lorenz Curve

The closer the Lorenz curve lies to the 45-degree line of equality, the more equitable the distribution of UHC service coverage.

A pronounced curve away from the equality line indicates increasing inequality.

### Gini Coefficient

The Gini coefficient provides a concise summary measure:

| Gini Value | Interpretation |
|------------|----------------|
| 0.00 | Perfect equality |
| 0.10–0.20 | Low inequality |
| 0.20–0.40 | Moderate inequality |
| >0.40 | High inequality |

These thresholds should be interpreted contextually depending on the indicator and dataset.

---

## Software Requirements

The script is written in Python and uses the following libraries:

- pandas
- matplotlib
- ineqpy

Install dependencies using:

```bash
pip install pandas matplotlib ineqpy
```

---

## Running the Script

Update the input and output file locations within the script:

```python
data_path = "path/to/your/data.csv"
```

Run the script:

```bash
python uhc_lorenz.py
```

After successful execution, the figure will be saved to the specified output directory.

---

## Potential Applications

While developed for Universal Health Coverage Service Coverage Index (UHC-SCI), the methodology can be applied broadly to assess equity and distributional outcomes across development sectors.

Examples include:

### Health

- Health expenditure
- Vaccination coverage
- Child mortality indicators
- Maternal health indicators

### Climate and Environment

- Climate finance allocation
- Adaptation investments
- Nature-based solutions financing
- Disaster risk exposure

### Social Development

- Social protection coverage
- Educational attainment
- Access to public services
- Poverty reduction investments

---

## Why Population Weighting Matters

Many international comparisons treat countries as equal units regardless of population size. This can lead to misleading conclusions about equity.

For example, a country with 2 million people and a country with 200 million people would receive the same weight in a conventional analysis despite the large difference in the number of people affected.

By incorporating population weights, this framework provides a more realistic representation of how services are distributed across populations rather than across countries.

---

## Future Enhancements

Potential extensions include:

- Regional Lorenz curves
- Time-series analysis
- Trend analysis of Gini coefficients
- Climate finance equity assessments
- Equity-adjusted development indicators
- Concentration curves using vulnerability metrics
- Dashboard integration and interactive visualizations

---

## Citation

If you use this repository in research, reports, policy analysis, or academic publications, please cite:

> Ahmed, A. K.(2026). Population-Weighted Lorenz Curve Analysis of Universal Health Coverage Service Coverage Index (UHC-SCI). GitHub Repository.

---



---

## License

This project is released under the MIT License.

You are free to use, modify, and distribute the code with appropriate attribution.
