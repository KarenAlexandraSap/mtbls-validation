## METABOLIGHTS VALIDATION FRAMEWORK
MetaboLights validation framework is dynamic and based on [Open Policy Agent](https://www.openpolicyagent.org/) 

View all [MetaboLights Validation Rules](docs/MetaboLightsRules.md)


## Open Policy Agent Deployment 

### Development with vscode
- Install Open Policy Agent exxtension (tsandall.opa)
- Download opa executable from [here](https://www.openpolicyagent.org/docs/latest/#running-opa)
- Update "opa.dependency_paths.opa" settings in .vscode/settings.json to your executable path (e.g., /Users/x/.../opa )


### Run and test validation
```
cd validation
opa test . -v
opa build  --ignore tests .
```
