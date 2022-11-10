# IAM JSON Policies

### Policy Types

An IAM Policy is an object that defines the permissions attached to an
_identity_ or _resource_. The following policy types supported AWS IAM:

- [Identity-Based Policy](#identity-based-policy)
- [Resource-Based Policy](#resource-based-policy)
- [Session Policy](#session-policy)
- [Permission Boundary](#permission-boundary)
- [Service Control Policy (SCP)](#service-control-policy-scp)
- [Access Control Lists (Legacy Policy Type)](#access-control-lists-legacy-policy-type)

##### **Identity-Based Policy**

Defines what actions an IAM Identity (user, group, or role) are allowed to take
against specific resources.

Example: Granting permissions to an IAM user access to perform certain actions
such as `ec2:DescribeInstances`, `s3:ListBuckets`, `s3:PutObject`,
`cloudformation:CreateStack`, etc.

##### Resource-Based Policy

Resource-based policies are policies that are associated or attached to a
specific resource. They are used to define who (principals) has access to a
resource regardless of whether the resource exists in the same account or
another AWS account.

Some popular resource-based policies are S3 bucket policies and IAM role trust
policies (aka Trust Relationships).

##### Permission Boundary

Permission boundaries create a logical boundary around the permissions that can
be defined for an IAM Entity (User or Role) to explicitly allow a maximum set of
permissions. Permission boundaries are a great way to implement the principle of
the least privilege to ensure that an IAM Entity never has more privileges than
are necessary to perform their job function. Permission boundaries don't grant
permissions, so you still need to use identity or resource policies to grant
access.

See my
[permission boundaries](https://medium.com/geekculture/aws-iam-permissions-boundaries-781ca8c8e9c0)
Medium post for more info.

##### Service Control Policy (SCP)

AWS Organizations not only allows you to divide your organization into logical
business units and manage AWS billing across many AWS accounts, it also enables
you to set permissions across your AWS accounts using service control policies
(SCPs). SCPs act as **guardrails** for your AWS accounts and thus have a
similar role to a permission boundary or session policy in that they only set
permissions limits but don’t explicitly grant permissions - permissions are
still granted via identity-based or resourced-based policies.

##### Session Policy

Session policies are the most sophisticated type of IAM policy and serve an
equivalent purpose as a permission boundary — they limit the permissions
attached to temporary credentials that have been created using the AssumeRole*
or GetFederationToken APIs. A sessions permissions is the result of the
intersection between an identity-based policy (for the IAM entity that created
the session), a resource-based policy (if one is defined), and the session
policy.

[AWS session policy docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session)

##### Access Control Lists (Legacy Policy Type)

Access control lists (ACLs) are similar to resource-based policies in that they
allow cross-account access to a resource they are attached to, however, ACLs can
only be used for defining cross-account access, not access within the same
account. ACLs are also the only type of policy that don’t evaluate access based
on a JSON policy document. ACLs are a legacy policy type and AWS recommends
modernizing security strategy by disabling ACLs and using identity-based or
resource-based policies.

##### Policy Elements

- [IAM JSON Policy Elements: Version](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_version.html)
- [IAM JSON Policy Elements: Id](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_id.html)
- [IAM JSON Policy Elements: Statement](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_statement.html)
- [IAM JSON Policy Elements: Sid](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_sid.html)
- [IAM JSON Policy Elements: Effect](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_effect.html)
- [IAM JSON Policy Elements: Principal](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_principal.html)
- [IAM JSON Policy Elements: NotPrincipal](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_notprincipal.html)
- [IAM JSON Policy Elements: Action](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_action.html)
- [IAM JSON Policy Elements: NotAction](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_notaction.html)
- [IAM JSON Policy Elements: Resource](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_resource.html)
- [IAM JSON Policy Elements: NotResource](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_notresource.html)
- [IAM JSON Policy Elements: Condition](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_condition.html)
- [Variables and Tags](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_variables.html)
- [Supported Data Types](https://docs.aws.amazon.com/IAM//latest/UserGuide/reference_policies_elements_datatypes.html)

###### References

- [Medium.com | AWS IAM Policy Types - Flexible Access Control for Finer-Grained Permissions](https://medium.com/geekculture/aws-iam-policy-types-c26d8d45eb95)
