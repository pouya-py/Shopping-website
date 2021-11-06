# import csv

# with open('test.csv', 'w',newline='', encoding='utf-8') as f:
#     # writer = csv.writer(f,quotechar='|')
#     # writer.writerows([['first_name'],['last_name']])
#     fieldnames = ['first_name','last_name']
#     anotherwriter = csv.DictWriter(f,fieldnames=fieldnames)
#     anotherwriter.writeheader()
#     anotherwriter.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     anotherwriter.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})

#---------------
from django.conf import settings
settings.configure()

# field = [field for field in range(1,10) ]
# print(field)
# from django.http import QueryDict

# q = QueryDict('a=1&b=12',mutable=True)
# q.update({'a':'5'})
# q['next'] = '/a&b/'
# print(q.urlencode(safe='/&')) 
# print(q.getlist('a'))

# from django.http import JsonResponse

# respose = JsonResponse([1,3,5],safe=False)
# print(respose.content)