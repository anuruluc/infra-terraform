# infra-terraform

## Description
infra-terraform is a Terraform module for automating the deployment of cloud infrastructure. It provides a set of reusable and modular infrastructure components that can be easily configured and deployed using Terraform.

## Features
### Key Features

* **Modular Infrastructure**: infra-terraform provides a set of modular infrastructure components that can be easily composed to create complex infrastructure deployments.
* **Cloud-Agnostic**: infra-terraform supports multiple cloud providers, including AWS, Azure, and Google Cloud Platform.
* **Reusable**: infra-terraform components can be reused across multiple projects and environments.
* **Easy Configuration**: infra-terraform provides a simple and intuitive configuration interface that makes it easy to customize and deploy infrastructure.

### Supported Features

* **Virtual Networks**: Create and manage virtual networks and subnets.
* **Security Groups**: Create and manage security groups and rules.
* **Instances**: Create and manage virtual machines and instances.
* **Storage**: Create and manage storage resources, including volumes and snapshots.
* **Databases**: Create and manage databases, including relational and NoSQL databases.

## Technologies Used

* **Terraform**: Terraform is the primary infrastructure as code tool used to deploy and manage the infrastructure.
* **Cloud Providers**: infra-terraform supports multiple cloud providers, including AWS, Azure, and Google Cloud Platform.
* **Go**: The infra-terraform module is written in Go and uses the Terraform SDK to interact with the Terraform engine.

## Installation

### Prerequisites

* **Terraform**: Terraform 0.14 or later is required to use infra-terraform.
* **Cloud Provider**: A cloud provider account is required to deploy and manage infrastructure.

### Installation Steps

1. **Clone the repository**: Clone the infra-terraform repository using Git.
2. **Initialize the Terraform module**: Run `terraform init` in the root directory of the repository.
3. **Configure the module**: Configure the module by creating a `terraform.tf` file in the root directory of the repository.
4. **Deploy the infrastructure**: Run `terraform apply` to deploy the infrastructure.

## Usage

### Example Usage

```terraform
# Configure the module
module "infra" {
  source = path.module

  # Configure the cloud provider
  cloud_provider = "aws"

  # Configure the virtual network
  virtual_network = {
    name        = "my-vnet"
    cidr_block  = "10.0.0.0/16"
  }

  # Configure the security group
  security_group = {
    name        = "my-sg"
    rules       = [
      {
        protocol  = "tcp"
        from_port = 22
        to_port   = 22
      }
    ]
  }
}
```

### Customizing the Module

The infra-terraform module can be customized by modifying the `terraform.tf` file in the root directory of the repository. This file contains the configuration for the module and can be modified to suit the needs of your project.

## Contributing

We welcome contributions to the infra-terraform module. If you have a feature or bug fix that you would like to contribute, please submit a pull request against the master branch.

## License

The infra-terraform module is licensed under the Apache License 2.0.

## Contact

If you have any questions or need further assistance, please contact us at [support@infra-terraform.com](mailto:support@infra-terraform.com).