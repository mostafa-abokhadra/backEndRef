### installing packages
- once you install your first package, a node_modules folder will be created and the package installed will be inside it.
- also package.json file will be updated, dependencies field will be added with the package installed e:g
```json
{
    "dependencies": {
        "packageName": "^packageVersion"
    }
}
```
- also package-lock.json file will be created once you installed your first package, then the same file will be updated for subsequent packages, this file simpley keeps track of the packages and version you install using npm in the project and ensuring there is no inconsistincies when some one else install the same packages