# IAM Identifiers

IAM uses a few different identifiers for users, user groups, roles, policies,
and server certificates.

- [Friendly Names and Paths](#friendly-names-and-paths)
- [IAM ARN](#iam-arns)
- [Unique Identifiers](#unique-identifiers)

### Friendly Names and Paths

TODO

### IAM ARNs

Most resources have a friendly name for example, a user named Bob or a user
group named Developers. However, the permissions policy language requires you to
specify the resource or resources using the following
**Amazon Resource Name (ARN)** format.

    arn:<partition>:<service>:<region>:<account>:<resource>

ARN Examples

- IAM Role: `arn:aws:iam::111122223333:role/examplerole`
- IAM Role
  Session: `arn:aws:sts::111122223333:assumed-role/examplerole/examplerolesessionname`
- IAM User: `arn:aws:iam::111122223333:user/exampleuser`
- IAM Federated User
  Session: `arn:aws:sts::111122223333:federated-user/exampleuser`

### Unique Identifiers

TODO

### References

- [AWS Docs | IAM Identifiers](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_identifiers.html)
