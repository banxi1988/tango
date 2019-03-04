## Django 中一些值得注意的术语

1. `app_label` 在我之前的意识中， `label` 这个单词是指描述性的文案。但是在 Django 中 `app_label` 指的可是 一个 Django App 的唯一标识。默认是在 App 所在包名的最后一段。文档对此的描述是：
 >AppConfig.label
  Short name for the application, e.g. 'admin'
 >  
 > This attribute allows relabeling an application when two applications have conflicting labels. It defaults to the last component of name. It should be a valid Python identifier.
 > 
 > It must be unique across a Django project. 
