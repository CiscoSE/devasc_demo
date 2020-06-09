# DevNet Associate Demo Collection - Chapter 7 (Unofficial)

*Collection of DevAsc Chapter 7 demo scripts*

## Usage

To use the examples read the appropriate readmes for the specific chapter. If environment variables are used a creds.template file is available that can be updated with the specific variables that are used in the scripts. That file is a template and is a git tracked file, do not add content directly to the file, first copy the file and rename the extension to .sh then update the new file, creds.sh is included in the git.ignore file to ensure secrets are not shared. As part of good practice store any authorization tokens in that new file and prior to script execution run the bash script to update your environment variables. 

## Demos
### Postman Setup
To perform this sections demos import the collection and environment to your postman instance.

### IOS-XE RestConf API
1. Discover Root of endpoint resource using .well-known/host-meta
2. Get Top Level Resource
3. Get the Running Configuration
4. Get the supported YANG Modules of the device
5. Get all Interfaces
6. Get Specific Interface

### NX-OS NX-API Rest
1. Get Authorization Cookie/Token
2. Get a specific VRF as defined in the environment variables as "vrf" update the variable for uniqueness. On first attempt should return a 200 OK with 0 items. 
3. Create the VRF
4. Delete the VRF

### ACI Rest API
1. Get Authorization Cookie/Token
2. Get all Tenants
3. Get a specific Tenant as defined in the environment variables as "tenant" update the variable for uniqueness. On first attempt should return a 200 OK with 0 items. 
4. Create the Tenant.
5. Get a specific VRF as defined in the environment variables as "vrf" update the variable for uniqueness. On first attempt should return a 200 OK with 0 items. 
6. Create the VRF
7. Delete the VRF
8. Delete the Tenant

### Webex Teams Native Python vs. SDK
1. Ensure you have added the Webex Authorization token to your terminal session environment.
2. Activate the python virtual environment from the root of the repository.
3. Review the code sample in wbxteams_rest.py. 
4. In the script enter the room id you would like to post to. If you do not know the roomID use the Webex Teams API docs to get a list of rooms and the corrosponding Room IDs.
5. This script uses native python Rest calls using the requests library. It will post a message to the specified Room using the provided token stored in the environment variable. Execute the script by using:
    ```
    python wbxteams_rest.py
    ```
6. Review the code sample in wbxteams_sdk.py
7. In the script enter the room id you would like to post to. If you do not know the roomID use the Webex Teams API docs to get a list of rooms and the corrosponding Room IDs.
8. This script uses the community developed python library webexteamssdk to make Rest calls. It will post a message to the specified Room using the provided token stored in the environment variable. Execute the script by using:
    ```
    python wbxteams_sdk.py
    ```

The demostration of these two scripts highlights the value and speed to development when using SDKs but still provides the basics on how to leverage native libraries.