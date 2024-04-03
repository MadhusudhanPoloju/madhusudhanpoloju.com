# GCP provider

provider "google" {
  credentials = file(variable.gcp_svc_key)
  project = variable.gcp_project
  region = variable.gcp_region
}