# import http.client

# host = 'jooble.org'
# key = '86766a54-ca75-417b-ac2a-bc9ce55f8fa1'

# connection = http.client.HTTPSConnection(host)

# headers = {"Content-type": "application/json"}

# body = '{"keywords": "software engineer", "location": "Philippines"}'
# connection.request('POST', '/api/' + key, body, headers)
# response = connection.getresponse()
# print(response.status, response.reason)
# print(response.read())

# import requests

# headers = {
#   "X-API-Key": "ak_5ghg605pw970ba18yle8tz7yc73dfe7tux8pzs6yanyk5yg"
# }

# response = requests.request(
#     'GET',
#     'https://api.openwebninja.com/jsearch/search-v2',
#     params={
#         "query":"sofware developer in philippines",
#         "country":"ph",
#         "date_posted": "month",
#         "employment_types": "FULLTIME",
#     },


#     headers=headers
# )

# data = response.json()
# print(data)

from jobspy import scrape_jobs
from jobspy.model import Site
import csv
import pandas as pd

jobs = scrape_jobs(
    site_name=[Site.INDEED, Site.LINKEDIN, Site.GOOGLE],
    search_term="software engineer",
    google_search_term="softare engineer in philippines",
    location='Philippines',
    distance=50,
    is_remote=False,
    job_type="fulltime",
    easy_apply=None,
    results_wanted=100,
    country_indeed="Philippines",
    proxies=None,
    ca_cert=None,
    description_format="markdown",
    linkedin_fetch_description=False,
    linkedin_company_ids=None,
    offset=0,
    hours_old=None,
    enforce_annual_salary=False,
    verbose=0,
    user_agent=None,
)

jobs.to_csv(
    "jobs.csv",
    quoting=csv.QUOTE_NONNUMERIC,
    escapechar="\\",
    index=False,
)

jobs.to_excel("jobs.xlsx", index=False)