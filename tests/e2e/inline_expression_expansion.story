function build_jira_request_body body:any returns any
    return {} as Map[any,any]

function create_jira_issue body:any returns any
    return http fetch body: build_jira_request_body(body:body) url: "foobar"
