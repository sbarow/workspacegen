# WorkSpaceGen
Generate Xcode Workspaces from `project.yml` file.

Uses [XcodeGen](https://github.com/yonaskolb/XcodeGen) to generate `.xcodeproj` files and then builds a Workspace based on the project dependencies.

### TODO
 
 - [ ] Project generation
 - [ ] Use `.workspacegen` file to define aliases for project instead of search project for `project.yml` files
 - [ ] Ability to define Schemes that should be included in workspace
 - [ ] Static libraries & strings/images. 
 - [ ] Warn on missing dependency in App target - implicit framework dependencies are used therefore are not copied into the app's frameworks dir if the app does not include the dep in its `project.yml` file. This will cause a crash when running on a device that the framework can't be found.
 - [ ] Investigate static libraries
 - [ ] Quit Xcode if open before opening generated workspace
 - [ ] Documentaion
 - [ ] Tests

### Whats up with the Python

- Wanted to learn python (this code could be horrendous, I have no idea, but it works)
- Swift is always ~~breaking~~changing
