# GIT 提交规范

<!-- description: 介绍了GIT 提交的规范格式-->

##  1. 提交信息格式 

Git 提交信息通常包含三部分：
- **类型（type）**：表示本次提交的类别，例如：`feat`（新特性）、`fix`（修复 bug）等。
- **简短描述（subject）**：简短的变更描述，通常不超过 50 个字符，首字母小写，不以句号结尾。
- **详细描述（body）**：对于复杂变更的详细说明，建议每行不超过 72 个字符。

### 格式示例：

```
<type>(<scope>): <subject>

<body>

```



## 2. 常见提交类型

- **feat**：新增功能（feature）
- **fix**：修复 bug
- **docs**：修改文档
- **style**：格式调整（不影响功能）
- **refactor**：重构代码（不影响功能）
- **perf**：性能优化
- **test**：增加/修改测试
- **chore**：杂项任务（构建、配置、依赖更新等）
  - compat:  兼容性更新
  - deps：依赖更新


### 示例：

```
feat(auth): add login feature
fix(user): resolve crash on profile page
docs(readme): update installation instructions
chore(compat): adjust compatibility for Android 12
```

## 3. 分支命名规范

分支命名应简洁且清晰，通常使用以下方式：

- **feature/**：新特性开发，例如 `feature/user-login`
- **bugfix/**：修复 bug，例如 `bugfix/crash-on-login`
- **hotfix/**：紧急修复，例如 `hotfix/critical-bug`
- **release/**：发布版本，例如 `release/v1.2.0`
- **test/**：测试分支，例如 `test/add-new-test`

## 4. 提交类型说明

### 4.1 **`refactor`**：代码重构

- **目的**：改善代码结构、可读性、可维护性，不改变功能。
- **不影响外部行为**：重构后，系统功能和用户体验保持不变。

### 4.2 **`chore`**：维护任务

- **目的**：解决与项目环境、平台、依赖、版本等相关的问题。
- **可能影响外部行为**：例如平台兼容性调整、新依赖库支持等。

#### 为什么 "兼容性调整" 属于 `chore` 而非 `refactor`？

- **`refactor`** 更侧重于改善代码的内部结构，优化功能实现，通常不影响外部行为。
- **`chore`** 关注的是平台适配、依赖更新等维护性任务，通常会影响项目的外部行为或接口。

### 示例：

```
refactor(utils): simplify date formatting function
chore(compat): adjust compatibility for Android 12
```

## 5. 工具支持

可以使用以下工具来确保 Git 提交符合规范：

- **Commitizen**：帮助生成符合规范的提交信息。
- **Husky**：在 Git 提交前进行钩子检查，确保提交信息符合规范。
- **Commitlint**：检查提交信息是否符合规范。

## 6. 提交信息规范的好处

- **提高代码可读性**：清晰的提交信息帮助团队成员理解每次提交的目的和变化。
- **方便追踪和回滚**：通过规范的提交信息，可以快速找到问题发生的具体变动。
- **提高团队协作效率**：团队成员遵循统一的提交规范，能够更有效地沟通和协作。