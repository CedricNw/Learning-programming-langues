import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faHome, faUser, faBars, faAngleDoubleLeft} from '@fortawesome/free-solid-svg-icons'

// Icons der Library hinzufügen
library.add(faHome, faUser, faBars, faAngleDoubleLeft)

// App initialisieren
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)

app.mount('#app')