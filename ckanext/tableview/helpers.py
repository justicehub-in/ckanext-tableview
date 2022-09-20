from ckan.plugins.toolkit import get_action, ObjectNotFound, NotAuthorized
#from ckan.common import config
from pylons import config
import pandas as pd
import requests
import io


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
    except Exception as e:
        return []


def tableview_theme():
    """
    Return tableview theme string from config file
    """
    theme = config.get("ckan.tableview_theme")
    return theme if theme else str(theme)

def tableview_cols(pkg, res):
    url = 'https://openbudgetsindia.org/dataset/' + str(pkg) + "/resource/" + str(res) + "/download/data.csv"  
    s = requests.get(url).content 
    data = pd.read_csv(io.StringIO(s.decode('utf-8')), header=0).fillna('')
    cols = list(data.columns)  
    return cols
