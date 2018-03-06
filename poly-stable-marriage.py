import random

# Why not, right?
_int_names = [
    'John', 'Paul', 'George', 'Ringo', 'Lucy', 'Michelle', 'Rita', 'Pam'
]
_org_names = [
    'Org_A',
    'Org_B',
    'Org_C',
    'Org_D',
    'Org_E',
    'Org_F',
    'Org_G',
    'Org_H',
]

# Randomly generate a few random Orgs. and Interns. Note the 'max_interns' property of an Org.
_orgs = [{
    'name': _,
    'max_interns': random.randint (1, 1),
    'preferences': random.sample (_int_names, len (_int_names)),
} for _ in _org_names]

_total_internships = sum ([_['max_interns'] for _ in _orgs])
_ints = [{
    'name': _,
    'preferences': random.sample (_org_names, len (_org_names)),
} for _ in _int_names]

# Lists to keep track of tentative matches as well as Interns pending a match to an Org.
_matched = []
_pending = _int_names.copy ()

# Start
while len (_pending) > 0 and len (_matched) < _total_internships:
    for i_n in _pending:
        print ('On {}'.format (i_n))
        i = next ((_ for _ in _ints if _['name'] == i_n), None)
        if i is not None:
            for o_n in i['preferences']:
                print ('Trying Org. {}'.format (o_n))
                o = next ((_ for _ in _orgs if _['name'] == o_n), None)
                if o is not None:
                    x = o['max_interns']
                    m = [_ for _ in _matched if o_n in _]
                    if len (m) < x:
                        _matched.append ((i_n, o_n))
                        _pending.remove (i_n)
                        print ('{} is now tentatively interning at {}.'.format (i_n, o_n))
                        break
                    else:
                        print ('{} seems taken.'.format (o_n))
                        c = o['preferences'].index (m[0][0])
                        for n in m[1:]:
                            c = max (c, o['preferences'].index (n[0]))

                        d = o['preferences'].index (i_n)
                        if c < d:
                            print ('The Org. is happier with {} vs. {}.'.format (o['preferences'][c], i_n))
                        else:
                            print ('{} Appears to be a better match for Org. {} than {}.'.format (i_n, o_n, o['preferences'][c]))
                            _pending.remove (i_n)
                            _pending.append (o['preferences'][c])
                            _matched.remove ((o['preferences'][c], o_n))
                            _matched.append ((i_n, o_n))
                            break


