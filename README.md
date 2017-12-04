# Xcode WorkSpace Gen

Uses [XcodeGen](https://github.com/yonaskolb/XcodeGen) to generate `.xcodeproj` from `project.yml` files and then builds a Workspace based on the project dependencies.

### Usage

Copy this into the root folder of your iOS repo. 

```
tools/workspacegen
```

Create a python script in the root of your directory named `workspacegen` with the following content

```
#!/usr/bin/env bash

"${0%/*}"/path/to/workspace.py "$@"
```

Running commands would then be done with:

```
./workspacegen {command}
```

**Available Commands**

- `list_targets` - list all available targets by searching project directory for `project.yml` files
- `clean` - Deletes `.xcodeproj` & `.xcworkspace` files (**careful**)
- `project` - Generates `.xcodeproj` & an `.xcworkspace` for the specified target.

### TODO
 
 - [X] Project generation
 - [ ] Use `.workspacegen` file to define aliases for project instead of search project for `project.yml` files
 - [ ] Ability to define Schemes that should be included in workspace
 - [ ] Static libraries & strings/images. 
 - [ ] Warn on missing dependency in App target - implicit framework dependencies are used therefore are not copied into the app's frameworks dir if the app does not include the dep in its `project.yml` file. This will cause a crash when running on a device that the framework can't be found.
 - [ ] Investigate static libraries
 - [ ] Quit Xcode if open before opening generated workspace
 - [ ] Bootstrap - Fetch all carthage dependencies and build (too slow?), install xcode templates etc.
 - [ ] Sort xml alpha/grouped
 - [ ] Paths to dependencies (would need changes in `XcodeGen`)
 - [ ] Documentaion
 - [ ] Tests

### Whats up with the Python

- Wanted to learn python (seriously this is the first time I have ever written it, this code could be horrendous, I have no idea, but it works)
- Swift is always ~~breaking~~changing
