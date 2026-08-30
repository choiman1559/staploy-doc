# Staployfile Language Reference


## 1. Overview


## 2. Syntax

### 2.1 HCL Syntax

### 2.2 Labels

### 2.3 Attributes

### 2.4 Blocks

### 2.5 Expressions

## 3. Global Blocks

### 3.1 `configure`

### 3.2 `alias`

### 3.3 `build`

### 3.4 `manage`

### 3.5 `target`

## 4. Alias

### 5.1 Worker Alias

### 5.2 App Alias

## 6. Worker Expressions

### 6.1 Worker ID and Name

### 6.2 `group:` Expression

### 6.3 `alias:` Expression

### 6.4 `where` Block

## 7. Application References

### 7.1 Application Name

### 7.2 Application Version

### 7.3 `alias:` Expression

### 7.4 Shell Version Expression

## 8. Build

## 9. Manage Operations

### 9.1 `create`

### 9.2 `upload`

### 9.3 `delete`

### 9.4 `pull`

## 10. Target Operations

### 10.1 `unset`

### 10.2 `remove`

### 10.3 `deploy`

### 10.4 `push_only`

### 10.5 `set_active`

### 10.6 `disconnect`

## 11. Shell Hooks

### 11.1 `pre_deploy`

### 11.2 `post_deploy`

### 11.3 Shell Execution

## 12. Execution Order

### 12.1 File Execution Order

### 12.2 Target Operation Order

## 13. Resolution Rules

### 13.1 Worker Alias Resolution

### 13.2 App Alias Resolution

### 13.3 Build Artifact Resolution

## 14. Error Handling

## 15. Examples
