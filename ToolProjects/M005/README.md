# "prov" Provisioning infrastructure and development environments

When working as a software developer you will constantly need to install stuff and document what you have done.

This is necessary to e.g.:
- create consistent developer environments for your developer group
- create consistent build machines for your continuous integration workflow
- create test environments
- create staging environments
- create production environments (at least you have to be able to communicate the needs to system administrators)

Optimally you document in a way that is repeatable and can be executed automatically.

When you get stuck and do not know what you need, take 1..n of the projects you have already implemented and think: what if you would need to quickly create all the environments mentioned above for these.

## Requirements

### degree of detail

- [ ] Make sure that you install and/or document the specific version of each tool. Do not simply use "an installer from the internet for node" but instead install node 16.0.10 e.g. to make sure that the environments you create are really consistent.

### locations

- [ ] You can easily set up an environment on a hoster, like vultr.
- [ ] You can easily set up a vm environment on your local computer.
- [ ] You can easily install a local machine to make it the way you need it. E.g. a physical laptop. Not a virtual machine.
- [ ] You can easily create docker containers.

### variants

- you might try to use provisioning tools that are already available, like terraform, ansible, chef ... still, keep in mind that they contain lots of code and might become a weak spot in your environment creation process by themselfs, as they might break when you do not expect it

## Progressive Levels

### Level 0 - Local Setup
- [ ] Add version control
  - Specific versions
  - Dependencies
  - Compatibility
- [ ] Create local installation
  - Physical machines
  - Developer laptops
  - Manual processes
- [ ] Implement documentation
  - Setup guides
  - Requirements
  - Troubleshooting

### Level 1 - Virtualization
- [ ] Add VM support
  - Local VMs
  - Configuration
  - Networking
- [ ] Create containers
  - Docker setup
  - Image building
  - Container management
- [ ] Implement automation
  - Scripts
  - Templates
  - Workflows

### Level 2 - Cloud Integration
- [ ] Add cloud providers
  - Vultr setup
  - AWS support
  - Azure integration
- [ ] Create environments
  - Development
  - Staging
  - Production
- [ ] Implement scaling
  - Load balancing
  - Auto-scaling
  - Resource management

### Level 3 - Infrastructure
- [ ] Add configuration
  - Environment vars
  - Config files
  - Secrets
- [ ] Create networking
  - VPN setup
  - Security groups
  - DNS management
- [ ] Implement monitoring
  - Health checks
  - Metrics
  - Alerts

### Level 4 - CI/CD
- [ ] Add build machines
  - CI setup
  - Build agents
  - Test environments
- [ ] Create deployment
  - Release process
  - Rollback
  - Blue-green
- [ ] Implement validation
  - Environment checks
  - Security scans
  - Compliance

### Level 5 - Enterprise
- [ ] Add governance
  - Access control
  - Audit logs
  - Compliance
- [ ] Create disaster recovery
  - Backup strategy
  - Recovery plans
  - Failover
- [ ] Implement optimization
  - Cost management
  - Performance
  - Resource usage

## Environments
- Development
- Testing
- Staging
- Production
- CI/CD
- Disaster recovery

## Best Practices
- Version control
- Documentation
- Automation
- Security
- Monitoring
- Cost optimization
