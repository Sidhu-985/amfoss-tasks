# Documentation for Vue Hackernews 2.0

## Overview
Vue Hackernews 2.0 is an educational project designed to display,build certain stories on whats happening in todays world of **Programming**.
The project includes various scripts that teach fundamental programming concepts and help users create through UI and animations with Vue.

## Functionality

### Models

#### Views

- **ItemList.vue**
  - Displays a list of stories.

- **ItemView.vue**
  - Shows details of specific Hacker News page with comments.

- **UserView.vue**
  - Displays details about the user.

#### Components

- **Comment.vue**

  - Displays comments for each news page.

- **Item.vue**

  - Displays a single news page.

- **ProgressBar.vue**

  - Shows a progress bar during loading time.
    
- **Spinner.vue**

  - Displays a circular spinning while data is being fetched from API.
    
#### API

- **`create-api-client.js`**

  - API client to make requests for certain data to the Hacker News API from the client side.

- **`create-api-server.js`**
  - API server setted up for server-side interactions.

- **`index.js`**
  - Uses methods for fetching data(items and users) from the Hacker News API.

#### Utilities

- **`filters.js`**
  - Filters the news pages based on date or numbers.

- **`title.js`**
  - Displays the title of the news document page based on the current route.

#### Router

- **`index.js`**
  
  - Configures routes and maps them to their respective components, enabling navigation within the app.
    
## Implementation details
You can find all the code files by referring to our directory structure.

### Build
The part containing webpack configuration files for client and server builds is present in ```build/``` directory.

### Images and Logo
Assets such as images and logos of different sizes are in ```public/``` directory.

### Main UI
The main components of the website is present in ```src/``` including components,views,API setup,utilities and Vuex store.

# Code Example
```js
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// route-level code splitting
const createListView = id => () => import('../views/CreateListView').then(m => m.default(id))
const ItemView = () => import('../views/ItemView.vue')
const UserView = () => import('../views/UserView.vue')

export function createRouter () {
  return new Router({
    mode: 'history',
    fallback: false,
    scrollBehavior: () => ({ y: 0 }),
    routes: [
      { path: '/top/:page(\\d+)?', component: createListView('top') },
      { path: '/new/:page(\\d+)?', component: createListView('new') },
      { path: '/show/:page(\\d+)?', component: createListView('show') },
      { path: '/ask/:page(\\d+)?', component: createListView('ask') },
      { path: '/job/:page(\\d+)?', component: createListView('job') },
      { path: '/item/:id(\\d+)', component: ItemView },
      { path: '/user/:id', component: UserView },
      { path: '/', redirect: '/top' }
    ]
  })
}
```
