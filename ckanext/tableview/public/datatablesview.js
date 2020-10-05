this.ckan.module('table_view', function (jQuery) {
  return {
    initialize: function() {
      jQuery('#dtprv').DataTable({});
    }
  }
});
