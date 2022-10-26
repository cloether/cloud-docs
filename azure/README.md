# Microsoft Azure

### Azure Logging and Monitoring

- [Data Collection Best Practices](https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-data-collection)

##### Azure Cloud Adoption Framework

- [Monitoring - Service Level Objectives](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/monitor/service-level-objectives)
- [Cloud Models - Monitoring Overview](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/monitor/cloud-models-monitor-overview)
- [Monitoring Strategy](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/strategy/monitoring-strategy)

##### Azure Monitor

- [Azure Monitor - Security Controls using Azure Policy](https://learn.microsoft.com/en-us/azure/azure-monitor/security-controls-policy#azure-security-benchmark)

##### Azure Monitor Logs

- [Azure Monitor Logs - Workspace Design](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/workspace-design)
- [Azure Monitor Logs - Data Retention and Archive](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive?tabs=portal-1%2Cportal-2)

##### ARM Schemas

- [Github - Azure/azure-resource-manager-schemas](https://github.com/Azure/azure-resource-manager-schemas)

<hr>

##### Azure Platform Logs

- Activity Logs
    - Subscription-Level Events
    - Default Retention: `90 Days`
    - Automatically Collected/Generated
        - Forward to a Destination for Longer Retention
    - Log Analytics Table: `AzureActivity`

- Resource Logs
    - Resource-Level Events
    - Provide detailed diagnostic and auditing information for Azure resources
      and the Azure platform they depend on.
    - Are not collected until they're routed to a destination

- [Azure Active Directory Logs](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/overview-reports)
    - Tenant-Level Events
    - Automatically Collected/Generated: Yes
    - Cost
        - Sending to Log Analytics: No
        - Log Analytics Data Ingestion: Yes
        - Log Analytics Data Retention: Yes
    - [How-To Integrate Activity Logs with Log Analytics](https://learn.microsoft.com/en-us/azure/active-directory/reports-monitoring/howto-integrate-activity-logs-with-log-analytics)
    - [Azure Sentinel - Connect Azure AD Logs](https://learn.microsoft.com/en-us/azure/sentinel/connect-azure-active-directory)

- Log Destinations
    - Log Analytics
        - Retention
          Mechanism: [Archive Policy](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-retention-archive?tabs=portal-1%2Cportal-2)
        - [Pricing](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/cost-logs)
    - Storage Account
        - Retention
          Mechanism: [Lifecycle Management Policy](https://learn.microsoft.com/en-us/azure/storage/blobs/lifecycle-management-policy-configure?tabs=azure-portal)
    - Event Hub
    - Partner Integrations

##### References

- [Log Management Fundamentals for Cybersecurity Engineers](https://medium.com/microsoftazure/log-management-fundamentals-for-cybersecurity-engineers-33e433677a0b)
- [Highly Effective Azure Monitoring with Azure Log Analytics](https://medium.com/microsoftazure/highly-effective-azure-monitoring-with-azure-log-analytics-ac4810e5dc97)
- [Microsoft Cybersecurity Reference Architectures](https://learn.microsoft.com/en-us/security/cybersecurity-reference-architecture/mcra)

- [Understanding Azure Logs from a security perspective — Part 1 — Activity Logs](https://davidokeyode.medium.com/understanding-azure-logs-part-1-activity-logs-e5483c7b8a46)
- [Understanding Azure Logs from a security perspective — Part 2 — NSG Flow Logs](https://davidokeyode.medium.com/understanding-azure-logs-from-a-security-perspective-part-2-nsg-flow-logs-3edc5c42f39a)
- [Log Management Fundamentals for Cybersecurity Engineers](https://medium.com/microsoftazure/log-management-fundamentals-for-cybersecurity-engineers-33e433677a0b)
- [Security Log Management Lifecycle with Microsoft Sentinel](https://medium.com/microsoftazure/security-log-management-lifecycle-with-microsoft-sentinel-2dd8c7d983c)
- [Incident Case Management on Sentinel — Syncing status between different solutions](https://medium.com/microsoftazure/incident-case-management-on-sentinel-syncing-status-between-different-solutions-bc7a8076669e?source=collection_home---4------1-----------------------)

