from ckan.plugins.toolkit import get_action, ObjectNotFound, NotAuthorized


def tableview_datastore_dictionary(resource_id):
    """
    Return the data dictionary info for a resource
    """
    try:
        return [
            f for f in get_action('datastore_search')(
                None, {u'resource_id': resource_id, u'limit': 0})['fields']
            if not f['id'].startswith(u'_')]
    except (ObjectNotFound, NotAuthorized):
        return []
