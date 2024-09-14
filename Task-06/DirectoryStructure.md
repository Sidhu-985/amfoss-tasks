# Directory Structure of Vue Hackernews Website

```
vue-hackernews/
│
├── build/
│   ├── setup-dev-server.js
│   ├── webpack.base.config.js
|   ├── webpack.client.config.js
|   └── webpack.server.config.js
│
├── public/
│   ├── logo-120.png
│   ├── logo-144.png
│   ├── logo-152.png
|   ├── logo-192.png
|   ├── logo-256.png
|   ├── logo-384.png
|   ├── logo-48.png
|   └──  logo-512.png
|
├── src/
|   ├── api/
|   |   ├── create-api-client.js
|   |   ├── create-api-server.js
|   |   └── index.js
|   |
|   ├── components/
|   |   ├── Comment.vue
|   |   ├── Item.vue
|   |   ├── ProgressBar.vue
|   |   └── Spinner.vue
|   |
|   ├── router/
|   |   └── index.js
|   |
|   ├── store/
|   |   ├── actions.js
|   |   ├── getters.js
|   |   ├── index.js
|   |   └──  mutations.js
|   |
|   ├── util/
|   |  ├── filters.js
|   |  └── title.js
|   |
|   ├── views/
|   |   ├── CreateListView.js
|   |   ├── ItemList.vue
|   |   ├── ItemView.vue
|   |   └── UserView.vue
|   |
|   ├── App.vue
|   ├── app.js
|   ├── entry-client.js
|   ├── entry-server.js
|   └── index.template.html
|
├── .babelrc
├── .gitignore
├── LICENSE
├── Readme.md
├── manifest.json
├── package.json
├── server.js
├── yarn.lock
```
