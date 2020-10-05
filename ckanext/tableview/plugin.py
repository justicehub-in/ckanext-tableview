# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit

default = toolkit.get_validator(u'default')
boolean_validator = toolkit.get_validator(u'boolean_validator')
ignore_missing = toolkit.get_validator(u'ignore_missing')


class TableView(p.SingletonPlugin):
    """
    DataTables table view plugin
    """
    
    if not p.toolkit.check_ckan_version('2.3'):
        raise p.toolkit.CkanVersionException(
            'This extension requires CKAN >= 2.3. If you are using a ' +
            'previous CKAN version the PDF viewer is included in the main ' +
            'CKAN repository.')
    
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IConfigurable, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IRoutes, inherit=True)
    p.implements(p.ITemplateHelpers)

    def update_config(self, config):
        """
        Set up the resource library, public directory and
        template directory for the view
        """
        p.toolkit.add_public_directory(config, 'public')
        p.toolkit.add_template_directory(config, 'templates')
        p.toolkit.add_resource('public', 'tableview')

    def can_view(self, data_dict):
        resource = data_dict['resource']
        return resource.get(u'datastore_active')

    def view_template(self, context, data_dict):
        return u'datatables_view.html'

    def form_template(self, context, data_dict):
        return u'datatables_form.html'
    
    def get_helpers(self):
        from ckanext.tableview import helpers as datatablesview_helpers
        return {
                'tableview_datastore_dictionary': datatablesview_helpers.tableview_datastore_dictionary,
                }

    def info(self):
        return {
            u'name': u'table_view',
            u'title': u'Table',
            u'filterable': True,
            u'icon': u'table',
            u'requires_datastore': True,
            u'default_title': p.toolkit._(u'Table'),
            u'schema': {
                u'responsive': [default(False), boolean_validator],
                u'show_fields': [ignore_missing],
                u'filterable': [default(True), boolean_validator],
            }
        }

    def before_map(self, m):
        m.connect(
            u'/tableview/ajax/{resource_view_id}',
            controller=u'ckanext.tableview.controller'
                       u':TableViewController',
            action=u'ajax')
        return m
