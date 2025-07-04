module "vpc" {
  source = "../modules/vpc"
}

module "eks" {
  source       = "../modules/eks"
  cluster_name = "employee-cluster"
  vpc_id       = module.vpc.vpc_id
  subnet_ids   = module.vpc.subnet_ids
}

module "iam" {
  source = "../modules/iam"
}

module "rds" {
  source = "../modules/rds"
}
