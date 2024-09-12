# Portfolio Analysis

The goal is to analyze the performance of a portfolio.

The data is stored in 2 CSV files with the following columns:

For `portfolio.csv`:
- `name`: the name of the asset
- `shares`: the number of shares of the asset
- `price`: the price of the asset at the time of purchase

For `prices.csv`:
- the first column is the name of the asset
- the second column is the current price of the asset


Run the code using the command below:

    ```shell
    python report.py --portfolio data/portfolio.csv --prices data/prices.csv
    ```

The output should be a table with the following columns:

    ```shell
        Name     Shares      Price     Change
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84
    ```
