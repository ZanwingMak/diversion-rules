# diversion-rules

用于维护分流规则、订阅转换配置，以及配套的 `subconverter` 本地规则镜像。

仓库主要配合自建 [sub-web](https://github.com/CareyWang/sub-web) 和 [subconverter](https://github.com/tindy2013/subconverter) 使用。

## 目录说明

- `config/`：通用远程配置。
- `config/personal/`：个人自用配置，目前主要维护 `marvin.ini` 和 `marvin-no-zhuanxian.ini`。
- `rule/`：仓库内自定义规则文件，可直接在配置中引用。
- `subconverter/base/`：`subconverter` 的模板文件。
- `subconverter/example/`：`subconverter` 官方示例配置。
- `subconverter/pref.toml`：`subconverter` 主配置。
- `subconverter/snippets/`：拆分出来的规则集与分组片段。
- `subconverter/rules/`：按来源仓库路径镜像到本地的规则文件。

## 当前配置约定

个人配置以 `config/personal/marvin.ini` 为主，`config/personal/marvin-no-zhuanxian.ini` 为无专线版本。

`subconverter/snippets/` 中当前维护了：

- `rulesets.toml`：本地规则集映射，目前共 `70` 条。
- `groups.toml`：代理分组定义，目前共 `87` 组。
- `emoji.toml`：节点重命名与表情配置。

其中 `rulesets.toml` 的规则路径统一写成：

```toml
path = "rules/xxx/xxx"
```

也就是相对于 `subconverter/` 目录引用本地镜像规则，而不是直接引用远程 URL。

## 本地规则镜像

`config/personal/marvin.ini` 中引用的远程规则，已经同步下载到 `subconverter/rules/`，并保留来源仓库路径层级。

当前目录结构示例：

```text
subconverter/rules/
├── ACL4SSR/ACL4SSR/master/...
├── blackmatrix7/ios_rule_script/master/...
├── tindy2013/subconverter/master/...
└── ZanwingMak/diversion-rules/master/...
```

每个规则文件顶部都会附带来源注释，格式如下：

```text
# SOURCE: https://example.com/path/to/rule.list
```

这样在本地维护时，可以直接追溯到原始下载链接。

## 规则来源

当前本地镜像主要来自这些项目：

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)
- [ACL4SSR/ACL4SSR](https://github.com/ACL4SSR/ACL4SSR)
- [tindy2013/subconverter](https://github.com/tindy2013/subconverter)
- [ZanwingMak/diversion-rules](https://github.com/ZanwingMak/diversion-rules)

如需新增规则，建议先在 `marvin.ini` 中维护来源链接，再同步更新 `subconverter/rules/` 与 `subconverter/snippets/rulesets.toml`。

## 关于 subconverter 规则集数量限制

当前自用规则和分组较多，`subconverter` 默认可显示的规则集数量可能不够。

本仓库已在 `subconverter/pref.toml` 的 `[advanced]` 中设置：

```toml
max_allowed_rulesets = 256
```

相关说明可参考：

- [subconverter README-cn：配置文件 advanced 部分](https://github.com/tindy2013/subconverter/blob/master/README-cn.md#配置文件)
