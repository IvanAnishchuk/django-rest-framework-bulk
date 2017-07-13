import rest_framework


class BulkSchemaGenerator(rest_framework.schemas.SchemaGenerator):
    """
    Customized schema generator with bulk actions included
    """

    default_list_mapping = {
        'get': 'list',
        'put': 'bulk_update',
        'patch': 'bulk_partial_update',
        'delete': 'bulk_destroy',
    }
