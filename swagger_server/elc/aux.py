"""Auxilary functions for the API controllers."""


def set_timestamp():
    """Format POSIX UTC time for metadata."""
    from time import gmtime

    t = gmtime()
    return '{0:4d}-{1:02d}-{2:02d} {3:02d}:{4:02d}:{5:02d} UTC'.format(
        t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)


def get_checksum(data, full=False):
    """Calculate an md5 hash of an object and return short form."""
    import hashlib
    import pickle

    if full:
        # Full checksum
        return hashlib.md5(pickle.dumps(data)).hexdigest()
    else:
        # GitHub style 7 character abbreviated form
        return hashlib.md5(pickle.dumps(data)).hexdigest()[0:7]


def build_filename(endpoint, data):
    """Compose a filename for CSV return."""
    from ..elc import aux

    datatype = {'occ': 'occurrences',
                'ref': 'references',
                'tax': 'taxa',
                'loc': 'locales'}

    return 'elc_{0:s}_{1:s}.csv'.format(datatype.get(endpoint),
                                        get_checksum(data=data))


def set_db_special(db, endpoint):
    """Add custom payload additions unique to a specific db."""
    if db == 'pbdb' and endpoint in ['loc', 'occ']:
        return {'show': 'full'}

    if db == 'pbdb' and endpoint in ['ref']:
        return {'show': 'both'}

    # Add another database specific case here
    else:
        return {}


def get_id_numbers(data, endpoint):
    """Return a list of the specified endpoint's primary id numbers."""
    ids = set()
    id_field = '{0:s}_id'.format(endpoint)

    for rec in data:
        ids.add(rec.get(id_field))

    return list(ids)


def build_meta(options):
    """Generate metadata for the composite return."""
    from ..elc import config, aux

    return {'license': config.get('default', 'license'),
            'retrieval_timestamp': aux.set_timestamp(),
            'source': 'http://earthlifeconsortium.org',
            'age_units': options.get('ageunits'),
            'coordinates': options.get('geog')}


def build_meta_sub(source, t0, sub_tag, options, data=None):
    """Generate database specific metadata object for the return."""
    from time import time

    if data and type(data) is list:
        rec_count = len(data) - options.get('tot_rec_count')
        options.update(tot_rec_count=len(data))
    else:
        if data == []:
            rec_count = 0
        else:
            rec_count = 1

    return {sub_tag: {'subquery': source,
                      'response_time': round(time()-t0, 3),
                      'record_count': rec_count}}
