

# Jekyll | jekyll Front Matter 变量有哪些？

在 Jekyll 中，**Front Matter** 是位于每个页面或文章顶部的元数据部分，用于定义该内容的各种属性和配置。Front Matter 使用 YAML 语法，通常被三条短横线（`---`）包围。以下是 Jekyll 常用的 Front Matter 变量：

### 常见的 Front Matter 变量

1. **layout**

   - **描述**：指定该页面或文章使用的布局模板。

   - 示例

     ：

     ```yaml
     layout: post
     ```

2. **title**

   - **描述**：定义页面或文章的标题。

   - 示例

     ：

     ```yaml
     title: 我的第一篇文章
     ```

3. **date**

   - **描述**：设置文章的发布日期和时间（主要用于博客文章）。

   - **格式**：`YYYY-MM-DD HH:MM:SS +/-TTTT`

   - 示例

     ：

     ```yaml
     date: 2024-12-23 10:00:00 +0800
     ```

4. **categories**

   - **描述**：为文章指定一个或多个分类。

   - 示例

     ：

     ```yaml
     categories: [技术, 编程]
     ```

5. **tags**

   - **描述**：为文章添加标签，便于内容分类和搜索。

   - 示例

     ：

     ```yaml
     tags: [Jekyll, 前端, 静态网站]
     ```

6. **permalink**

   - **描述**：自定义页面或文章的 URL 路径。

   - 示例

     ：

     ```yaml
     permalink: /custom/path/
     ```

7. **published**

   - **描述**：控制内容是否发布。设置为 `false` 时，该内容不会生成。

   - 示例

     ：

     ```yaml
     published: false
     ```

8. **author**

   - **描述**：指定文章的作者。

   - 示例

     ：

     ```yaml
     author: 张三
     ```

9. **excerpt**

   - **描述**：提供文章的摘要，用于显示在列表或预览中。

   - 示例

     ：

     ```yaml
     excerpt: 这是文章的摘要内容。
     ```

10. **draft**

    - **描述**：标记文章为草稿。草稿不会在默认情况下生成，除非使用 `--drafts` 选项。

    - 示例

      ：

      ```yaml
      draft: true
      ```

11. **description**

    - **描述**：为页面或文章添加描述，常用于 SEO 优化。

    - 示例

      ：

      ```yaml
      description: 这是一个示例页面的描述，用于搜索引擎优化。
      ```

12. **image**

    - **描述**：指定文章的特色图片。

    - 示例

      ：

      ```yaml
      image: /assets/images/featured.jpg
      ```

13. **seo_title**

    - **描述**：用于搜索引擎优化的标题，可能与 `title` 不同。

    - 示例

      ：

      ```yaml
      seo_title: 我的文章 SEO 标题
      ```

14. **layout-specific Variables**

    - **描述**：根据所使用的布局模板，可能需要定义特定的变量。例如，如果布局包含侧边栏，可以添加 `sidebar` 变量。

    - 示例

      ：

      ```yaml
      sidebar: true
      ```

### 自定义变量

除了上述标准变量，Jekyll 允许用户在 Front Matter 中定义自定义变量，以便在模板中使用。这些变量的名称和用途由用户自行决定。

**示例**：

```yaml
---
title: 自定义变量示例
custom_var: 这是一个自定义变量
---
```

在模板中，可以通过 `{{ page.custom_var }}` 来引用该变量。

### 示例完整 Front Matter

```yaml
---
layout: post
title: 我的第一篇文章
date: 2024-12-23 10:00:00 +0800
categories: [技术, 编程]
tags: [Jekyll, 前端, 静态网站]
permalink: /blog/my-first-post/
published: true
author: 张三
excerpt: 这是文章的摘要内容。
draft: false
description: 这是一个示例页面的描述，用于搜索引擎优化。
image: /assets/images/featured.jpg
seo_title: 我的文章 SEO 标题
sidebar: true
custom_var: 这是一个自定义变量
---
```

### 注意事项

- **变量命名**：变量名称区分大小写，建议使用小写字母和下划线或短横线。
- **数据类型**：确保变量值的类型正确，例如 `categories` 和 `tags` 应为数组，`published` 和 `draft` 为布尔值。
- **YAML 语法**：确保 Front Matter 的 YAML 语法正确，避免缩进错误或格式问题，否则可能导致 Jekyll 构建失败。

### 参考资料

- [Jekyll 官方文档：Front Matter](https://jekyllrb.com/docs/front-matter/)
- [Jekyll 官方文档：Variables](https://jekyllrb.com/docs/variables/)

通过合理配置 Front Matter 变量，可以更好地管理和展示 Jekyll 站点的内容，提升网站的可维护性和灵活性。