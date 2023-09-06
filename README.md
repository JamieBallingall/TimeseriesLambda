# Excel LAMBDA functions for timeseries analysis

This repo contains three functions that might help you conduct timeseries analysis in Excel.
Specifically:
* ACFX: Compute the autocorrelation function on the residuals of an OLS regression
* PACFX: Compute the partial autocorrelation function on the residuals of an OLS regression
* CHOLESKY: Compute the Cholesky decomposition of a square, symmetric, positive definite matrix

For context on how to interpret ACF and PACF see
[https://spureconomics.com/interpreting-acf-and-pacf-plots/](https://spureconomics.com/interpreting-acf-and-pacf-plots/).

The definitions found in the `.lambda` are not suitable to copy directly into an Excel spreadsheet
because they contain comments, newlines and exceess spaces. The Python script `make_lambda.py`
strips all spaces, newlines and anything on a line appearing after `//` from the file, making it
suitable to copy-and-paste into an Excel named range. The useage is:

```
python make_lambda.py < WIBBLE.lambda > WIBBLE.min.lambda
```

Warning: do not use `make_lambda.py` on functions that manipulate strings, especially ones that
contain string literals with spaces in them since it will mangle them. All the functions in this
repo are safe, however.
