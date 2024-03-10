Issue Summary:

Duration: March 8, 2024, 10:00 AM to March 9, 2024, 2:00 AM (UTC)
Impact: A 12-hour outage affected the availability of our web application, resulting in a service      downtime for all users. Approximately 80% of our user base experienced inability to access the platform or encountered significant delays.
Root Cause: The outage was caused by a misconfiguration in the load balancer settings, leading to an overload on our database servers.
Timeline:

10:00 AM: Issue detected through monitoring alert indicating unusually high latency.
10:05 AM: Engineering team investigated potential causes, initially suspecting database performance issues.
11:00 AM: Misleading assumption made that recent code deployment might have caused database queries to become inefficient.
12:30 PM: Incident escalated to senior engineering team as problem persisted.
1:00 PM: Further investigation revealed load balancer misconfiguration as the likely culprit.
2:00 PM: Load balancer settings adjusted to distribute traffic evenly across database servers.
2:30 PM: Service partially restored, but performance remained degraded.
4:00 PM: Additional optimizations made to database queries to alleviate strain on servers.
8:00 PM: Service fully restored as load balancer adjustments propagated across all regions.
Root Cause and Resolution:

The root cause of the outage was traced to a misconfigured load balancer, which was sending an unequal distribution of traffic to our database servers. This led to an overload on certain servers, causing high latency and service degradation.

To resolve the issue, we adjusted the load balancer settings to evenly distribute traffic across all database servers. Additionally, optimizations were made to database queries to reduce the strain on the servers and improve overall performance.

Corrective and Preventative Measures:

Improvements/Fixes:

Implement regular audits of load balancer configurations to prevent similar misconfigurations.
Enhance monitoring systems to quickly identify and alert on imbalanced traffic distribution.
Conduct thorough testing of code deployments to ensure compatibility with existing infrastructure.
Tasks to Address the Issue:

Schedule a comprehensive review of load balancer configurations by the infrastructure team.
Implement automated checks to verify load balancer settings against predefined thresholds.
Conduct a postmortem review with the engineering team to identify lessons learned and areas for improvement in incident response procedures.
By implementing these corrective measures and conducting thorough reviews of our infrastructure and monitoring systems, we aim to minimize the risk of similar incidents in the future and ensure the continued reliability of our web application for our users.

