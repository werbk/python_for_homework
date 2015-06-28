from tests_group.group_helper import Group
from fixture.TestBase import random_string
import string
import random
import jsonpickle
import json
import getopt
import sys




try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:

    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.json'

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = str(a)



test_data = [Group(group_name='', group_header='', group_footer='')] + [Group(group_name=random_string('name', 10),
                                                                              group_header=random_string('header', 10),
                                                                              group_footer=random_string('footer', 10))
                                                                              for i in range(n)]

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))