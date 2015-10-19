#!/usr/bin/python

import re
from ouidb import OuiDb

def gen_maclist_pop_wifi():
    """
    Generate a file called maclist.lst with the list of the most popular wifi
    MAC prefixes and the name of the vendor for those addresses
    """
    o = OuiDb()
    pop = o.find_by_popular()
    regex = re.compile(".*{0}.*".format('wireless'), re.IGNORECASE)
    popwifi=[x for x in pop for y in x['devices'] if regex.match(y['device_type']
    ml = ["%s   %s" % (p['vendor_prefix'], p['vendor_name']) for p in popwifi]
    with open('maclist.lst','w') as f:
        f.write('\n'.join(ml))

def main()
    gen_maclist_pop_wifi()

if __name__ == '__main__':
    main()
