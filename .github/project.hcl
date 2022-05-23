# Set account-wide variables. These are automatically pulled in to configure the remote state bucket in the root
# terragrunt.hcl configuration.
locals {
  #Required
  organization      = "cvt"
  project           = "Global Emergent Markets"
  codename          = "gem"
  owner             = "Jaya Prabha"
  cost-center       = "TBD"
  application-owner = "e-Zest"
  hosting-owner     = "Cloud Engineering Group"
  validated-system  = "No"
  terraform         = "Yes"

  #Optional
  #tags = {}
}