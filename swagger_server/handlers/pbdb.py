"""Custom decoder logic for the Paleobiology Database response."""


def locales(resp_json, return_obj, options):
    """Extract locale data from the subquery."""
    from ..elc import ages

    factor = ages.set_age_scaler(options=options, db='pbdb')

    for rec in resp_json.get('records', []):

        data = dict()

        data.update(locale_id='pbdb:{0:s}'.format(rec.get('oid', 'col:0')))
        data.update(doi=None)

        data.update(source='pbdb:{0:s}'.format(rec.get('rid', 'ref:0')))
        data.update(locale_name=rec.get('nam'))
        data.update(data_type=rec.get('cct', 'general faunal/floral'))
        data.update(occurrences_count=rec.get('noc'))
        data.update(site_id=None)

        data.update(max_age=round(rec.get('eag') / factor, 4))
        data.update(min_age=round(rec.get('lag') / factor, 4))

        if options.get('geog') == 'paleo':
            data.update(lat=rec.get('pla'))
            data.update(lon=rec.get('pln'))
        else:
            data.update(lat=rec.get('lat'))
            data.update(lon=rec.get('lng'))

        return_obj.append(data)

    return return_obj


def occurrences(resp_json, return_obj, options):
    """Extract occurrence data from the subquery."""
    from ..elc import ages

    factor = ages.set_age_scaler(options=options, db='pbdb')

    for rec in resp_json.get('records', []):

        data = dict()

        data.update(occ_id='pbdb:{0:s}'.format(rec.get('oid', 'occ:0')))

        data.update(taxon=rec.get('tna'))
        data.update(taxon_id='pbdb:{0:s}'.format(rec.get('tid', 'txn:0')))

        data.update(max_age=round(rec.get('eag') / factor, 4))
        data.update(min_age=round(rec.get('lag') / factor, 4))

        data.update(source='pbdb:{0:s}'.format(rec.get('rid', 'ref:0')))
        data.update(data_type=rec.get('cct', 'general faunal/floral'))
        data.update(locale_id='pbdb:{0:s}'.format(rec.get('cid', 'col:0')))

        # !!! geog stuff here

        return_obj.append(data)

    return return_obj


def references(resp_json, return_obj, options):
    """Extract references data from the subquery."""
    import re

    for rec in resp_json.get('records', []):

        data = {'title': rec.get('tit'),
                'kind': rec.get('pty'),
                'year': rec.get('pby'),
                'journal': rec.get('pbt'),
                'editor': rec.get('eds'),
                'doi': rec.get('doi'),
                'cite': rec.get('ref')}

        # Reference number
        data.update(ref_id='pbdb:{0:s}'.format(rec.get('oid', 'occ:0')))

        # Publication volume(number)
        if rec.get('vno'):
            if rec.get('vol'):
                data.update(vol_no='{0:s} ({1:s})'.format(rec.get('vol'),
                                                          rec.get('vno')))
            else:
                data.update(vol_no=rec.get('vno'))
        else:
            data.update(vol_no=None)

        # Reference page range as first-last
        if rec.get('pgf'):
            if rec.get('pdl'):
                data.update(page_range='{0:s}-{1:s}'.format(rec.get('pgf'),
                                                            rec.get('pgl')))
            else:
                data.update(page_range=rec.get('pgf'))
        else:
            data.update(page_range=None)

        # Build author list
        author_list = list()

        if rec.get('author1last'):
            author1 = rec.get('author1last').replace(',', '')
            if rec.get('author1init'):
                author1 = '{0:s}, {1:s}'.format(author1,
                                                rec.get('author1init'))
            author_list.append(author1)

        if rec.get('author2last'):
            author2 = rec.get('author2last').replace(',', '')
            if rec.get('author2init'):
                author2 += ', ' + rec.get('author2init')
            author_list.append(author2)
        if 'otherauthors' in rec:
            more_authors = rec.get('otherauthors').split(', ')
            for next_author in more_authors:
                surname = re.search('[A-Z][a-z]+', next_author)
                name = surname.group() + ', ' + \
                    next_author[0: surname.start()-1]
                name = name.replace(', and', ', ')
                author_list.append(name)



                #  # Format and append parsed record
                #  ret_obj = format_handler(reference, ret_obj, format)

        return_obj.append(data)

    return return_obj
