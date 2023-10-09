# dynatrace-scripts
Various scripts to help automate Dynatrace configurations and actions.
## bulk-change-settings.py
This script is designed to apply a settings 2.0 configuration to a collection of entities defined by an entitySelector string.

How to run the script:
1. Set variables in script (lines 5-9)
    1. env
       
       SaaS: `https://{your-environment-id}.live.dynatrace.com`
       
       Managed: `https://{your-domain}/e/{your-environment-id}`
    3. token
  
       API token. Scopes required: `entities.read,settings.write`
    5. entitySelector
  
       Specifies the entities to apply the configuration to. Example: `type(PROCESS_GROUP),tag(myapp)`

    7. schema

       The schema of the settings 2.0 configuration you want to apply. Found by clicking the 3 dots-> Schema Info Example: `builtin:availability.process-group-alerting`
    9. value
  
       This is the value object inside of the settings API request body. This can be easily found for your configuration by clicking the 3 dots in the upper right hand corner of the UI for the config. From here select "API". Now you will pull up the "add as a new value" or "update value" option. Inside of here you will copy the value object contents.

       Example: `{"enabled":true,"alertingMode":"ON_INSTANCE_COUNT_VIOLATION","minimumInstanceThreshold":1}`

    Full Example of lines 5-9:
    ```
    env="https://{your-environment-id}.live.dynatrace.com"
    token="<Api-Token>"
    entitySelector="type(PROCESS_GROUP),tag(myapp)"
    schema="builtin:availability.process-group-alerting"
    value = '{"enabled":true,"alertingMode":"ON_INSTANCE_COUNT_VIOLATION","minimumInstanceThreshold":1}'
    ```

3. Run script

   `python bulk-change-settings.py`
