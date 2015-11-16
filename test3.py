from requests import Request, Session

s = Session()
# req = Request('GET', "https://steelseries.zendesk.com/api/v2/users/me.json")

s.auth = ('ege.demirel@steelseries.com', 'Fz4Kavncy49mTV6HCN6A')
q = {"email": "ege.demirel@steelseries.com", "password": "Fz4Kavncy49mTV6HCN6A"}
# s.headers.update({'x-test': 'true'})
s.get("https://steelseries.zendesk.com")
# csrftoken = s.cookies['']]

s.post("https://id.steelseries.com/zendesk", data=q)

for i in s.cookies:
    print i

r = s.get("https://steelseries.zendesk.com")

# print r.content

# r = s.get("https://analytics.zendesk.com/#s=/gdc/projects/oj4pd7uox9b8zlqq1fh3xa4disp1rasz|projectDashboardPage|")



# from urllib2 import Request, urlopen

# values = """
#   {
#     "postUserLogin": {
#       "login": "ege.demirel@steelseries.com",
#       "password": "x8Z6pfGZ",
#       "remember": 1
#     }
#   }
# """

# headers = {
#   'Content-Type': 'application/json',
#   'Accept': 'application/json'
# }
# request = Request('https://analytics.zendesk.com/gdc/account/login', data=values, headers=headers)

# response_body = urlopen(request).read()
# print response_body
