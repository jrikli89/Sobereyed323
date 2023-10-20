# Python Flask modal.tokai

## Description

**Name**: modal.tokai Django Application

**Description**: The modal.tokai application is a state-of-the-art Django-based application delivering robust functionality and convenience to its users. It is architectured based on sound software engineering principles including proper exception handling, data validation, rigorous testing, thorough documentation, separation of concerns, Django's templacing system, stringent security measures, custom error pages, caching, exhaustive logging system, and modularity. Now, it also boasts integration with Pactflow and SwaggerHub to further enhance the application's robustness and versatility.

Our latest improvement is automatic deployment to DigitalOcean whenever a build is successfully completed. This update removes the necessity of manual deployment, making the development process more efficient.

## Getting Started

To begin, you need to connect to your Kubernetes cluster. This can be done directly through kubectl or doctl. More detailed instructions for this process can be found in the DigitalOcean Control Panel.

### How to confirm that Cert-Manager is running

You need to confirm whether Cert-Manager is operating properly. Run:

```bash
helm ls -n cert-manager
kubectl get pods -n cert-manager
```

Your Cert-Manager should be in a READY state and STATUS should be Running.

### Tweaking Helm Chart Values

Helm chart values can be inspected by running the below command.

```bash
helm show values jetstack/cert-manager --version 1.8.0
```

Feel free to adjust the values file (values.yml) according to your requirements.

### Configuring TLS Certificates via Cert-Manager

To create secure connections, you will need to configure TLS certificates via Cert-Manager. Detailed instructions, including the creation of Certificate and Issuer CRDs and necessary annotations can be found in the source code.

### Upgrading and Uninstalling Cert-Manager Stack

For upgrade instructions, navigate to Cert-Manager's official release page on GitHub, or consider using ArtifactHUB for a more user-friendly interface.

```bash
helm upgrade cert-manager jetstack/cert-manager --version <CERT_MANAGER_NEW_VERSION> --namespace cert-manager --values <YOUR_HELM_VALUES_FILE>
```

For uninstallation, execute the following helm command.

```bash
helm uninstall cert-manager -n cert-manager
kubectl delete ns cert-manager
```

### Automatic Deployment to DigitalOcean

Our application is now set to automatically deploy on DigitalOcean upon each successful build. This is accomplished by executing the `build_commands()` function in our manage.py script, which triggers our deployment function `deploy_application()`.

The `deploy_application()` function creates a new droplet in our DigitalOcean account and deploys the application to it.

To deploy your application automatically, Make sure you set your DigitalOcean API key in the digitalocean.py script.

```python
api_key = 'your_digitalocean_api_key'
```

You can modify the deployment process as necessary per your requirements in the `deploy_application()` function.

## Advanced Use 

If you'd like more detailed instructions, check out the following links provided by DigitalOcean: 

- [Configuring Production Ready TLS Certificates for Nginx](#)
- [Configuring Wildcard Certificates via Cert-Manager](#)

## Other Instructions

Continue with other instructions...

## Need Support?

In case of queries or for support, kindly explore our various support resources:

- [Application Documentation](https://docs.modal.tokai.com)
- [Interactive Support Forum](https://ask.modal.tokai.com)
- **Auto-complete**: To enrich user experience and make scripting quick, we have implemented an autocomplete feature throughout our project.
- **Walkthrough**: Our guides and tutorials give detailed, step-by-step instructions, helping users understand, use, and contribute to the application.
- **Regular Updates and Enhancements**: We make consistent updates and modifications to keep our application up-to-date. For detailed version history, see our changelog.
- **Community-Driven Approach**: We value feedback and suggestions from our community of users. We maintain an open dialogue with our users via our interactive forums encouraging all users to participate in the application's development journey.