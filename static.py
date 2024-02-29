class ResponseStatusCode():
    success = 200
    created = 201
    found = 302
    not_modified = 304
    bad_request = 400
    forbidden = 403
    not_found = 404
    unauthorized = 401
    already_exists = 409
    internal_server_error = 500


class ResponseStatus():
    success = 'success'
    error = 'error'


class ResponseMessage():
    success = "Success"
    failed = "Something went wrong"
    not_found = "Not Found"
    duplicate_request = "Duplicate request"
    error = "Internal server error"
    fees_created = "Fees Created Successfully"
    fees_deleted="Fees Deleted Successfully"
    promotion_created="Promotions Created Successfully"