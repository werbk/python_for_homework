from tests_group.group_helper import Group
from fixture.TestBase import random_string
import jsonpickle
import os.path
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

'''def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' ' #+ string.punctuation
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])'''
'''
test_data = [
    Group(group_name=name, group_header=header, group_footer=footer)
    for name in ['', random_string('name', 10)]
    for header in ['', random_string('header', 20)]
    for footer in ['', random_string('footer', 20)]]'''

test_data = [Group(group_name='', group_header='', group_footer='')] + [Group(group_name=random_string('name', 10),
                                                                              group_header=random_string('header', 10),
                                                                              group_footer=random_string('footer', 10))
                                                                              for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(test_data))