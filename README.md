# Sponsors-Search

The list of [licensed visa sponsors](https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers) avaliable in the gov.uk website is in PDF format. This is not ideal. This repo contains code to convert it into nice formats (csv, json) and serve it in a searchable html page.

Webpage currently avaliable [here](https://antoniocampello.com/sponsors-search/).

The code is under MIT and all the data contains public sector information licensed under the Open Government Licence v3.0.

## Scripts

The code:

- Downloads the PDF in https://www.gov.uk/government/publications/register-of-licensed-sponsors-workers
- Does some nice tricks to extract a table from that
- Generates a JSON and a CSV
- Includes a index.html to serve it as a front-end.

The code is set up to update periodically (every week).

## Want to contribute?

Open a pull request/issue.
