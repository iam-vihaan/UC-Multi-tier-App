module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.3"

  cluster_name    = var.cluster_name
  cluster_version = "1.27"
  subnet_ids      = var.subnet_ids
  vpc_id          = var.vpc_id

  enable_irsa = true

  eks_managed_node_groups = {
    ec2_nodes = {
      desired_capacity = 2
      max_capacity     = 3
      min_capacity     = 1
      instance_types   = ["t3.medium"]
    }
  }

  fargate_profiles = {
    default = {
      selectors = [
        {
          namespace = "employee-directory"
        }
      ]
    }
  }
}
